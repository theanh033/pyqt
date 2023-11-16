import typing
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import sys
import MySQLdb as mdb
duongx = 1
class Login_w(QMainWindow):
    def __init__(self):
        super(Login_w,self).__init__()
        uic.loadUi('Login.ui',self)
        self.btn_Login.clicked.connect(self.login)
        self.btn_Register.clicked.connect(self.register_form)
    def register_form(self):
        widget.setCurrentIndex(1)

    def login(self, arg1):
        usernameLogin = self.edt_UserLogin.text()
        passwordLogin = self.edt_PasswordLogin.text()
        db=mdb.connect('localhost','root','','login_app')
        queryRole = db.cursor()
        query=db.cursor()
        query.execute("SELECT * FROM user_list Where Username= '"+ usernameLogin+"' and Password='"+ passwordLogin+"' ")
        queryRole.execute("SELECT Role From user_list Where Username= '"+ usernameLogin+"' ")
        kt = query.fetchone()
        kt1 = queryRole.fetchone()
        if kt:
                
                QMessageBox.information(self,"Thông Báo!","Login Success")
                for x in kt1:
                    self.thread = Home_w(index=x)
                widget.setCurrentIndex(2)
               
                
        else:
             QMessageBox.information(self,"Thông Báo!","Login Failed")
class Register_w(QMainWindow):
    def __init__(self):
        super(Register_w,self).__init__()
        uic.loadUi('Register.ui',self)
        self.btn_Register.clicked.connect(self.register)

   

        self.btn_BackRegister.clicked.connect(self.login_form)
    def login_form(self):
        widget.setCurrentIndex(0)




    def register(self):
        duong = "0"
        usernameRegister = self.edt_UsernameRegister.text()
        passwordRegister = self.edt_PasswordRegister.text()
        if self.rd_Admin.isChecked() == True:
           duong = "0"
        if self.rd_QTV.isChecked() == True:
           duong = "1"

        passwordRegisterAgain = self.edt_PasswordAgainRegister.text()
        db=mdb.connect('localhost','root','','login_app')
        query=db.cursor()
        query.execute("SELECT * FROM user_list Where Username= '"+ usernameRegister+"' and Password='"+ passwordRegister+"' ")
        kt = query.fetchone()
        if kt:
            QMessageBox.information(self,"Thông Báo!","Tài khoản đã tồn tại!")
        else:
             if passwordRegister != passwordRegisterAgain:
                 QMessageBox.information(self,"Thông Báo!","Mật khẩu không trùng khớp!")
                 self.edt_UsernameRegister.text == ""
             else:
                query.execute("INSERT INTO user_list VALUES ('"+usernameRegister+"','"+passwordRegister+"','"+duong+"') ")
                db.commit()
                QMessageBox.information(self,"Thông Báo!","Đăng ký thành công!")
                
                widget.setCurrentIndex(2)
                 
class Home_w(QMainWindow):
    def __init__(self, index=0):
        super(Home_w,self).__init__()
        uic.loadUi('Home.ui',self)
        self.a = index
        print("Role = ",self.a)
        if self.a == 1:
            self.btnUser.setEnabled(False)
        else:
            self.btnUser.setEnabled(True)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
Login_f = Login_w()
Register_f = Register_w()
Home_f = Home_w()
widget.addWidget(Login_f)
widget.addWidget(Register_f)
widget.addWidget(Home_f)
widget.setCurrentIndex(0)
widget.setFixedHeight(500)
widget.setFixedWidth(700) 
widget.show()
app.exec()

