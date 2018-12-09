import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThreadPool

import logging
import numpy as np
import json
import math
from functools import partial

import constants
import utils
import num_methods

from ui.main_window import Ui_MainWindow
from initial_window import InitialWindow
from simple_thread import Worker


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, filesMap, auto=None, betta=None, betta0=None, betta1=None, x=None, y=None, T=None):
        super().__init__()

        self.setupUi(self)

        self.funcDict = {
            constants.PLAN: None,
            constants.PROB: None,
            constants.TRAF: None,
        }
        self.uFunc = None

        self.filesMap = filesMap
        self.firstCrtField.setEnabled(not auto)
        self.secondCrtField.setEnabled(not auto)
        self.bettaField.setEnabled(auto)
        self.bettaEdit.setEnabled(not auto)

        self.bettaStr = ''
        self.auto = auto
        self.T = T
        self.y0 = y
        self.c1Weight = 1.0
        self.c2Weight = 1.0
        validator = QtGui.QDoubleValidator(self)
        locale = QtCore.QLocale("en")
        validator.setLocale(locale)

        if auto:
            self.x0 = None
            self.betta = (betta0, betta1)
            self.c1WeightEdit.setValidator(validator)
            self.c2WeightEdit.setValidator(validator)
        else:
            self.x0 = x
            self.betta = betta
            self.bettaEdit.setValidator(validator)
            self.bettaEdit.setText('0.1')

        self.initBaseFuncs()
        self.initPlots()
        self.drawBasePlots()

        self.startBtn.clicked.connect(self.start)
        self.saveS.setEnabled(False)
        self.saveP.setEnabled(False)
        self.saveZ.setEnabled(False)

        self.threadpool = QThreadPool()
        self.show()

    def log(self, text):
        self.logTextEdit.insertPlainText(str(text) + '\n')

    def start(self):
        if self.auto:
            try:
                self.c1Weight = float(self.c1WeightEdit.text())
                self.c2Weight = float(self.c1WeightEdit.text())
            except:
                self.c1Weight = 1.0
                self.c2Weight = 1.0
                self.c1WeightEdit.setText(str(self.c1Weight))
                self.c2WeightEdit.setText(str(self.c2Weight))
        else:
            try:
                self.betta = float(self.bettaEdit.text())
            except:
                self.betta = 0.1
                self.bettaEdit.setText(str(self.betta))

        worker = Worker(self.calcWeightFuncs)
        worker.signals.result.connect(self.initWeightFuncs)
        worker.signals.progress.connect(self.log)
        self.threadpool.start(worker)

    def initBaseFuncs(self):
        self.log('Initing base funcs')
        self._loadFuncs()
        self.correctProb = lambda w: 0 if w < 0 or w > 1 else self.funcDict[constants.PROB](w)

    def calcWeightFuncs(self, progress_callback):
        progress_callback.emit('Calculating U(y) function')
        integral = num_methods.integral.TrapzIntegral(self.correctProb, nodes_num=5000)
        uFunc = num_methods.interpolation.SplineInterpolation(
            utils.Tabulate(
                integral,
                (0, 1, 1e-3)
            )
        )
        progress_callback.emit('Finding threshold strategy')
        solver = num_methods.solver.Solver(self.x0, self.y0, self.betta, self.T,
                                                    u=uFunc,
                                                    s=self.funcDict[constants.PLAN],
                                                    z=self.funcDict[constants.TRAF],
                                                    p=self.correctProb,
                                                    auto=self.auto,
                                                    c1_weight=self.c1Weight,
                                                    c2_weight=self.c2Weight,
                                                    progress_callback=progress_callback.emit)

        return uFunc, solver.solve()

    def initWeightFuncs(self, results):
        self.log('Initing weight funcs')
        self.uFunc, other = results
        if self.auto:
            self.real_shows, self.threshold, self.betta_opt, self.c1, self.c2, self.lossFunc = other
        else:
            self.real_shows, self.threshold, self.c1, self.c2 = other
        self.finish()

    def initPlots(self):
        self.planWidget.setLegend('Plan', x_label='t', y_label='user count')
        self.probWidget.setLegend('Probability', x_label='w', y_label='p(w)')
        self.lossWidget.setLegend('Loss', x_label='betta', y_label='loss value')
        self.thresholdWidget.setLegend('Threshold y(t)', x_label='t', y_label='y(t)')
        self.errorWidget.setLegend('Error plot', x_label='t', y_label='|S(t) - x(t)|')

    def drawBasePlots(self):
        self.planWidget.plotData(utils.Tabulate(self.funcDict[constants.PLAN], (0, self.T, 0.01)),
                                        label='Plan S(t)',
                                        color='blue')

        self.planWidget.plotData(utils.Tabulate(self.funcDict[constants.TRAF], (0, self.T, 0.01)),
                                        label='Traffic z(t)',
                                        color='red')

        self.probWidget.plotData(utils.Tabulate(self.correctProb, (-0.1, 1.1, 0.01)),
                                        label='p(w)',
                                        color='orange')


    def drawWeightFuncs(self):
        self.planWidget.plotData(utils.Tabulate(self.real_shows, (0, self.T, 0.01)),
                                       label='x(t) real shows',
                                        color='green')
        self.errorWidget.plotData(utils.Tabulate(lambda t: abs(self.funcDict[constants.PLAN](t) - self.real_shows(t)) , (0, self.T, 0.01)),
                                        label='|S(t) - real_shows(t)|',
                                        color='green')
        self.thresholdWidget.plotData(utils.Tabulate(self.threshold, (0, self.T, 0.01)),
                                    label='threshold',
                                    color='blue')

        if self.auto:
            self.lossWidget.plotData(utils.Tabulate(self.lossFunc, (self.betta[0], self.betta[1], 0.01)),
                                        label=f'Loss(betta) = {self.c1Weight:.2f} * C1 + {self.c2Weight:.2f} * C2',
                                        color='orange')

    def finish(self):
        self.initPlots()
        self.drawWeightFuncs()
        self.update()
        self.saveS.setEnabled(True)
        self.saveP.setEnabled(True)
        self.saveZ.setEnabled(True)

        self.saveS.setFunc(self.funcDict[constants.PLAN])
        self.saveP.setFunc(self.funcDict[constants.PROB])
        self.saveZ.setFunc(self.funcDict[constants.TRAF])

        self.firstCrtField.setText(str(self.c1))
        self.secondCrtField.setText(str(self.c2))

        if self.auto:
            self.bettaField.setText(str(self.betta_opt))

    def _loadFuncs(self):
        self.log('Start files loading...')
        filesMap = self.filesMap
        for key in filesMap:
            filePath = filesMap[key]
            self.log(f'Try to load {key} file: {filePath}')

            func = None
            if filePath.endswith('.pickle'):
                grid = utils.loadPickle(filePath, 'rb')
                if grid is None:
                    self.error(f'Unable to load {key} function as pickle:\n{filePath}.')
                func = num_methods.interpolation.SplineInterpolation(grid)
            elif filePath.endswith('.json'):
                jsn = utils.loadJson(filePath, 'r')
                if jsn is None:
                    self.error(f'Unable to load {key} function interpolation as json:\n{filePath}.')
                func = num_methods.interpolation.SplineInterpolation(None).load_from_dict(jsn)
            else:
                grid = utils.loadCSV(filePath)
                if grid is None:
                    self.error(f'Unable to load {key} function as csv:\n{filePath}.')
                func = num_methods.interpolation.SplineInterpolation(grid)

            self.funcDict[key] = func
            self.log('Successful')
        self.log('All files loaded')

    def _dump(self, mode):
        dumpDir = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory'))

        for key in self.funcDict:
            utils.dumpFunc(self.funcDict[key], dumpDir, key, mode)

        utils.dumpFunc(self.uFunc, dumpDir, 'integral', mode)

    def error(self, message):
        logging.error(message)
        self.message = QtWidgets.QMessageBox.warning(self, 'Error', message)
        self.close()
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = InitialWindow(MainWindow)
    window.show()
    app.exec_()