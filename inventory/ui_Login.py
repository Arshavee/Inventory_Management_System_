# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginwaEuOJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os,sys
import sqlite3
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from ui_Application import Ui_MainWindow
from Asset_user import Ui_MainWindow_user
from AssetNewAllocation import Ui_MainWindow_allocation
from assetsearch import Ui_MainWindow_search

mainList = ['Asset Data','User Entry','Asset Allocation','Asset Search']

class Ui_mainWindow(object):
    def db_conn(self):
        userid = self.textEdit_userid.text()
        connection = sqlite3.connect("appuser_db.db")

        cursor = connection.cursor()
        sql_fetch_password = """select sys_pass from login_page where user_name = ?"""
        cursor.execute(sql_fetch_password, (userid,))
        print("in database")
        record = str(cursor.fetchall())
        passwd = record.strip(" [()],'")
        print(passwd)
        password = self.textEdit_password.text()
        print(password)
        if (passwd == password) & (password != ""):
            if self.comboBox_login.currentText() == 'User Entry':
                self.openUser()
            if self.comboBox_login.currentText() == 'Asset Data':
                self.openApplication()
            if self.comboBox_login.currentText() == 'Asset Allocation':
                self.openAllocation()
            if self.comboBox_login.currentText() == 'Asset Search':
                self.openSearch()
        else:
            print("Password unmatched")
            MainWindow.hide()
        return passwd
        cursor.close()
        connection.close()

    def openApplication(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()
    
    def openUser(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_user()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def openAllocation(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_allocation()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def openSearch(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_search()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(527, 481)
        MainWindow.setMinimumSize(QtCore.QSize(527, 481))
        MainWindow.setMaximumSize(QtCore.QSize(527, 481))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LOGIN = QFrame(self.centralwidget)
        self.LOGIN.setObjectName(u"LOGIN")
        self.LOGIN.setGeometry(QRect(80, 0, 351, 481))
        self.LOGIN.setFrameShape(QFrame.StyledPanel)
        self.LOGIN.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.LOGIN)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 190, 61, 21))
        self.loginButton = QCommandLinkButton(self.LOGIN)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(140, 380, 81, 41))
        self.label_5 = QLabel(self.LOGIN)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 270, 81, 21))
        self.comboBox_login = QComboBox(self.LOGIN)
        self.comboBox_login.setObjectName(u"comboBox_login")
        self.comboBox_login.setGeometry(QRect(68, 330, 221, 31))
        self.comboBox_login.addItems(mainList)
        self.comboBox_login.setEditable(True)
        self.label_3 = QLabel(self.LOGIN)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 40, 301, 41))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QFont.NoAntialias)
        self.label_3.setFont(font)
        self.label_3.setCursor(QCursor(Qt.ArrowCursor))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(self.LOGIN)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 301, 41))
        self.label_4.setFont(font)
        self.label_4.setCursor(QCursor(Qt.ArrowCursor))
        self.label_4.setAutoFillBackground(True)
        self.label_4.setFrameShadow(QFrame.Sunken)
        self.textEdit_userid = QLineEdit(self.LOGIN)
        self.textEdit_userid.setObjectName(u"textEdit_userid")
        self.textEdit_userid.setGeometry(QRect(150, 190, 141, 31))
        self.textEdit_password = QLineEdit(self.LOGIN)
        self.textEdit_password.setEchoMode(QLineEdit.Password)
        self.textEdit_password.setObjectName(u"textEdit_password")
        self.textEdit_password.setGeometry(QRect(150, 270, 141, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.textEdit_userid, self.textEdit_password)
        QWidget.setTabOrder(self.textEdit_password, self.comboBox_login)
        QWidget.setTabOrder(self.comboBox_login, self.loginButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.loginButton.clicked.connect(lambda: self.db_conn())
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        #self.LOGIN.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#00aa7f;\">Password</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#00aa7f;\">User Id</span></p></body></html>", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.loginButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#00aa7f;\">Password</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1f78cc;\">Inventory Management</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">LOGIN</span></p></body></html>", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
