# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ioscan.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(241, 161)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chkX4 = QtWidgets.QCheckBox(self.groupBox)
        self.chkX4.setObjectName("chkX4")
        self.horizontalLayout.addWidget(self.chkX4)
        self.chkX3 = QtWidgets.QCheckBox(self.groupBox)
        self.chkX3.setObjectName("chkX3")
        self.horizontalLayout.addWidget(self.chkX3)
        self.chkX2 = QtWidgets.QCheckBox(self.groupBox)
        self.chkX2.setObjectName("chkX2")
        self.horizontalLayout.addWidget(self.chkX2)
        self.chkX1 = QtWidgets.QCheckBox(self.groupBox)
        self.chkX1.setObjectName("chkX1")
        self.horizontalLayout.addWidget(self.chkX1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radY2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radY2.setAutoExclusive(False)
        self.radY2.setObjectName("radY2")
        self.horizontalLayout_2.addWidget(self.radY2)
        self.radY1 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radY1.setAutoExclusive(False)
        self.radY1.setObjectName("radY1")
        self.horizontalLayout_2.addWidget(self.radY1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "IoScan"))
        self.groupBox.setTitle(_translate("Dialog", "X"))
        self.chkX4.setText(_translate("Dialog", "X4"))
        self.chkX3.setText(_translate("Dialog", "X3"))
        self.chkX2.setText(_translate("Dialog", "X2"))
        self.chkX1.setText(_translate("Dialog", "X1"))
        self.groupBox_2.setTitle(_translate("Dialog", "Y"))
        self.radY2.setText(_translate("Dialog", "Y2"))
        self.radY1.setText(_translate("Dialog", "Y1"))

