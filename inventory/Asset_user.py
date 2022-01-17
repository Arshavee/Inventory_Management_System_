# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Asset_userUHxnNa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
from ui_Application import Ui_MainWindow

atv_status = ["Active", "Inactive"]
class Ui_MainWindow_user(object):
    def openWindow(self):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            MainWindow.hide()

    def userid(self):

        connection = sqlite3.connect("appuser_db.db")
        crsr = connection.cursor()
        sql_command = '''SELECT astusr_id FROM asset_user ORDER BY ROWID DESC LIMIT 1;'''
        crsr.execute(sql_command)
        # connection.commit()
        par = crsr.fetchall()
        print(par)
        a = str(par)

        par = (a[9:-3])
        print(par)
        if par == " ":
            astusr_id = "1"
        else:
            astusr_id = str(int(par) + 1)
        astusr_cont_id = str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + str(astusr_id).zfill(
            5 - len(astusr_id))
        print(astusr_cont_id)
        self.a_userid_input.setText(astusr_cont_id)

        connection.close()


    def submit(self):
        aa=self.a_userid_input.text()
        a= self.lineEdit_u_email.text()
        b=self.lineEdit_u_cont_no.text()
        c=self.lineEdit_u_name.text()
        d=self.lineEdit_u_assetid.text()
        e=self.lineEdit_u_sitloc.text()
        f=self.lineEdit_u_dept.text()
        g=self.lineEdit_u_desig.text()
        h=self.dateEdit_u_create_date.text()
        i=self.lineEdit_other_detail.text()
        j=self.comboBox_u_activestatus.currentText()
        params=( aa,a,b,c,d,e,f,g,h,i,j  )

        connection = sqlite3.connect("appuser_db.db")

        crsr = connection.cursor()
        sql_command = '''INSERT into asset_user (astusr_id,astusr_email,astusr_contno,astusr_user_name,astusr_astid,
        astusr_user_sitting_location,astusr_user_dept,astusr_user_dsig,astusr_ast_user_create_date,astusr_other_details
        ,astusr_active_status) VALUES (?,?,?,?,?,?,?,?,?,?,?);'''
        crsr.execute(sql_command, params)
        connection.commit()
        print("commited successfully")
        connection.close()
        self.a_userid_input.setText(" ")
        self.lineEdit_u_email.setText(" ")
        self.lineEdit_u_cont_no.setText(" ")
        self.lineEdit_u_name.setText(" ")
        self.lineEdit_u_assetid.setText(" ")
        self.lineEdit_u_sitloc.setText(" ")
        self.lineEdit_u_dept.setText(" ")
        self.lineEdit_u_desig.setText(" ")
        self.dateEdit_u_create_date.clear()
        self.lineEdit_other_detail.setText(" ")
        self.comboBox_u_activestatus.clear()
        self.userid()
    def setupUi(self, MainWindow):
        global atv_status

        connection = sqlite3.connect("appuser_db.db")
        crsr = connection.cursor()
        sql_command = '''SELECT astusr_id FROM asset_user ORDER BY ROWID DESC LIMIT 1;'''
        crsr.execute(sql_command)
        # connection.commit()
        params = crsr.fetchall()
        a = str(params)
        par = (a[1:-1])
        print(par)
        print(type(par))
        connection.close()
        if (par != ' '):
            c = 1
        else:
            a = int(par)
            c = a + 1
        print(c)
        print(type(c))
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 570)
        MainWindow.setMinimumSize(QSize(550, 570))
        MainWindow.setMaximumSize(QSize(550, 570))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 20, 491, 531))
        self.label_u_cont_no = QLabel(self.widget)
        self.label_u_cont_no.setObjectName(u"label_u_cont_no")
        self.label_u_cont_no.setGeometry(QRect(20, 170, 111, 16))
        self.label_u_name = QLabel(self.widget)
        self.label_u_name.setObjectName(u"label_u_name")
        self.label_u_name.setGeometry(QRect(20, 210, 121, 16))
        self.label_u_assetid = QLabel(self.widget)
        self.label_u_assetid.setObjectName(u"label_u_assetid")
        self.label_u_assetid.setGeometry(QRect(20, 250, 121, 16))
        self.label_u_dept = QLabel(self.widget)
        self.label_u_dept.setObjectName(u"label_u_dept")
        self.label_u_dept.setGeometry(QRect(20, 320, 121, 16))
        self.label_u_sitloc = QLabel(self.widget)
        self.label_u_sitloc.setObjectName(u"label_u_sitloc")
        self.label_u_sitloc.setGeometry(QRect(20, 280, 121, 16))
        self.label_u_desig = QLabel(self.widget)
        self.label_u_desig.setObjectName(u"label_u_desig")
        self.label_u_desig.setGeometry(QRect(20, 350, 121, 16))
        self.label_u_creat_date = QLabel(self.widget)
        self.label_u_creat_date.setObjectName(u"label_u_creat_date")
        self.label_u_creat_date.setGeometry(QRect(20, 390, 121, 16))
        self.label_other_detail = QLabel(self.widget)
        self.label_other_detail.setObjectName(u"label_other_detail")
        self.label_other_detail.setGeometry(QRect(20, 420, 121, 16))
        self.label_u_activestatus = QLabel(self.widget)
        self.label_u_activestatus.setObjectName(u"label_u_activestatus")
        self.label_u_activestatus.setGeometry(QRect(20, 450, 121, 16))
        self.a_userid = QLabel(self.widget)
        self.a_userid.setObjectName(u"a_userid")
        self.a_userid.setGeometry(QRect(20, 110, 121, 16))
        self.u_email = QLabel(self.widget)
        self.u_email.setObjectName(u"u_email")
        self.u_email.setGeometry(QRect(20, 140, 121, 20))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 40, 261, 61))
        self.a_userid_input = QLabel(self.widget)
        self.a_userid_input.setObjectName(u"a_userid_input")
        self.a_userid_input.setGeometry(QRect(260, 106, 101, 20))
        self.lineEdit_u_email = QLineEdit(self.widget)
        self.lineEdit_u_email.setObjectName(u"lineEdit_u_email")
        self.lineEdit_u_email.setGeometry(QRect(240, 140, 161, 20))
        self.lineEdit_u_cont_no = QLineEdit(self.widget)
        self.lineEdit_u_cont_no.setObjectName(u"lineEdit_u_cont_no")
        self.lineEdit_u_cont_no.setGeometry(QRect(240, 170, 161, 20))
        self.lineEdit_u_assetid = QLineEdit(self.widget)
        self.lineEdit_u_assetid.setObjectName(u"lineEdit_u_assetid")
        self.lineEdit_u_assetid.setGeometry(QRect(240, 250, 161, 20))
        self.lineEdit_u_name = QLineEdit(self.widget)
        self.lineEdit_u_name.setObjectName(u"lineEdit_u_name")
        self.lineEdit_u_name.setGeometry(QRect(240, 210, 161, 20))
        self.lineEdit_u_sitloc = QLineEdit(self.widget)
        self.lineEdit_u_sitloc.setObjectName(u"lineEdit_u_sitloc")
        self.lineEdit_u_sitloc.setGeometry(QRect(240, 280, 161, 20))
        self.lineEdit_u_dept = QLineEdit(self.widget)
        self.lineEdit_u_dept.setObjectName(u"lineEdit_u_dept")
        self.lineEdit_u_dept.setGeometry(QRect(240, 320, 161, 20))
        self.lineEdit_u_desig = QLineEdit(self.widget)
        self.lineEdit_u_desig.setObjectName(u"lineEdit_u_desig")
        self.lineEdit_u_desig.setGeometry(QRect(240, 350, 161, 20))
        self.lineEdit_other_detail = QLineEdit(self.widget)
        self.lineEdit_other_detail.setObjectName(u"lineEdit_other_detail")
        self.lineEdit_other_detail.setGeometry(QRect(240, 420, 161, 20))
        self.comboBox_u_activestatus = QComboBox(self.widget)
        self.comboBox_u_activestatus.setObjectName(u"comboBox_u_activestatus")
        self.comboBox_u_activestatus.setGeometry(QRect(240, 450, 161, 20))
        self.comboBox_u_activestatus.addItems(atv_status)
        self.dateEdit_u_create_date = QDateEdit(self.widget)
        self.dateEdit_u_create_date.setObjectName(u"dateEdit_u_create_date")
        self.dateEdit_u_create_date.setGeometry(QRect(240, 380, 161, 22))
        self.toolButton_save_assetuser = QToolButton(self.widget)
        self.toolButton_save_assetuser.setObjectName(u"toolButton_save_assetuser")
        self.toolButton_save_assetuser.setGeometry(QRect(160, 490, 141, 31))
        self.toolButton_save_assetuser.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")

        self.toolButton_mainpage = QToolButton(self.widget)
        self.toolButton_mainpage.setObjectName(u"toolButton_mainpage")
        self.toolButton_mainpage.setGeometry(QRect(330, 490, 141, 31))
        self.toolButton_mainpage.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")

        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(-10, 0, 630, 50))
        self.top_bar.setMaximumSize(QSize(16777215, 50))
        self.top_bar.setStyleSheet(u"background-color:rgb(13, 41, 86)")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.lable_title = QLabel(self.top_bar)
        self.lable_title.setObjectName(u"lable_title")
        self.lable_title.setGeometry(QRect(100, 0, 361, 51))
        self.lable_title.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lable_title.setFont(font)
        self.lable_title.setStyleSheet(u"color: rgb(33, 189, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit_u_email, self.lineEdit_u_cont_no)
        QWidget.setTabOrder(self.lineEdit_u_cont_no, self.lineEdit_u_name)
        QWidget.setTabOrder(self.lineEdit_u_name, self.lineEdit_u_assetid)
        QWidget.setTabOrder(self.lineEdit_u_assetid, self.lineEdit_u_sitloc)
        QWidget.setTabOrder(self.lineEdit_u_sitloc, self.lineEdit_u_dept)
        QWidget.setTabOrder(self.lineEdit_u_dept, self.lineEdit_u_desig)
        QWidget.setTabOrder(self.lineEdit_u_desig, self.dateEdit_u_create_date)
        QWidget.setTabOrder(self.dateEdit_u_create_date, self.lineEdit_other_detail)
        QWidget.setTabOrder(self.lineEdit_other_detail, self.comboBox_u_activestatus)
        QWidget.setTabOrder(self.comboBox_u_activestatus, self.toolButton_save_assetuser)
        QWidget.setTabOrder(self.comboBox_u_activestatus, self.toolButton_mainpage)

        self.retranslateUi(MainWindow)

        self.toolButton_save_assetuser.clicked.connect(lambda :self.submit())
        #self.toolButton_mainpage.clicked.connect(lambda: self.mainpage())
        self.toolButton_mainpage.clicked.connect(self.openWindow)
        #self.toolButton_mainpage.clicked.connect(self.mainpage())
        self.userid()
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_u_cont_no.setText(QCoreApplication.translate("MainWindow", u" User Contact number", None))
        self.label_u_name.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_u_assetid.setText(QCoreApplication.translate("MainWindow", u"User's Asset Id", None))
        self.label_u_dept.setText(QCoreApplication.translate("MainWindow", u"User Department", None))
        self.label_u_sitloc.setText(QCoreApplication.translate("MainWindow", u"User's Sitting Location", None))
        self.label_u_desig.setText(QCoreApplication.translate("MainWindow", u"User's Designation", None))
        self.label_u_creat_date.setText(QCoreApplication.translate("MainWindow", u"User Creation Date", None))
        self.label_other_detail.setText(QCoreApplication.translate("MainWindow", u"Other Details", None))
        self.label_u_activestatus.setText(QCoreApplication.translate("MainWindow", u"User Active Status", None))
        self.a_userid.setText(QCoreApplication.translate("MainWindow", u"Asset User id", None))
        self.u_email.setText(QCoreApplication.translate("MainWindow", u" User Email", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#55aa00;\"> Add New Asset User</span></p></body></html>", None))
        self.a_userid_input.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_save_assetuser.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.toolButton_mainpage.setText(QCoreApplication.translate("MainWindow", u"MAIN PAGE", None))
        self.lable_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffff7f;\">Asset User</span></p></body></html>", None))
    # retranslateUi

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow_user()
    ui = Ui_MainWindow_user()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())