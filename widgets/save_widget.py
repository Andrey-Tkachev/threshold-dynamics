from PyQt5 import QtWidgets

from save_dialog import SaveDialog

class SaveWidget(QtWidgets.QPushButton):

    def __init__(self, parent):
        super().__init__(parent)
        self.clicked.connect(self.save)
        self.func = None

    def setFunc(self, func):
        self.func = func

    def save(self):
        self.dialog = SaveDialog(self.func)