from PyQt5 import QtWidgets
from functools import partial

from ui.initial_window import Ui_InitialWindow

import constants

class InitialWindow(QtWidgets.QMainWindow, Ui_InitialWindow):

    def __init__(self, nextClass):
        super().__init__()
        self.nextClass = nextClass
        self.setupUi(self)

        self.files = {
            constants.SETTINGS: None,
        }

        self.fileKey2textField = {
            constants.SETTINGS: self.displayFileName,
        }

        self.okDialog.accepted.connect(self.goNext)
        self.okDialog.rejected.connect(self.close)
        self.openFileButton.clicked.connect(partial(self.openFileNameDialog,
                                                    fileKey=constants.SETTINGS))

        self.autoModeCheckBox.clicked.connect(self.toggleInput)

    def toggleInput(self):
        notChecked = not self.autoModeCheckBox.isChecked()
        self.bettaInitialField.setEnabled(notChecked)
        self.xInitialField.setEnabled(notChecked)
        self.yInitialField.setEnabled(notChecked)

    def openFileNameDialog(self, fileKey):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.files[fileKey], _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                'Load function json',
                                                '',
                                                'All Files (*);;JONS files (*.json)', options=options)
        self.updateField(fileKey)

    def updateField(self, fileKey):
        text = self.files[fileKey]
        if text is not None:
            self.fileKey2textField[fileKey].setText(text)

    def goNext(self):
        autoMode = self.autoModeCheckBox.isChecked()
        self.nextWindow = self.nextClass(self.files, auto=autoMode,
                                            betta=self.bettaInitialField.toPlainText(),
                                            x=self.xInitialField.toPlainText(),
                                            y=self.yInitialField.toPlainText())
        self.close()