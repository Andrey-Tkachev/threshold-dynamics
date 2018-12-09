# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_raw/save_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SaveDialog(object):
    def setupUi(self, SaveDialog):
        SaveDialog.setObjectName("SaveDialog")
        SaveDialog.resize(366, 169)
        self.centralwidget = QtWidgets.QWidget(SaveDialog)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.tabMode = QtWidgets.QComboBox(self.centralwidget)
        self.tabMode.setObjectName("tabMode")
        self.tabMode.addItem("")
        self.horizontalLayout_2.addWidget(self.tabMode)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.fromField = QtWidgets.QLineEdit(self.centralwidget)
        self.fromField.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.fromField.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fromField.setObjectName("fromField")
        self.horizontalLayout_3.addWidget(self.fromField)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.toField = QtWidgets.QLineEdit(self.centralwidget)
        self.toField.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.toField.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.toField.setObjectName("toField")
        self.horizontalLayout_3.addWidget(self.toField)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.stepField = QtWidgets.QLineEdit(self.centralwidget)
        self.stepField.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.stepField.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stepField.setObjectName("stepField")
        self.horizontalLayout_3.addWidget(self.stepField)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.saveInterpolation = QtWidgets.QRadioButton(self.centralwidget)
        self.saveInterpolation.setObjectName("saveInterpolation")
        self.verticalLayout.addWidget(self.saveInterpolation)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.okDialog = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.okDialog.setEnabled(True)
        self.okDialog.setOrientation(QtCore.Qt.Horizontal)
        self.okDialog.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.okDialog.setObjectName("okDialog")
        self.verticalLayout.addWidget(self.okDialog)
        SaveDialog.setCentralWidget(self.centralwidget)

        self.retranslateUi(SaveDialog)
        QtCore.QMetaObject.connectSlotsByName(SaveDialog)

    def retranslateUi(self, SaveDialog):
        _translate = QtCore.QCoreApplication.translate
        SaveDialog.setWindowTitle(_translate("SaveDialog", "MainWindow"))
        self.label.setText(_translate("SaveDialog", "Тип сетки:"))
        self.tabMode.setItemText(0, _translate("SaveDialog", " равномерная"))
        self.label_2.setText(_translate("SaveDialog", "От:"))
        self.fromField.setText(_translate("SaveDialog", "0.0"))
        self.label_3.setText(_translate("SaveDialog", "До:"))
        self.toField.setText(_translate("SaveDialog", "10.0"))
        self.label_4.setText(_translate("SaveDialog", "Шаг:"))
        self.stepField.setText(_translate("SaveDialog", "1.0"))
        self.saveInterpolation.setText(_translate("SaveDialog", "Сохранить как интерполяцию"))

