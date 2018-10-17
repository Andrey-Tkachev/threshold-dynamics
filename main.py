import sys

from PyQt5 import QtWidgets

import numpy as np
import json
import math

import constants
from ui.main_window import Ui_MainWindow
from initial_window import InitialWindow

class ParamFunc(object):

    def __init__(self, paramsDict):
        self.params = paramsDict

    def tabulate(self, beg, end):
        results = []
        for x in range(beg, end):
            results = self(x)

class

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, filesMap, auto=None, x=None, y=None):
        super().__init__()
        self.setupUi(self)
        self.planFunc = None
        self.probFunc = None
        self.planWidget.setLegend('Plan', x_label='t', y_label='users')
        self.planWidget.plotData(np.random.rand(10), label='S(t)', color='blue')
        self.planWidget.plotData(np.random.rand(10), label='X(t)', color='orange')
        self.show()

    def loadParams(self, filesMap):
        settings = json.load(filesMap[constants.SETTINGS])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = InitialWindow(MainWindow)
    window.show()
    app.exec_()