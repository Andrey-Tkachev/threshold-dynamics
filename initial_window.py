import os.path

from PyQt5 import QtWidgets, QtCore, QtGui
from functools import partial

from ui.initial_window import Ui_InitialWindow

import constants
import utils

class InitialWindow(QtWidgets.QMainWindow, Ui_InitialWindow):

    def __init__(self, nextClass):
        super().__init__()
        self.nextClass = nextClass
        self.setupUi(self)

        validator = QtGui.QDoubleValidator(self)
        locale = QtCore.QLocale("en")
        validator.setLocale(locale)

        self.files = {
            constants.PROB: None,
        }

        self.fileKey2textField = {
            constants.PLAN: self.displayPlanFile,
            constants.PROB: self.displayProbFile,
            constants.TRAF: self.displayTrafficFile,
        }

        self.okDialog.accepted.connect(self.goNext)
        self.okDialog.rejected.connect(self.close)
        self.openPlanFile.clicked.connect(partial(self.openFileNameDialog,
                                                    fileKey=constants.PLAN))
        self.openProbFile.clicked.connect(partial(self.openFileNameDialog,
                                                    fileKey=constants.PROB))
        self.openTrafFile.clicked.connect(partial(self.openFileNameDialog,
                                                    fileKey=constants.TRAF))

        self.bettaInitialField.setValidator(validator)
        self.betta0InitialField.setValidator(validator)
        self.betta1InitialField.setValidator(validator)
        self.xInitialField.setValidator(validator)
        self.yInitialField.setValidator(validator)
        self.tInitialField.setValidator(validator)

        self.autoModeCheckBox.clicked.connect(self.toggleInput)

    def toggleInput(self):
        notChecked = not self.autoModeCheckBox.isChecked()
        self.bettaInitialField.setEnabled(notChecked)
        self.xInitialField.setEnabled(notChecked)
        self.betta0InitialField.setEnabled(not notChecked)
        self.betta1InitialField.setEnabled(not notChecked)

    def openFileNameDialog(self, fileKey):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.files[fileKey], _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                'Load function:',
                                                '',
                                                '''
                                                Json (*.json);;
                                                Pickle (*.pickle);;
                                                CSV files (*.csv);;
                                                ''', options=options)
        self.updateField(fileKey)

    def updateField(self, fileKey):
        text = self.files[fileKey]
        if text is not None:
            self.fileKey2textField[fileKey].setText(text)
        for key in self.fileKey2textField:
            if (key not in self.files
                            or self.files[key] is None
                            or not os.path.isfile(self.files[key])):
                return
        self.okDialog.setEnabled(True)

    def goNext(self):
        autoMode = self.autoModeCheckBox.isChecked()
        self.nextWindow = self.nextClass(self.files, auto=autoMode,
                                            betta=float(self.bettaInitialField.text()),
                                            betta0=float(self.betta0InitialField.text()),
                                            betta1=float(self.betta1InitialField.text()),
                                            x=float(self.xInitialField.text()),
                                            y=float(self.yInitialField.text()),
                                            T=float(self.tInitialField.text()))
        self.close()