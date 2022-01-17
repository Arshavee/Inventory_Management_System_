from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import (QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QWidget)
import sqlite3
from ui_Application import Ui_MainWindow

class Ui_MainWindow_allocation(object):
    def openWindow(self):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            MainWindow.hide()
    def allocation(self):
        astid=self.lineEdit_assetid_allo.text()
        usrid=self.lineEdit_userid_allo.text()

        param=[astid,usrid,"Allocate"]
        print(param)
        connection = sqlite3.connect("appuser_db.db")
        crsr = connection.cursor()
        sql_command = '''INSERT into asset_allocation (ast_id,user_id,status,status_chng_dt) values(?,?,?,( select date()));'''
        crsr.execute(sql_command, (param))
        connection.commit()
        connection.close()
        self.lineEdit_assetid_allo.setText("")
        self.lineEdit_userid_allo.setText("")
        print("allocation successfull ")
    def dislocation(self):
        astid=self.lineEdit_assetid_allo.text()
        usrid=self.lineEdit_userid_allo.text()
        id=[astid,usrid]
        connection = sqlite3.connect("appuser_db.db")
        crsr = connection.cursor()
        sql_command = '''UPDATE asset_allocation SET status = 'dislocate', status_chng_dt=( select date())
                        WHERE  ast_id=? and user_id= ?;'''
        crsr.execute(sql_command, id)
        connection.commit()
        connection.close()
        print("dislocation successfull ")
        self.lineEdit_assetid_allo.setText("")
        self.lineEdit_userid_allo.setText("")
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(629, 498)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 630, 50))
        self.top_bar.setMaximumSize(QSize(16777215, 50))
        self.top_bar.setStyleSheet(u"background-color:rgb(13, 41, 86)")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.lable_title = QLabel(self.top_bar)
        self.lable_title.setObjectName(u"lable_title")
        self.lable_title.setGeometry(QRect(150, 0, 411, 51))
        self.lable_title.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lable_title.setFont(font)
        self.lable_title.setStyleSheet(u"color: rgb(33, 189, 255);")
        self.label_55 = QLabel(self.centralwidget)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(170, 70, 331, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QFont.NoAntialias)
        self.label_55.setFont(font1)
        self.label_55.setCursor(QCursor(Qt.ArrowCursor))
        self.label_55.setAutoFillBackground(False)
        self.label_55.setFrameShadow(QFrame.Sunken)
        self.lineEdit_assetid_allo = QLineEdit(self.centralwidget)
        self.lineEdit_assetid_allo.setObjectName(u"lineEdit_assetid_allo")
        self.lineEdit_assetid_allo.setGeometry(QRect(250, 180, 171, 31))
        self.label_assetid_allo = QLabel(self.centralwidget)
        self.label_assetid_allo.setObjectName(u"label_assetid_allo")
        self.label_assetid_allo.setGeometry(QRect(120, 180, 101, 41))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_assetid_allo.setFont(font2)
        self.label_userid_allo = QLabel(self.centralwidget)
        self.label_userid_allo.setObjectName(u"label_userid_allo")
        self.label_userid_allo.setGeometry(QRect(130, 270, 101, 41))
        self.label_userid_allo.setFont(font2)
        self.lineEdit_userid_allo = QLineEdit(self.centralwidget)
        self.lineEdit_userid_allo.setObjectName(u"lineEdit_userid_allo")
        self.lineEdit_userid_allo.setGeometry(QRect(250, 280, 171, 31))

        self.btn_dislocate = QPushButton(self.centralwidget)
        self.btn_dislocate.setObjectName(u"btn_dislocate")
        self.btn_dislocate.setGeometry(QRect(40, 380, 131, 41))
        self.btn_dislocate.setStyleSheet(u"color: rgb(255,0,0);\n"
"\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.btn_allocate = QPushButton(self.centralwidget)
        self.btn_allocate.setObjectName(u"btn_allocate")
        self.btn_allocate.setGeometry(QRect(250, 380, 131, 41))
        self.btn_allocate.setMaximumSize(QSize(131, 16777215))
        self.btn_allocate.setStyleSheet(u"color: rgb(0, 170, 0);\n"
                                        
"font: 12pt \"MS Shell Dlg 2\";")
        self.btn_mainpage = QPushButton(self.centralwidget)
        self.btn_mainpage.setObjectName(u"btn_mainpage")
        self.btn_mainpage.setGeometry(QRect(440, 380, 131, 41))
        self.btn_mainpage.setMaximumSize(QSize(131, 16777215))
        self.btn_mainpage.setStyleSheet(u"color: rgb(0, 170, 0);\n"                                        
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_assetid = QLabel(self.centralwidget)
        self.label_assetid.setObjectName(u"label_assetid")
        self.label_assetid.setGeometry(QRect(440, 180, 141, 31))
        self.label_assetid.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_userid = QLabel(self.centralwidget)
        self.label_userid.setObjectName(u"label_userid")
        self.label_userid.setGeometry(QRect(440, 280, 141, 31))
        self.label_userid.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        self.btn_allocate.clicked.connect(lambda: self.allocation())
        self.btn_dislocate.clicked.connect(lambda: self.dislocation())
        self.btn_mainpage.clicked.connect(self.openWindow)
        #self.toolButton_mainpage.clicked.connect(self.openWindow)

        self.lineEdit_assetid_allo.textChanged[str].connect(self.onChanged_assetid)
        self.lineEdit_userid_allo.textChanged[str].connect(self.onChanged_userid)


    def onChanged_assetid(self, text):
        if text == "":
                print("Print from if")
                self.label_assetid.setText('')
                self.label_assetid.adjustSize()
        else:
                print("text : "+text)
                print(type(text))
                connection = sqlite3.connect("appuser_db.db")
                crsr = connection.cursor()
                sql_command = '''SELECT ast_name FROM asset WHERE ast_cont_id = (?);'''
                crsr.execute(sql_command, (text,))
                t = crsr.fetchall()
                connection.commit()
                connection.close()
                t_id = str(t)
                tt_id = t_id[3:-4]
                self.label_assetid.setText(tt_id)
                self.label_assetid.adjustSize()
    
    def onChanged_userid(self, text):
        if text == '':
                self.label_userid.setText("")
                self.label_userid.adjustSize()
        else:
                connection = sqlite3.connect("appuser_db.db")
                crsr = connection.cursor()
                sql_command = '''SELECT astusr_user_name FROM asset_user WHERE astusr_id = ?;'''
                crsr.execute(sql_command, (text,))
                t = crsr.fetchall()
                connection.commit()
                connection.close()
                t_id = str(t)
                tt_id = t_id[3:-4]
                self.label_userid.setText(tt_id)
                self.label_userid.adjustSize()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lable_title.setText(QCoreApplication.translate("MainWindow", u"   Inventory Management", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#55aa7f;\">Asset Allocation</span></p></body></html>", None))
        self.label_assetid_allo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">Asset Id</span></p></body></html>", None))
        self.label_userid_allo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">User Id</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_dislocate.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">Dislocate</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_mainpage.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">MAIN PAGE</span></p></body></html>", None))
        self.btn_mainpage.setText(QCoreApplication.translate("MainWindow", u"MAIN PAGE", None))
        self.btn_dislocate.setText(QCoreApplication.translate("MainWindow", u"Dislocate", None))
        self.btn_allocate.setText(QCoreApplication.translate("MainWindow", u"Allocate", None))
        self.label_assetid.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_userid.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_userid.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.btn_mainpage.setText(QCoreApplication.translate("MainWindow", u"", None))

    # retranslateUi

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_allocation()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
