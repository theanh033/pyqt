# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Register.setGeometry(QtCore.QRect(410, 370, 161, 41))
        self.btn_Register.setObjectName("btn_Register")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 170, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 220, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 260, 101, 21))
        self.label_3.setObjectName("label_3")
        self.rd_Admin = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_Admin.setGeometry(QtCore.QRect(340, 310, 95, 20))
        self.rd_Admin.setObjectName("rd_Admin")
        self.rd_QTV = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_QTV.setGeometry(QtCore.QRect(450, 310, 95, 20))
        self.rd_QTV.setObjectName("rd_QTV")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 310, 101, 21))
        self.label_4.setObjectName("label_4")
        self.btn_BackRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btn_BackRegister.setGeometry(QtCore.QRect(220, 370, 151, 41))
        self.btn_BackRegister.setObjectName("btn_BackRegister")
        self.edt_UsernameRegister = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_UsernameRegister.setGeometry(QtCore.QRect(340, 180, 231, 22))
        self.edt_UsernameRegister.setObjectName("edt_UsernameRegister")
        self.edt_PasswordRegister = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_PasswordRegister.setGeometry(QtCore.QRect(340, 220, 231, 22))
        self.edt_PasswordRegister.setObjectName("edt_PasswordRegister")
        self.edt_PasswordAgainRegister = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_PasswordAgainRegister.setGeometry(QtCore.QRect(340, 260, 231, 22))
        self.edt_PasswordAgainRegister.setObjectName("edt_PasswordAgainRegister")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 70, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_Register.setText(_translate("MainWindow", "Register"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Password again"))
        self.rd_Admin.setText(_translate("MainWindow", "Admin"))
        self.rd_QTV.setText(_translate("MainWindow", "QTV"))
        self.label_4.setText(_translate("MainWindow", "Role"))
        self.btn_BackRegister.setText(_translate("MainWindow", "Back"))
        self.label_5.setText(_translate("MainWindow", "REGISTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())