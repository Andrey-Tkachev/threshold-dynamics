# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_raw/initial_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InitialWindow(object):
    def setupUi(self, InitialWindow):
        InitialWindow.setObjectName("InitialWindow")
        InitialWindow.setWindowModality(QtCore.Qt.WindowModal)
        InitialWindow.resize(582, 235)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InitialWindow.sizePolicy().hasHeightForWidth())
        InitialWindow.setSizePolicy(sizePolicy)
        InitialWindow.setMinimumSize(QtCore.QSize(500, 210))
        InitialWindow.setMaximumSize(QtCore.QSize(864, 16666))
        font = QtGui.QFont()
        font.setFamily("Serif")
        InitialWindow.setFont(font)
        InitialWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        InitialWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(InitialWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 150))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 115151))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.funcsInitialLayout = QtWidgets.QVBoxLayout()
        self.funcsInitialLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.funcsInitialLayout.setSpacing(6)
        self.funcsInitialLayout.setObjectName("funcsInitialLayout")
        self.funcName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcName.sizePolicy().hasHeightForWidth())
        self.funcName.setSizePolicy(sizePolicy)
        self.funcName.setMaximumSize(QtCore.QSize(16777215, 50))
        self.funcName.setObjectName("funcName")
        self.funcsInitialLayout.addWidget(self.funcName)
        self.openFileLayout = QtWidgets.QHBoxLayout()
        self.openFileLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.openFileLayout.setObjectName("openFileLayout")
        self.displayFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.displayFileName.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayFileName.sizePolicy().hasHeightForWidth())
        self.displayFileName.setSizePolicy(sizePolicy)
        self.displayFileName.setMinimumSize(QtCore.QSize(0, 30))
        self.displayFileName.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.displayFileName.setMouseTracking(False)
        self.displayFileName.setReadOnly(True)
        self.displayFileName.setObjectName("displayFileName")
        self.openFileLayout.addWidget(self.displayFileName)
        self.openFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton.setMinimumSize(QtCore.QSize(0, 30))
        self.openFileButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.openFileButton.setBaseSize(QtCore.QSize(0, 0))
        self.openFileButton.setObjectName("openFileButton")
        self.openFileLayout.addWidget(self.openFileButton)
        self.funcsInitialLayout.addLayout(self.openFileLayout)
        self.verticalLayout.addLayout(self.funcsInitialLayout)
        self.autoModeCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoModeCheckBox.sizePolicy().hasHeightForWidth())
        self.autoModeCheckBox.setSizePolicy(sizePolicy)
        self.autoModeCheckBox.setObjectName("autoModeCheckBox")
        self.verticalLayout.addWidget(self.autoModeCheckBox)
        self.handModeHorLayout = QtWidgets.QHBoxLayout()
        self.handModeHorLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.handModeHorLayout.setContentsMargins(-1, -1, -1, 0)
        self.handModeHorLayout.setSpacing(5)
        self.handModeHorLayout.setObjectName("handModeHorLayout")
        self.bettaInitialLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bettaInitialLabel.sizePolicy().hasHeightForWidth())
        self.bettaInitialLabel.setSizePolicy(sizePolicy)
        self.bettaInitialLabel.setObjectName("bettaInitialLabel")
        self.handModeHorLayout.addWidget(self.bettaInitialLabel)
        self.bettaInitialField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.bettaInitialField.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bettaInitialField.sizePolicy().hasHeightForWidth())
        self.bettaInitialField.setSizePolicy(sizePolicy)
        self.bettaInitialField.setMaximumSize(QtCore.QSize(15005, 40))
        self.bettaInitialField.setObjectName("bettaInitialField")
        self.handModeHorLayout.addWidget(self.bettaInitialField)
        self.xInitialLabel = QtWidgets.QLabel(self.centralwidget)
        self.xInitialLabel.setObjectName("xInitialLabel")
        self.handModeHorLayout.addWidget(self.xInitialLabel)
        self.xInitialField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.xInitialField.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xInitialField.sizePolicy().hasHeightForWidth())
        self.xInitialField.setSizePolicy(sizePolicy)
        self.xInitialField.setMaximumSize(QtCore.QSize(16777215, 40))
        self.xInitialField.setObjectName("xInitialField")
        self.handModeHorLayout.addWidget(self.xInitialField)
        self.yInitialLabel = QtWidgets.QLabel(self.centralwidget)
        self.yInitialLabel.setObjectName("yInitialLabel")
        self.handModeHorLayout.addWidget(self.yInitialLabel)
        self.yInitialField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.yInitialField.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yInitialField.sizePolicy().hasHeightForWidth())
        self.yInitialField.setSizePolicy(sizePolicy)
        self.yInitialField.setMaximumSize(QtCore.QSize(16777215, 40))
        self.yInitialField.setObjectName("yInitialField")
        self.handModeHorLayout.addWidget(self.yInitialField)
        self.verticalLayout.addLayout(self.handModeHorLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.okDialog = QtWidgets.QDialogButtonBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okDialog.sizePolicy().hasHeightForWidth())
        self.okDialog.setSizePolicy(sizePolicy)
        self.okDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.okDialog.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okDialog.setCenterButtons(False)
        self.okDialog.setObjectName("okDialog")
        self.verticalLayout.addWidget(self.okDialog)
        InitialWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InitialWindow)
        QtCore.QMetaObject.connectSlotsByName(InitialWindow)

    def retranslateUi(self, InitialWindow):
        _translate = QtCore.QCoreApplication.translate
        InitialWindow.setWindowTitle(_translate("InitialWindow", "Thresholds initial"))
        self.funcName.setText(_translate("InitialWindow", "S(t)"))
        self.openFileButton.setText(_translate("InitialWindow", "open file"))
        self.autoModeCheckBox.setText(_translate("InitialWindow", "Auto mode"))
        self.bettaInitialLabel.setText(_translate("InitialWindow", "b"))
        self.xInitialLabel.setText(_translate("InitialWindow", "X0"))
        self.yInitialLabel.setText(_translate("InitialWindow", "Y0"))

