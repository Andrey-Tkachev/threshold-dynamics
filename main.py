import sys

from PyQt5 import QtWidgets

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


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, filesMap, auto=None, betta=None, x=None, y=None, t=None):
        super().__init__()

        self.setupUi(self)
        self.initButtons()

        self.filesMap = filesMap
        self.firstCrtField.setEnabled(not auto)
        self.secondCrtField.setEnabled(not auto)
        self.bettaField.setEnabled(auto)

        self.funcDict = {
            constants.PLAN: None,
            constants.PROB: None,
            constants.TRAF: None,
        }
        self.uFunc = None
        self.initFuncs()
        self.initPlots()
        if auto:
            x = None
            y = None
            betta = None

        self.solver = num_methods.solver.Solver(x, y, betta, t, u=self.uFunc,
                                                    s=self.funcDict[constants.PLAN],
                                                    z=self.funcDict[constants.TRAF])

        if not auto:
            self.firstCrtField.setText(str(self.solver.getC1()))
            self.secondCrtField.setText(str(self.solver.getC2()))
        else:
            self.bettaField.setText(str(self.solver.getBetta()))

        self.show()

    def initButtons(self):
        self.saveInterpolation.clicked.connect(partial(self._dump, constants.INTERPOL))
        self.saveTabulation.clicked.connect(partial(self._dump, constants.TABUL))

    def initFuncs(self):
        self._loadFuncs()
        integral = num_methods.integral.Integral(self.funcDict[constants.PROB])
        self.uFunc = num_methods.interpolation.Interpolation(utils.Tabulate(integral, (0, 10)))

    def initPlots(self):
        self.planWidget.setLegend('Plan', x_label='t', y_label='users')
        self.probWidget.setLegend('Probability', x_label='w', y_label='p(w)')
        self.uWidget.setLegend('p(w) integral', x_label='y', y_label='U(y)')

        self.planWidget.plotData(utils.Tabulate(self.funcDict[constants.PLAN], (0, 10)),
                                        label='S(t)',
                                        color='blue')

        self.planWidget.plotData(utils.Tabulate(self.funcDict[constants.TRAF], (0, 10)),
                                        label='z(t)',
                                        color='red')

        self.probWidget.plotData(utils.Tabulate(self.funcDict[constants.PROB], (0, 10)),
                                        label='p(w)',
                                        color='orange')

        self.uWidget.plotData(utils.Tabulate(self.uFunc, (0, 10)),
                                        label='U(y)',
                                        color='green')

        self.probWidget.plotData(utils.Tabulate(self.funcDict[constants.PROB], (0, 10)),
                                        label='p(w)',
                                        color='orange')

    def _loadFuncs(self):
        filesMap = self.filesMap
        for key in filesMap:
            filePath = filesMap[key]
            logging.debug(f'Try to load {key} file: {filePath}.')
            points = utils.loadCSV(filePath)
            if points is None:
                self.error(f'Something gone wrong with {filePath}')

            self.funcDict[key] = num_methods.interpolation.Interpolation(points)

    def _dump(self, mode):
        dumpDir = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))

        for key in self.funcDict:
            utils.dumpFunc(self.funcDict[key], dumpDir, key, mode)

        utils.dumpFunc(self.uFunc, dumpDir, 'integral', mode)

    def error(self, message):
        logging.error(message)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = InitialWindow(MainWindow)
    window.show()
    app.exec_()