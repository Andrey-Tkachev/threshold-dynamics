# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_raw/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 880)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(720, 600))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.controlLayout = QtWidgets.QHBoxLayout()
        self.controlLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.controlLayout.setObjectName("controlLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.planWidget = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.planWidget.sizePolicy().hasHeightForWidth())
        self.planWidget.setSizePolicy(sizePolicy)
        self.planWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.planWidget.setObjectName("planWidget")
        self.verticalLayout_2.addWidget(self.planWidget)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.thresholdWidget = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdWidget.sizePolicy().hasHeightForWidth())
        self.thresholdWidget.setSizePolicy(sizePolicy)
        self.thresholdWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.thresholdWidget.setObjectName("thresholdWidget")
        self.gridLayout_2.addWidget(self.thresholdWidget, 1, 0, 1, 1)
        self.errorWidget = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorWidget.sizePolicy().hasHeightForWidth())
        self.errorWidget.setSizePolicy(sizePolicy)
        self.errorWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.errorWidget.setObjectName("errorWidget")
        self.gridLayout_2.addWidget(self.errorWidget, 0, 0, 1, 1)
        self.lossWidget = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lossWidget.sizePolicy().hasHeightForWidth())
        self.lossWidget.setSizePolicy(sizePolicy)
        self.lossWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.lossWidget.setObjectName("lossWidget")
        self.gridLayout_2.addWidget(self.lossWidget, 0, 1, 1, 1)
        self.probWidget = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probWidget.sizePolicy().hasHeightForWidth())
        self.probWidget.setSizePolicy(sizePolicy)
        self.probWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.probWidget.setObjectName("probWidget")
        self.gridLayout_2.addWidget(self.probWidget, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.bettaField = QtWidgets.QLineEdit(self.centralwidget)
        self.bettaField.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bettaField.sizePolicy().hasHeightForWidth())
        self.bettaField.setSizePolicy(sizePolicy)
        self.bettaField.setMinimumSize(QtCore.QSize(200, 0))
        self.bettaField.setAutoFillBackground(True)
        self.bettaField.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bettaField.setReadOnly(True)
        self.bettaField.setObjectName("bettaField")
        self.horizontalLayout_4.addWidget(self.bettaField)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.firstCrtField = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstCrtField.sizePolicy().hasHeightForWidth())
        self.firstCrtField.setSizePolicy(sizePolicy)
        self.firstCrtField.setMinimumSize(QtCore.QSize(200, 0))
        self.firstCrtField.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.firstCrtField.setReadOnly(True)
        self.firstCrtField.setObjectName("firstCrtField")
        self.horizontalLayout.addWidget(self.firstCrtField)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.secondCrtField = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondCrtField.sizePolicy().hasHeightForWidth())
        self.secondCrtField.setSizePolicy(sizePolicy)
        self.secondCrtField.setMinimumSize(QtCore.QSize(200, 0))
        self.secondCrtField.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.secondCrtField.setReadOnly(True)
        self.secondCrtField.setObjectName("secondCrtField")
        self.horizontalLayout_2.addWidget(self.secondCrtField)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.bettaEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.bettaEdit.setText("")
        self.bettaEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bettaEdit.setObjectName("bettaEdit")
        self.horizontalLayout_6.addWidget(self.bettaEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.c2WeightEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.c2WeightEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.c2WeightEdit.setObjectName("c2WeightEdit")
        self.horizontalLayout_7.addWidget(self.c2WeightEdit)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.c1WeightEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.c1WeightEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.c1WeightEdit.setObjectName("c1WeightEdit")
        self.horizontalLayout_7.addWidget(self.c1WeightEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.logTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTextEdit.sizePolicy().hasHeightForWidth())
        self.logTextEdit.setSizePolicy(sizePolicy)
        self.logTextEdit.setAcceptDrops(False)
        self.logTextEdit.setStyleSheet("")
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setCenterOnScroll(True)
        self.logTextEdit.setObjectName("logTextEdit")
        self.horizontalLayout_5.addWidget(self.logTextEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_3.addWidget(self.startBtn)
        self.saveS = SaveWidget(self.centralwidget)
        self.saveS.setObjectName("saveS")
        self.horizontalLayout_3.addWidget(self.saveS)
        self.saveP = SaveWidget(self.centralwidget)
        self.saveP.setObjectName("saveP")
        self.horizontalLayout_3.addWidget(self.saveP)
        self.saveZ = SaveWidget(self.centralwidget)
        self.saveZ.setObjectName("saveZ")
        self.horizontalLayout_3.addWidget(self.saveZ)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.controlLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.controlLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Betta*:"))
        self.label.setText(_translate("MainWindow", "Criteria 1:"))
        self.label_2.setText(_translate("MainWindow", "Criteria 2:"))
        self.label_4.setText(_translate("MainWindow", "Выбирите betta:"))
        self.label_6.setText(_translate("MainWindow", "Вес C1"))
        self.c2WeightEdit.setText(_translate("MainWindow", "0.9"))
        self.label_5.setText(_translate("MainWindow", "Вес C2"))
        self.c1WeightEdit.setText(_translate("MainWindow", "0.1"))
        self.startBtn.setText(_translate("MainWindow", "Решить"))
        self.saveS.setText(_translate("MainWindow", "Сохранить S(t)"))
        self.saveP.setText(_translate("MainWindow", "Сохранить p(w)"))
        self.saveZ.setText(_translate("MainWindow", "Сохранить z(t)"))

from widgets.plot_widget import PlotWidget
from widgets.save_widget import SaveWidget
