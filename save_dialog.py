import os.path
import logging

from PyQt5 import QtWidgets, QtGui, QtCore

import constants
import utils
from ui.save_window import Ui_SaveDialog

class SaveDialog(QtWidgets.QMainWindow, Ui_SaveDialog):

    def __init__(self, function):
        super().__init__()
        self.setupUi(self)
        validator = QtGui.QDoubleValidator(self)
        locale = QtCore.QLocale("en")
        validator.setLocale(locale)
        self.fromField.setValidator(validator)
        self.toField.setValidator(validator)
        self.stepField.setValidator(validator)

        self.function = function
        self.okDialog.accepted.connect(self.openFile)
        self.saveInterpolation.clicked.connect(self.toggle)
        self.show()

    def openFile(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                'Choose file:',
                                                '',
                                                '''
                                                All files (*)
                                                ''', options=options)
        self.fileName = fileName
        self.dumpFunc()

    def toggle(self):
        flag = not self.saveInterpolation.isChecked()
        self.tabMode.setEnabled(flag)
        self.fromField.setEnabled(flag)
        self.toField.setEnabled(flag)
        self.stepField.setEnabled(flag)

    def dumpFunc(self):
        mode = constants.TABUL
        rng = None
        if self.saveInterpolation.isChecked():
            mode = constants.INTERPOL
        else:
            rng = (
                float(self.fromField.text()),
                float(self.toField.text()),
                float(self.stepField.text()),
            )
        try:
            utils.dumpFunc(self.function, self.fileName, mode=mode, rng=rng)
        except Exception as e:
            self.error('Dump error occured: ' + str(e))

        self.close()

    def error(self, message):
        logging.error(message)
        self.message = QtWidgets.QMessageBox.warning(self, "Error", message)
        self.close()