# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormMain(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 40, 191, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Plants = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Plants.setObjectName("Plants")
        self.verticalLayout.addWidget(self.Plants)
        self.Members = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Members.setObjectName("Members")
        self.verticalLayout.addWidget(self.Members)
        self.Actual_data = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Actual_data.setObjectName("Actual_data")
        self.verticalLayout.addWidget(self.Actual_data)
        self.Products = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Products.setObjectName("Products")
        self.verticalLayout.addWidget(self.Products)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Plants.setText(_translate("Form", "Plants"))
        self.Members.setText(_translate("Form", "Members"))
        self.Actual_data.setText(_translate("Form", "Actual_data"))
        self.Products.setText(_translate("Form", "Products"))