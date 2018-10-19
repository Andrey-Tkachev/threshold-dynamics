import os.path

from PyQt5 import QtWidgets
from functools import partial

from ui.initial_window import Ui_InitialWindow

import constants
import utils

class InitialWindow(QtWidgets.QMainWindow, Ui_InitialWindow):

    def __init__(self, nextClass):
        super().__init__()
        self.nextClass = nextClass
        self.setupUi(self)

        self.files = {
            constants.PLAN: None,
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

        self.bettaInitialField.textChanged.connect(partial(self.validate,
                                                        self.bettaInitialField))
        self.xInitialField.textChanged.connect(partial(self.validate,
                                                self.xInitialField))
        self.yInitialField.textChanged.connect(partial(self.validate,
                                                self.yInitialField))
        self.tInitialField.textChanged.connect(partial(self.validate,
                                                self.tInitialField))

        self.autoModeCheckBox.clicked.connect(self.toggleInput)

    def validate(self, obj):
        text = obj.toPlainText()
        if not text:
            return

        if not utils.IsReal(text):
            obj.setPlainText(text[:-1])

    def toggleInput(self):
        notChecked = not self.autoModeCheckBox.isChecked()
        self.bettaInitialField.setEnabled(notChecked)
        self.xInitialField.setEnabled(notChecked)
        self.yInitialField.setEnabled(notChecked)

    def openFileNameDialog(self, fileKey):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.files[fileKey], _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                'Load function:',
                                                '',
                                                '''
                                                Pickle (*.pickle);;
                                                CSV files (*.csv);;
                                                ''', options=options)
        self.updateField(fileKey)

    def updateField(self, fileKey):
        text = self.files[fileKey]
        if text is not None:
            self.fileKey2textField[fileKey].setText(text)
        for key in self.fileKey2textField:
            if key not in self.files or not os.path.isfile(self.files[key]):
                return
        self.okDialog.setEnabled(True)

    def goNext(self):
        autoMode = self.autoModeCheckBox.isChecked()
        self.nextWindow = self.nextClass(self.files, auto=autoMode,
                                            betta=self.bettaInitialField.toPlainText(),
                                            x=self.xInitialField.toPlainText(),
                                            y=self.yInitialField.toPlainText(),
                                            t=self.tInitialField.toPlainText())
        self.close()