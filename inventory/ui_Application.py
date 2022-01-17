# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainRpxBXz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient, QStandardItemModel, QStandardItem, )
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
import sqlite3

import datetime
import sys

type_list = []
group_list = []
data = {}
ast_status = ["Active", "Inactive"]


class Ui_MainWindow(object):
    def get_ast_cont_id(self):
        connection = sqlite3.connect("appuser_db.db")
        crsr = connection.cursor()
        sql_command = '''SELECT ast_id FROM asset ORDER BY ROWID DESC LIMIT 1;'''
        crsr.execute(sql_command)
        # connection.commit()
        par = crsr.fetchall()
        print(par)
        a = str(par)

        par = (a[2:-3])
        print(par)
        if par == " ":
            ast_id = "1"
        else:
            ast_id = str(int(par) + 1)
        ast_cont_id = str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + str(ast_id).zfill(
            6 - len(ast_id))
        print(ast_cont_id)
        self.lineEdit_asset_id.setText(ast_cont_id)
    def dependent_combobox(self):
        global data
        connection = sqlite3.connect("appuser_db.db")
        cur = connection.cursor()
        cur.execute("SELECT t_id,t_desc FROM asset_type")
        rows = cur.fetchall()
        cur.close()

        gdesc_lst = []
        tdesc_lst = []

        for item in rows:
            type_list = []
            c = str(item)
            c = c[5:-2]
            a = str(item)
            a = a[1]
            print(c)
            tdesc_lst.append(c)
            connection = sqlite3.connect("appuser_db.db")
            cur = connection.cursor()
            scommand = '''SELECT g_desc FROM asset_group where g_t_id=(?);'''
            cur.execute(scommand, (a,))
            tt_desc = cur.fetchall()
            for item in tt_desc:
                c = str(item)
                c = c[2:-3]
                type_list.append(c)

            gdesc_lst.append(type_list)
            connection.commit()
            connection.close()
        data = dict(zip(tdesc_lst, gdesc_lst))
    def updateStateCombo_asset(self, index):
        indx = self.model.index(index, 0, self.comboBox_type_asset.rootModelIndex())
        self.comboBox_group_asset.setRootModelIndex(indx)
        self.comboBox_group_asset.setCurrentIndex(0)
    def updateStateCombo_asset_edit(self, index):
        indx = self.model.index(index, 0, self.comboBox_type_asset.rootModelIndex())
        self.comboBox_group_asset_edit_2.setRootModelIndex(indx)
        self.comboBox_group_asset_edit_2.setCurrentIndex(0)
    def updateStateCombo_bulkupload(self, index):
        indx = self.model.index(index, 0, self.comboBox_type_asset.rootModelIndex())
        self.comboBox_group_asset_edit_bulk.setRootModelIndex(indx)
        self.comboBox_group_asset_edit_bulk.setCurrentIndex(0)
    def bulkuoload_commit(self):
        self.asset_view_id_edit.setCurrentText(" ")
        id = self.label_Asset_id_edit_input_bulk.text()
        ast_srl_no = self.lineEdit_srlno_edit_bulk.text()
        ast_name = self.lineEdit_asset_name_edit_bulk.text()
        ast_type = self.comboBox_type_asset_edit_bulk.currentText()

        ast_grp = self.comboBox_group_asset_edit_bulk.currentText()
        self.comboBox_group_asset_edit_bulk.addItems(group_list)
        ast_details = self.lineEdit_details_edit_bulk.text()
        ast_parent = self.lineEdit_asset_parend_id_edit_bulk.text()
        ast_oem = self.lineEdit_asset_oem_edit_bulk.text()
        oem_cont_no = self.lineEdit_oem_contact_edit_bulk.text()
        oem_cont_no_1 = self.lineEdit_oem_contact_edit_2_bulk.text()
        ast_seller = self.lineEdit_asset_seller_name_edit_bulk.text()
        ast_seller_no = self.lineEdit_seller_contact_edit_bulk.text()
        oem_email = self.lineEdit_oem_email_edit_bulk.text()
        oem_email_esk1 = self.lineEdit_oem_email1_edit_bulk.text()
        ast_seller_email = self.lineEdit_seller_email_edit_bulk.text()
        ast_purchase_date = self.dateEdit_purchasedate_edit_bulk.text()
        ast_warranty_details = self.lineEdit_warranty_details_edit_bulk.text()
        ast_warranty_enddate = self.dateEdit_warranty_enddate_edit_bulk.text()
        ast_status = self.comboBox_asset_status_edit_bulk.currentText()
        self.comboBox_asset_status_edit_bulk.addItems(ast_status)
        ast_price = self.lineEdit_asset_price_edit_bulk.text()
        params = (
            id, ast_srl_no, ast_name, ast_type, ast_grp, ast_details, ast_parent, ast_oem, oem_cont_no,
            oem_cont_no_1, ast_seller, ast_seller_no, oem_email, oem_email_esk1, ast_seller_email, ast_purchase_date,
            ast_warranty_details, ast_warranty_enddate, ast_status, ast_price)

        print(params)
        print(len(params))
        try:
            connection = sqlite3.connect("appuser_db.db", timeout=10)

            # cursor
            crsr = connection.cursor()
            sql_command = '''INSERT into asset (ast_cont_id,ast_srlno,ast_name,ast_type,ast_grp,ast_details,ast_parent,ast_oem,oem_contno,
                	oem_contno_esk1,ast_seller,ast_sellerno,oem_email,oem_email_esk1,seller_email,ast_purchasedate,ast_warranty_details,
                	ast_warranty_enddate,ast_status,ast_price) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
            crsr.execute(sql_command, params)
            connection.commit()
            print("Committed Successfully")
            crsr.close()
        except sqlite3.Error as error:
            print("Failed to update multiple records of sqlite table", error)
        finally:
            if (connection):
                connection.close()
                print("The SQLite connection is closed")
        self.label_Asset_id_edit_input_bulk.setText(" ")
        self.lineEdit_srlno_edit_bulk.setText(" ")
        self.lineEdit_asset_name_edit_bulk.setText(" ")
        self.comboBox_type_asset_edit_bulk.clear()
        self.comboBox_group_asset_edit_bulk.clear()
        self.lineEdit_details_edit_bulk.setText(" ")
        self.lineEdit_asset_parend_id_edit_bulk.setText(" ")
        self.lineEdit_asset_oem_edit_bulk.setText(" ")
        self.lineEdit_oem_contact_edit_bulk.setText(" ")
        self.lineEdit_oem_contact_edit_2_bulk.setText(" ")
        self.lineEdit_asset_seller_name_edit_bulk.setText(" ")
        self.lineEdit_seller_contact_edit_bulk.setText(" ")
        self.lineEdit_oem_email_edit_bulk.setText(" ")
        self.lineEdit_oem_email1_edit_bulk.setText(" ")
        self.lineEdit_seller_email_edit_bulk.setText(" ")
        self.dateEdit_purchasedate_edit_bulk.clear()
        self.lineEdit_warranty_details_edit_bulk.setText(" ")
        self.dateEdit_warranty_enddate_edit_bulk.clear()
        self.comboBox_asset_status_edit_bulk.clear()
        self.lineEdit_asset_price_edit_bulk.setText(" ")
        self.asset_view_id_edit_bulk.clear()
    def bulkupload(self):
        id = self.asset_view_id_edit_bulk.currentText()
        '''
        connection = sqlite3.connect("appuser_db.db")
        crsr = connection.cursor()
        
        sql_command = SELECT ast_cont_id FROM asset ORDER BY ROWID DESC LIMIT 1;
        crsr.execute(sql_command)
        # connection.commit()
        params = crsr.fetchall()
        a = str(params)
        par = (a[3:-4])
        print(par)
        connection.close()
        if (par == ' '):
            c = 1
        else:
            a = int(par)
            c = a + 1
        '''
        connection = sqlite3.connect("appuser_db.db")
        crsr = connection.cursor()
        sql_command = '''SELECT ast_id FROM asset ORDER BY ROWID DESC LIMIT 1;'''
        crsr.execute(sql_command)
        # connection.commit()
        par = crsr.fetchall()
        print(par)
        a = str(par)

        par = (a[2:-3])
        print(par)

        c = str(int(par) + 1)


        print(c)
        print(type(c))
        m = str(c)
        cont_id=str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + m.zfill(6 - len(m))
        print(cont_id)
        self.label_Asset_id_edit_input_bulk.setText(cont_id)

        connection = sqlite3.connect("appuser_db.db")
        crsr = connection.cursor()
        sql_command = '''SELECT * FROM asset Where ast_cont_id= (?);'''
        crsr.execute(sql_command, (id,))
        # connection.commit()
        params = crsr.fetchall()
        connection.close()
        print(params)
        print("param")

        pd = str(params[0][20])
        print(pd)
        y = (pd[6:])
        m = pd[3:5]
        d = pd[0:2]
        print(y)
        print(m)
        print(d)
        ppd = QDate(int(y), int(m), int(d))

        wd = str(params[0][22])
        wy = (wd[6:])
        wm = wd[3:5]
        wd = wd[0:2]
        wwd = QDate(int(wy), int(wm), int(wd))

        # self.lineEdit_srlno_edicomboBox_type_asset_edit_bulk.setText(str(params[0][1]))
        self.lineEdit_asset_name_edit_bulk.setText(str(params[0][3]))
        self.comboBox_type_asset_edit_bulk.setCurrentText(str(params[0][4]))
        self.comboBox_group_asset_edit_bulk.setCurrentText(str(params[0][5]))
        self.lineEdit_details_edit_bulk.setText(str(params[0][6]))
        self.lineEdit_asset_parend_id_edit_bulk.setText(str(params[0][7]))
        self.lineEdit_asset_oem_edit_bulk.setText(str(params[0][8]))
        self.lineEdit_oem_contact_edit_bulk.setText(str(params[0][9]))
        self.lineEdit_oem_contact_edit_2_bulk.setText(str(params[0][10]))
        self.lineEdit_asset_seller_name_edit_bulk.setText(str(params[0][11]))
        self.lineEdit_seller_contact_edit_bulk.setText(str(params[0][12]))
        self.lineEdit_oem_email_edit_bulk.setText(str(params[0][13]))
        self.lineEdit_oem_email1_edit_bulk.setText(str(params[0][14]))
        self.lineEdit_seller_email_edit_bulk.setText(str(params[0][15]))
        self.dateEdit_purchasedate_edit_bulk.setDate(ppd)
        self.lineEdit_warranty_details_edit_bulk.setText(str(params[0][21]))
        self.dateEdit_warranty_enddate_edit_bulk.setDate(wwd)
        self.comboBox_asset_status_edit_bulk.setCurrentText(str(params[0][23]))
        self.comboBox_asset_status_edit_bulk.addItems(ast_status)
        self.lineEdit_asset_price_edit_bulk.setText(str(params[0][24]))
    def callidasset(self):
        listy = []
        connection = sqlite3.connect("appuser_db.db")

        crsr = connection.cursor()
        sql_command = '''SELECT ast_cont_id from asset;'''
        crsr.execute(sql_command)
        # connection.commit()
        params = crsr.fetchall()
        print(params)
        for item in params:
            c = str(item)
            c = c[2:-3]
            listy.append(c)

        print(listy)
        listy=set(listy)
        listy=sorted(listy)
        # list = params[2:-3]
        # print(list)

        #
        self.asset_view_id_edit_bulk.addItems(listy)
        self.asset_view_id.addItems(listy)
        self.asset_view_id_edit.addItems(listy)
    def group_view(self):
        grp_id = self.lineEdit_groupeview_id.currentText()
        self.lineEdit_groupeview_id.setCurrentText(" ")
        connection = sqlite3.connect("appuser_db.db")

        crsr = connection.cursor()
        sql_command = '''SELECT * FROM asset_group Where g_id= (?);'''
        crsr.execute(sql_command, (grp_id,))
        # connection.commit()
        params = crsr.fetchall()

        connection = sqlite3.connect("appuser_db.db")
        cur = connection.cursor()
        id = str(params[0][1])
        print(id)
        scommand = '''SELECT t_desc FROM asset_type where t_id=(?);'''
        cur.execute(scommand, (id,))
        tt_desc = cur.fetchall()
        print(tt_desc)
        connection.commit()
        connection.close()
        t = str(tt_desc)
        t_desc = t[3:-4]
        print(t_desc)
        connection.close()
        self.label_groupview_id_3.setText(str(params[0][0]))
        self.label_groupview_type_2.setText(t_desc)
        self.label_groupview_desc_2.setText(str(params[0][2]))
    def edit_group_commit(self):
        id = self.lineEdit_groupedit_id.currentText()
        self.lineEdit_groupedit_id.setCurrentText(" ")
        type = self.comboBox_groupedit_type.currentText()
        grpdesc = self.lineEdit_groupedit_desc.text()

        connection = sqlite3.connect("appuser_db.db")
        cur = connection.cursor()
        scommand = '''SELECT t_id FROM asset_type where t_desc=(?);'''
        cur.execute(scommand, (type,))
        t_id = cur.fetchall()
        connection.commit()
        connection.close()
        t_id = str(t_id)

        tt_id = t_id[2:-3]
        print(tt_id)
        param = (tt_id, grpdesc, id)
        try:
            connection = sqlite3.connect("appuser_db.db", timeout=10)

            # cursor
            crsr = connection.cursor()
            sql_command = '''UPDATE asset_group set g_t_id =?,g_desc =? WHERE g_id =?;'''
            crsr.execute(sql_command, param)
            connection.commit()
            print("Committed Successfully")
            crsr.close()
        except sqlite3.Error as error:
            print("Failed to update multiple records of sqlite table", error)
        finally:
            if (connection):
                connection.close()
                print("The SQLite connection is closed")
        self.label_groupedit_id_3.setText(" ")
        self.lineEdit_groupedit_desc.setText(" ")
        self.comboBox_groupedit_type.clear()
    def edit_group(self):
        global type_list
        print(type_list)
        grp_id = self.lineEdit_groupedit_id.currentText()
        print(grp_id)
        connection = sqlite3.connect("appuser_db.db")

        crsr = connection.cursor()
        sql_command = '''SELECT * FROM asset_group Where g_id= (?);'''
        crsr.execute(sql_command, (grp_id,))
        # connection.commit()
        params = crsr.fetchall()
        connection.close()
        connection = sqlite3.connect("appuser_db.db")
        cur = connection.cursor()
        id = str(params[0][1])
        print(id)
        scommand = '''SELECT t_desc FROM asset_type where t_id=(?);'''
        cur.execute(scommand, (id,))
        tt_desc = cur.fetchall()
        print(tt_desc)
        connection.commit()
        connection.close()
        t = str(tt_desc)
        t_desc = t[3:-4]
        print(t_desc)
        self.label_groupedit_id_3.setText(str(params[0][0]))
        self.comboBox_groupedit_type.addItems(type_list)
        self.comboBox_groupedit_type.setCurrentText(t_desc)
        self.lineEdit_groupedit_desc.setText(str(params[0][2]))
    def type_view(self):
        type_id = self.lineEdit_assettype_td_edit_view.currentText()
        print(type_id)
        self.lineEdit_assettype_td_edit_view.setCurrentText(" ")
        connection = sqlite3.connect("appuser_db.db")

        crsr = connection.cursor()
        sql_command = '''SELECT * FROM asset_type Where t_id= (?);'''
        crsr.execute(sql_command, (type_id,))
        # connection.commit()
        params = crsr.fetchall()
        connection.close()
        self.label_type_id_assettype_view_2.setText(str(params[0][0]))
        self.label_type_desc_assettype_view_2.setText(str(params[0][1]))
    def edit_type_commit(self):
        id = self.lineEdit_assettype_td_edit.currentText()
        self.lineEdit_assettype_td_edit.setCurrentText(" ")
        des = self.lineEdit_assettype_description_edit.text()
        param = (des, id)
        try:
            connection = sqlite3.connect("appuser_db.db", timeout=10)

            # cursor
            crsr = connection.cursor()
            sql_command = '''UPDATE asset_type set t_desc =? WHERE t_id =?;'''
            crsr.execute(sql_command, param)
            connection.commit()
            print("Committed Successfully")
            crsr.close()
        except sqlite3.Error as error:
            print("Failed to update multiple records of sqlite table", error)
        finally:
            if (connection):
                connection.close()
                print("The SQLite connection is closed")
        self.label_typeid_edit_input.setText(" ")
        self.lineEdit_assettype_description_edit.setText(" ")
    def edit_type(self):
        type_id = self.lineEdit_assettype_td_edit.currentText()
        print(type_id)
        connection = sqlite3.connect("appuser_db.db")

        crsr = connection.cursor()
        sql_command = '''SELECT * FROM asset_type Where t_id= (?);'''
        crsr.execute(sql_command, (type_id,))
        # connection.commit()
        params = crsr.fetchall()
        connection.close()
        self.label_typeid_edit_input.setText(str(params[0][0]))
        self.lineEdit_assettype_description_edit.setText(str(params[0][1]))
    def edit_asset_commit(self):
        ast_id = self.asset_view_id_edit.currentText()
        print(ast_id)
        self.asset_view_id_edit.setCurrentText(" ")
        ast_srl_no = self.lineEdit_srlno_edit_2.text()
        ast_name = self.lineEdit_asset_name_edit_2.text()
        ast_type = self.comboBox_type_asset_edit_2.currentText()
        ast_grp = self.comboBox_group_asset_edit_2.currentText()
        ast_details = self.lineEdit_details_edit_2.text()
        ast_parent = self.lineEdit_asset_parend_id_edit_2.text()
        ast_oem = self.lineEdit_asset_oem_edit_2.text()
        oem_cont_no = self.lineEdit_oem_contact_edit_3.text()
        oem_cont_no_1 = self.lineEdit_oem_contact_edit_4.text()
        ast_seller = self.lineEdit_asset_seller_name_edit_2.text()
        ast_seller_no = self.lineEdit_seller_contact_edit_2.text()
        oem_email = self.lineEdit_oem_email_edit_2.text()
        oem_email_esk1 = self.lineEdit_oem_email1_edit_2.text()
        ast_seller_email = self.lineEdit_seller_email_edit_2.text()
        ast_purchase_date = self.dateEdit_purchasedate_edit_2.text()
        ast_warranty_details = self.lineEdit_warranty_details_edit_2.text()
        ast_warranty_enddate = self.dateEdit_warranty_enddate_edit_2.text()
        ast_status = self.comboBox_asset_status_edit_2.currentText()
        ast_price = self.lineEdit_asset_price_edit_2.text()
        params = (
            ast_srl_no, ast_name, ast_type, ast_grp, ast_details, ast_parent, ast_oem, oem_cont_no,
            oem_cont_no_1, ast_seller, ast_seller_no, oem_email, oem_email_esk1, ast_seller_email, ast_purchase_date,
            ast_warranty_details, ast_warranty_enddate, ast_status, ast_price, ast_id)

        print(params)
        print(len(params))
        try:
            connection = sqlite3.connect("appuser_db.db", timeout=10)

            # cursor
            crsr = connection.cursor()
            sql_command = '''UPDATE asset set ast_srlno =?,ast_name =?,ast_type =?,ast_grp =?,ast_details =?,ast_parent =?,
                      ast_oem =?,oem_contno =?,oem_contno_esk1 =?,ast_seller =?,ast_sellerno =?,oem_email =?,oem_email_esk1 =?,
                      seller_email =?,ast_purchasedate =?,ast_warranty_details =?,ast_warranty_enddate =?,ast_status =?,ast_price =?
                         WHERE ast_cont_id =?;'''
            crsr.execute(sql_command, params)
            connection.commit()
            print("Committed Successfully")
            crsr.close()
        except sqlite3.Error as error:
            print("Failed to update multiple records of sqlite table", error)
        finally:
            if (connection):
                connection.close()
                print("The SQLite connection is closed")
        self.label_Asset_id_edit_input.setText(" ")
        self.lineEdit_srlno_edit_2.setText(" ")
        self.lineEdit_asset_name_edit_2.setText(" ")
        self.comboBox_type_asset_edit_2.clear()
        self.comboBox_group_asset_edit_2.clear()
        self.lineEdit_details_edit_2.setText(" ")
        self.lineEdit_asset_parend_id_edit_2.setText(" ")
        self.lineEdit_asset_oem_edit_2.setText(" ")
        self.lineEdit_oem_contact_edit_3.setText(" ")
        self.lineEdit_oem_contact_edit_4.setText(" ")
        self.lineEdit_asset_seller_name_edit_2.setText(" ")
        self.lineEdit_seller_contact_edit_2.setText(" ")
        self.lineEdit_oem_email_edit_2.setText(" ")
        self.lineEdit_oem_email1_edit_2.setText(" ")
        self.lineEdit_seller_email_edit_2.setText(" ")
        self.dateEdit_purchasedate_edit_2.clear()
        self.lineEdit_warranty_details_edit_2.setText(" ")
        self.dateEdit_warranty_enddate_edit_2.clear()
        self.comboBox_asset_status_edit_2.clear()
        self.lineEdit_asset_price_edit_2.setText(" ")
    def edit_asset(self):
        global type_list
        print(type_list)
        id = self.asset_view_id_edit.currentText()
        print(id)
        connection = sqlite3.connect("appuser_db.db")
        crsr = connection.cursor()
        sql_command = '''SELECT * FROM Asset Where ast_cont_id= (?);'''
        crsr.execute(sql_command, (id,))
        params = crsr.fetchall()

        print(params[0][5])
        # params = param [2:-3]
        print(type(params[0][0]))
        connection.close()
        print(params)

        pd=str(params[0][20])
        y=(pd[6:])
        m=pd[3:5]
        d=pd[0:2]
        ppd=QDate(int(y),int(m),int(d))

        wd = str(params[0][22])
        wy = (wd[6:])
        wm = wd[3:5]
        wd = wd[0:2]
        wwd = QDate(int(wy),int(wm),int(wd))

        self.label_Asset_id_edit_input.setText(str(params[0][1]))
        self.lineEdit_srlno_edit_2.setText(str(params[0][2]))
        self.lineEdit_asset_name_edit_2.setText(str(params[0][3]))
        # self.label_assetview_type_input.setText(str(params[0][3]))
        # self.comboBox_type_asset_edit_2.addItems(type_list)
        self.comboBox_type_asset_edit_2.setCurrentText(str(params[0][4]))
        # self.comboBox_group_asset_edit_2.addItems(group_list)
        self.comboBox_group_asset_edit_2.setCurrentText(str(params[0][5]))
        self.lineEdit_details_edit_2.setText(str(params[0][6]))
        self.lineEdit_asset_parend_id_edit_2.setText(str(params[0][7]))
        self.lineEdit_asset_oem_edit_2.setText(str(params[0][8]))
        self.lineEdit_oem_contact_edit_3.setText(str(params[0][9]))
        self.lineEdit_oem_contact_edit_4.setText(str(params[0][10]))
        self.lineEdit_asset_seller_name_edit_2.setText(str(params[0][11]))
        self.lineEdit_seller_contact_edit_2.setText(str(params[0][12]))
        self.lineEdit_oem_email_edit_2.setText(str(params[0][13]))
        self.lineEdit_oem_email1_edit_2.setText(str(params[0][14]))
        self.lineEdit_seller_email_edit_2.setText(str(params[0][15]))
        self.dateEdit_purchasedate_edit_2.setDate(ppd)
        self.lineEdit_warranty_details_edit_2.setText(str(params[0][21]))
        self.dateEdit_warranty_enddate_edit_2.setDate(wwd)
        self.comboBox_asset_status_edit_2.addItems(ast_status)
        self.comboBox_asset_status_edit_2.setCurrentText(str(params[0][23]))
        self.lineEdit_asset_price_edit_2.setText(str(params[0][24]))
    def view_asset(self):
        id = self.asset_view_id.currentText()
        print(id)
        self.asset_view_id.setCurrentText(" ")
        connection = sqlite3.connect("appuser_db.db")

        crsr = connection.cursor()
        sql_command = '''SELECT * FROM Asset Where ast_cont_id= (?);'''
        crsr.execute(sql_command, (id,))
        # connection.commit()
        params = crsr.fetchall()
        print(params[0][5])
        # params = param [2:-3]
        print(type(params[0][0]))
        connection.close()
        print(params)
        self.label_assetview_id_2_input.setText(str(params[0][1]))
        self.label_assetview_srlno_input.setText(str(params[0][2]))
        self.label_assetview_assetname_input.setText(str(params[0][3]))
        self.label_assetview_type_input.setText(str(params[0][4]))
        self.label_assetview_group_input.setText(str(params[0][5]))
        self.label_assetview_details_input.setText(str(params[0][6]))
        self.label_assetview_assetparentid_input.setText(str(params[0][7]))
        self.label_assetview_oemname_input.setText(str(params[0][8]))
        self.label_assetview_oemcontactno_input.setText(str(params[0][9]))
        self.label_assetview_oemcontactnoesk1_input.setText(str(params[0][10]))
        self.label_assetview_sellername_input.setText(str(params[0][11]))
        self.label_assetview_sellerno_input.setText(str(params[0][12]))
        self.label_assetview_oememail_input.setText(str(params[0][13]))
        self.label_assetview_oememailesk1_input.setText(str(params[0][14]))
        self.label_assetview_selleremail_input.setText(str(params[0][15]))
        self.label_assetview_purchasedate_input.setText(str(params[0][20]))
        self.label_assetview_Warrentydetails_input.setText(str(params[0][21]))
        self.label_assetview_warrentyenddate_input.setText(str(params[0][22]))
        self.label_assetview_status_input.setText(str(params[0][23]))
        self.label_assetview_price_input.setText(str(params[0][24]))
    def commit_data_asset(self):

        connection = sqlite3.connect("appuser_db.db")
        crsr = connection.cursor()
        sql_command = '''SELECT ast_id FROM asset ORDER BY ROWID DESC LIMIT 1;'''
        crsr.execute(sql_command)
        # connection.commit()
        par = crsr.fetchall()
        print(par)
        a = str(par)

        par = (a[2:-3])
        print(par)
        if par==" ":
            ast_id = "1"
        else:
            ast_id=str(int(par)+1)

        ast_srl_no=self.lineEdit_serial_no.text()
        ast_name=self.lineEdit_asset_name.text()
        ast_type=self.comboBox_type_asset.currentText()
        ast_grp=self.comboBox_group_asset.currentText()
        ast_details=self.lineEdit_details.text()
        ast_parent=self.lineEdit_asset_parend_id.text()
        ast_oem=self.lineEdit_asset_oem.text()
        oem_cont_no=self.lineEdit_oem_contact.text()
        oem_cont_no_1=self.lineEdit_oem_contact_1.text()
        ast_seller=self.lineEdit_asset_seller_name.text()
        ast_seller_no=self.lineEdit_seller_contact.text()
        oem_email=self.lineEdit_oem_email.text()
        oem_email_esk1=self.lineEdit_oem_email1.text()
        ast_seller_email=self.lineEdit_seller_email.text()
        ast_purchase_date=self.dateEdit_purchasedate.text()
        ast_warranty_details=self.lineEdit_warranty_details.text()
        ast_warranty_enddate=self.dateEdit_warranty_enddate.text()
        ast_status=self.comboBox_asset_status.currentText()
        ast_price=self.lineEdit_asset_price.text()
        ast_cont_id = str(datetime.datetime.now().year) + str(datetime.datetime.now().month )+ str(ast_id).zfill(6-len(ast_id))
        print(ast_cont_id)

        params = (
        ast_id, ast_cont_id,ast_srl_no, ast_name, ast_type, ast_grp, ast_details, ast_parent, ast_oem, oem_cont_no, oem_cont_no_1,
        ast_seller, ast_seller_no, oem_email, oem_email_esk1, ast_seller_email, ast_purchase_date,
        ast_warranty_details, ast_warranty_enddate, ast_status, ast_price)

        print(params)
        connection = sqlite3.connect("appuser_db.db")

        # cursor
        crsr = connection.cursor()
        sql_command = '''INSERT into asset (ast_id,ast_cont_id,ast_srlno,ast_name,ast_type,ast_grp,ast_details,ast_parent,ast_oem,oem_contno,
        	oem_contno_esk1,ast_seller,ast_sellerno,oem_email,oem_email_esk1,seller_email,ast_purchasedate,ast_warranty_details,
        	ast_warranty_enddate,ast_status,ast_price) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
        crsr.execute(sql_command, params)
        connection.commit()
        print("Committed Successfully")
        connection.close()

        self.lineEdit_asset_id.setText(" ")
        self.lineEdit_serial_no.setText(" ")
        self.lineEdit_asset_name.setText(" ")
        self.comboBox_type_asset.clear()
        self.comboBox_group_asset.clear()
        self.lineEdit_details.setText(" ")
        self.lineEdit_asset_parend_id.setText(" ")
        self.lineEdit_asset_oem.setText(" ")
        self.lineEdit_oem_contact.setText(" ")
        self.lineEdit_oem_contact_1.setText(" ")
        self.lineEdit_asset_seller_name.setText(" ")
        self.lineEdit_seller_contact.setText(" ")
        self.lineEdit_oem_email.setText(" ")
        self.lineEdit_oem_email1.setText(" ")
        self.lineEdit_seller_email.setText(" ")
        self.dateEdit_purchasedate.clear()
        self.lineEdit_warranty_details.setText(" ")
        self.dateEdit_warranty_enddate.clear()
        self.comboBox_asset_status.clear()
        self.lineEdit_asset_price.setText(" ")

        self.callidasset()
    def commit_data_type(self):
        type_a = self.lineEdit_assettype_td.text()
        print(type_a)
        connection = sqlite3.connect("appuser_db.db")

        crsr = connection.cursor()
        sql_command = '''INSERT into asset_type (t_desc) VALUES (?);'''
        crsr.execute(sql_command, (type_a,))
        connection.commit()
        print("commited successfully")
        connection.close()
        self.lineEdit_assettype_td.setText(" ")
    def commit_data_group(self):
        t1 = self.comboBox_Astgrp_type.currentText()
        desc = self.lineEdit_assetgroup_gd.text()

        connection = sqlite3.connect("appuser_db.db")
        cur = connection.cursor()
        scommand = '''SELECT t_id FROM asset_type where t_desc=(?);'''
        cur.execute(scommand, (t1,))
        t_id = cur.fetchall()
        connection.commit()
        connection.close()
        t_id = str(t_id)

        tt_id = t_id[2:-3]
        print(tt_id)
        params = (desc, tt_id)

        con = sqlite3.connect("appuser_db.db")

        crsr = con.cursor()
        sql_command = '''INSERT into asset_group (g_desc,g_t_id) VALUES (?,?);'''
        crsr.execute(sql_command, params)
        print("committed successfully")
        con.commit()
        con.close()
        self.comboBox_Astgrp_type.clear()
        self.lineEdit_assetgroup_gd.setText(" ")
    def type_fch(self):
        global type_list
        # print("inside type_fch")
        connection = sqlite3.connect("appuser_db.db")
        cur = connection.cursor()
        cur.execute("SELECT t_desc FROM asset_type")
        rows = cur.fetchall()
        # print(rows)
        for item in rows:
            c = str(item)
            c = c[2:-3]
            # print(c)
            # print(type(item))
            type_list.append(c)
        # print(type_list)
        connection.commit()
        connection.close()
    def group_fch(self):
        global group_list
        # print("inside group_fch")
        connection = sqlite3.connect("appuser_db.db")
        cur = connection.cursor()
        cur.execute("SELECT g_desc FROM asset_group")
        rows = cur.fetchall()
        # print(rows)
        for item in rows:
            c = str(item)
            c = c[2:-3]
            # print(c)
            group_list.append(c)
        print(group_list)
        connection.commit()
        connection.close()
    def setupUi(self, MainWindow):
        self.dependent_combobox()
        print(data)
        self.type_fch()
        self.group_fch()
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 500)
        MainWindow.setMinimumSize(QSize(600, 500))
        MainWindow.setMaximumSize(QSize(600, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45,45,45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
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

        self.verticalLayout.addWidget(self.top_bar)

        self.main_window = QFrame(self.centralwidget)
        self.main_window.setObjectName(u"main_window")
        self.main_window.setStyleSheet(
            u"background-color: rgb(255, 255, 255);")
        self.main_window.setFrameShape(QFrame.NoFrame)
        self.main_window.setFrameShadow(QFrame.Raised)
        self.btn_assetgroup_view = QPushButton(self.main_window)
        self.btn_assetgroup_view.setObjectName(u"btn_assetgroup_view")
        self.btn_assetgroup_view.setGeometry(QRect(30, 300, 121, 21))
        self.btn_assetgroup_view.setStyleSheet(u"color: rgb(0,0,153);")
        self.label_asset = QLabel(self.main_window)
        self.label_asset.setObjectName(u"label_asset")
        self.label_asset.setGeometry(QRect(50, 20, 81, 21))
        self.label_asset.setStyleSheet(u"color: rgb(153,0,76);")
        assetFont = QtGui.QFont()
        assetFont.setBold(True)
        self.label_asset.setFont(assetFont)
        self.pushButton_bulkupload = QPushButton(self.main_window)
        self.pushButton_bulkupload.setGeometry(QRect(30, 110, 121, 23))
        self.pushButton_bulkupload.setStyleSheet(u"color: rgb(0,0,153);")
        self.pushButton_bulkupload.setObjectName("pushButton_bulkupload")
        self.btn_asset_add = QPushButton(self.main_window)
        self.btn_asset_add.setObjectName(u"btn_asset_add")
        self.btn_asset_add.setGeometry(QRect(30, 50, 121, 21))
        self.btn_asset_add.setStyleSheet(u"color: rgb(0,0,153);")
        self.btn_assettype_view = QPushButton(self.main_window)
        self.btn_assettype_view.setObjectName(u"btn_assettype_view")
        self.btn_assettype_view.setGeometry(QRect(30, 200, 121, 21))
        self.btn_assettype_view.setStyleSheet(u"color: rgb(0,0,153);")
        self.btn_assetgroup_edit = QPushButton(self.main_window)
        self.btn_assetgroup_edit.setObjectName(u"btn_assetgroup_edit")
        self.btn_assetgroup_edit.setGeometry(QRect(30, 280, 121, 21))
        self.btn_assetgroup_edit.setStyleSheet(u"color: rgb(0,0,153);")
        self.btn_assettype_add = QPushButton(self.main_window)
        self.btn_assettype_add.setObjectName(u"btn_assettype_add")
        self.btn_assettype_add.setGeometry(QRect(30, 160, 121, 21))
        self.btn_assettype_add.setStyleSheet(u"color: rgb(0,0,153);")
        self.label_assetgroup = QLabel(self.main_window)
        self.label_assetgroup.setObjectName(u"label_assetgroup")
        self.label_assetgroup.setGeometry(QRect(60, 240, 70, 21))
        self.label_assetgroup.setStyleSheet(u"color:rgb(153,0,76);")
        groupFont = QtGui.QFont()
        groupFont.setBold(True)
        self.label_assetgroup.setFont(groupFont)
        self.btn_assetgroup_add = QPushButton(self.main_window)
        self.btn_assetgroup_add.setObjectName(u"btn_assetgroup_add")
        self.btn_assetgroup_add.setGeometry(QRect(30, 260, 121, 21))
        self.btn_assetgroup_add.setStyleSheet(u"color: rgb(0,0,153);")
        self.btn_asset_edit = QPushButton(self.main_window)
        self.btn_asset_edit.setObjectName(u"btn_asset_edit")
        self.btn_asset_edit.setGeometry(QRect(30, 70, 121, 21))
        self.btn_asset_edit.setStyleSheet(u"color: rgb(0,0,153);")
        self.btn_asset_view = QPushButton(self.main_window)
        self.btn_asset_view.setObjectName(u"btn_asset_view")
        self.btn_asset_view.setGeometry(QRect(30, 90, 121, 21))
        self.btn_asset_view.setStyleSheet(u"color: rgb(0,0,153);")
        self.btn_logout = QPushButton(self.main_window)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setGeometry(QRect(30, 350, 121, 41))
        self.btn_logout.setAutoFillBackground(False)
        self.btn_logout.setStyleSheet(u"color: rgb(0,0,153);")
        self.btn_assettype_edit = QPushButton(self.main_window)
        self.btn_assettype_edit.setObjectName(u"btn_assettype_edit")
        self.btn_assettype_edit.setGeometry(QRect(30, 180, 121, 21))
        self.btn_assettype_edit.setStyleSheet(u"color: rgb(0,0,153);")
        self.label_assettype = QLabel(self.main_window)
        self.label_assettype.setObjectName(u"label_assettype")
        self.label_assettype.setGeometry(QRect(60, 140, 70, 21))
        self.label_assettype.setStyleSheet(u"color: rgb(153,0,76);")
        typeFont = QtGui.QFont()
        typeFont.setBold(True)
        self.label_assettype.setFont(typeFont)
        self.stackedWidget = QStackedWidget(self.main_window)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 20, 431, 381))
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 70, 341, 81))
        font1 = QFont()
        font1.setPointSize(26)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.page_home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 140, 341, 81))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.page_home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 210, 171, 81))
        self.label_3.setFont(font1)
        self.stackedWidget.addWidget(self.page_home)
        self.page_asset = QWidget()
        self.page_asset.setObjectName(u"page_asset")
        self.label_9 = QLabel(self.page_asset)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, -10, 301, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        font2.setStyleStrategy(QFont.NoAntialias)
        self.label_9.setFont(font2)
        self.label_9.setCursor(QCursor(Qt.ArrowCursor))
        self.label_9.setAutoFillBackground(False)
        self.label_9.setFrameShadow(QFrame.Sunken)
        self.scrollArea = QScrollArea(self.page_asset)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 40, 431, 301))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 412, 564))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.label_asset_id = QLabel(self.scrollAreaWidgetContents)
        self.label_asset_id.setObjectName(u"label_asset_id")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_asset_id.setFont(font3)

        self.formLayout.setWidget(
            0, QFormLayout.LabelRole, self.label_asset_id)

        self.lineEdit_asset_id = QLabel(self.scrollAreaWidgetContents)
        self.lineEdit_asset_id.setObjectName(u"lineEdit_asset_id")

        self.formLayout.setWidget(
            0, QFormLayout.FieldRole, self.lineEdit_asset_id)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_serial_no = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_serial_no.setObjectName(u"lineEdit_serial_no")

        self.formLayout.setWidget(
            1, QFormLayout.FieldRole, self.lineEdit_serial_no)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_asset_name = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_asset_name.setObjectName(u"lineEdit_asset_name")

        self.formLayout.setWidget(
            2, QFormLayout.FieldRole, self.lineEdit_asset_name)

        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_26)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_17)

        self.lineEdit_details = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_details.setObjectName(u"lineEdit_details")

        self.formLayout.setWidget(
            5, QFormLayout.FieldRole, self.lineEdit_details)

        self.label_27 = QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_27)

        self.lineEdit_asset_parend_id = QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_asset_parend_id.setObjectName(
            u"lineEdit_asset_parend_id")

        self.formLayout.setWidget(
            6, QFormLayout.FieldRole, self.lineEdit_asset_parend_id)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_asset_oem = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_asset_oem.setObjectName(u"lineEdit_asset_oem")

        self.formLayout.setWidget(
            7, QFormLayout.FieldRole, self.lineEdit_asset_oem)

        self.label_24 = QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_24)

        self.lineEdit_oem_contact = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_oem_contact.setObjectName(u"lineEdit_oem_contact")

        self.formLayout.setWidget(
            8, QFormLayout.FieldRole, self.lineEdit_oem_contact)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_oem_contact_1 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_oem_contact_1.setObjectName(u"lineEdit_oem_contact_1")

        self.formLayout.setWidget(
            9, QFormLayout.FieldRole, self.lineEdit_oem_contact_1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_asset_seller_name = QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_asset_seller_name.setObjectName(
            u"lineEdit_asset_seller_name")

        self.formLayout.setWidget(
            10, QFormLayout.FieldRole, self.lineEdit_asset_seller_name)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_20)

        self.lineEdit_seller_contact = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_seller_contact.setObjectName(u"lineEdit_seller_contact")

        self.formLayout.setWidget(
            11, QFormLayout.FieldRole, self.lineEdit_seller_contact)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_15)

        self.lineEdit_oem_email = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_oem_email.setObjectName(u"lineEdit_oem_email")

        self.formLayout.setWidget(
            12, QFormLayout.FieldRole, self.lineEdit_oem_email)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_oem_email1 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_oem_email1.setObjectName(u"lineEdit_oem_email1")

        self.formLayout.setWidget(
            13, QFormLayout.FieldRole, self.lineEdit_oem_email1)

        self.label_25 = QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_25)

        self.lineEdit_seller_email = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_seller_email.setObjectName(u"lineEdit_seller_email")

        self.formLayout.setWidget(
            14, QFormLayout.FieldRole, self.lineEdit_seller_email)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_19)

        self.dateEdit_purchasedate = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_purchasedate.setObjectName(u"dateEdit_purchasedate")

        self.formLayout.setWidget(
            15, QFormLayout.FieldRole, self.dateEdit_purchasedate)

        self.label_28 = QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_28)

        self.lineEdit_warranty_details = QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_warranty_details.setObjectName(
            u"lineEdit_warranty_details")

        self.formLayout.setWidget(
            16, QFormLayout.FieldRole, self.lineEdit_warranty_details)

        self.dateEdit_warranty_enddate = QDateEdit(
            self.scrollAreaWidgetContents)
        self.dateEdit_warranty_enddate.setObjectName(
            u"dateEdit_warranty_enddate")

        self.formLayout.setWidget(
            17, QFormLayout.FieldRole, self.dateEdit_warranty_enddate)

        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.label_21)

        self.label_23 = QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_23)

        self.lineEdit_asset_price = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_asset_price.setObjectName(u"lineEdit_asset_price")

        self.formLayout.setWidget(
            19, QFormLayout.FieldRole, self.lineEdit_asset_price)

        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 60))
        self.label_22.setFont(font3)

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.label_22)

        self.comboBox_type_asset = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_type_asset.setObjectName(u"comboBox_type_asset")

        self.formLayout.setWidget(
            3, QFormLayout.FieldRole, self.comboBox_type_asset)

        self.comboBox_group_asset = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_group_asset.setObjectName(u"comboBox_group_asset")

        self.formLayout.setWidget(
            4, QFormLayout.FieldRole, self.comboBox_group_asset)

        self.comboBox_asset_status = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_asset_status.setObjectName(u"comboBox_asset_status")

        self.formLayout.setWidget(
            18, QFormLayout.FieldRole, self.comboBox_asset_status)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btn_asset_save = QPushButton(self.page_asset)
        self.btn_asset_save.setObjectName(u"btn_asset_save")
        self.btn_asset_save.setGeometry(QRect(180, 350, 81, 31))
        self.btn_asset_save.setFont(font3)
        self.btn_asset_save.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.stackedWidget.addWidget(self.page_asset)
        self.page_asset_edit = QWidget()
        self.page_asset_edit.setObjectName(u"page_asset_edit")
        self.label_53 = QLabel(self.page_asset_edit)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(70, 60, 301, 41))
        self.label_53.setFont(font2)
        self.label_53.setCursor(QCursor(Qt.ArrowCursor))
        self.label_53.setAutoFillBackground(False)
        self.label_53.setFrameShadow(QFrame.Sunken)
        self.label_asset_view_id_edit = QLabel(self.page_asset_edit)
        self.label_asset_view_id_edit.setObjectName(
            u"label_asset_view_id_edit")
        self.label_asset_view_id_edit.setGeometry(QRect(60, 170, 121, 20))

        self.asset_view_id_edit = QComboBox(self.page_asset_edit)
        self.asset_view_id_edit.setEditable(True)
        self.asset_view_id_edit.setObjectName(u"asset_view_id_edit")
        self.asset_view_id_edit.setGeometry(QRect(250, 170, 141, 31))

        self.pushButton_assetview_find_edit = QPushButton(self.page_asset_edit)
        self.pushButton_assetview_find_edit.setObjectName(
            u"pushButton_assetview_find_edit")
        self.pushButton_assetview_find_edit.setGeometry(
            QRect(190, 270, 75, 23))
        self.stackedWidget.addWidget(self.page_asset_edit)
        self.page_asset_edit_nxt = QWidget()
        self.page_asset_edit_nxt.setObjectName(u"page_asset_edit_nxt")
        self.btn_asset_save_edit_2 = QPushButton(self.page_asset_edit_nxt)
        self.btn_asset_save_edit_2.setObjectName(u"btn_asset_save_edit_2")
        self.btn_asset_save_edit_2.setGeometry(QRect(160, 350, 81, 31))
        self.btn_asset_save_edit_2.setFont(font3)
        self.btn_asset_save_edit_2.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.scrollArea_editasset_2 = QScrollArea(self.page_asset_edit_nxt)
        self.scrollArea_editasset_2.setObjectName(u"scrollArea_editasset_2")
        self.scrollArea_editasset_2.setGeometry(QRect(0, 40, 431, 301))
        self.scrollArea_editasset_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(
            u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, -261, 412, 560))
        self.formLayout_6 = QFormLayout(self.scrollAreaWidgetContents_6)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_asset_id_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_asset_id_edit_2.setObjectName(u"label_asset_id_edit_2")
        self.label_asset_id_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            0, QFormLayout.LabelRole, self.label_asset_id_edit_2)

        self.label_srlno_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_srlno_edit_2.setObjectName(u"label_srlno_edit_2")
        self.label_srlno_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            1, QFormLayout.LabelRole, self.label_srlno_edit_2)

        self.lineEdit_srlno_edit_2 = QLineEdit(self.scrollAreaWidgetContents_6)
        self.lineEdit_srlno_edit_2.setObjectName(u"lineEdit_srlno_edit_2")

        self.formLayout_6.setWidget(
            1, QFormLayout.FieldRole, self.lineEdit_srlno_edit_2)

        self.label_assetname_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_assetname_edit_2.setObjectName(u"label_assetname_edit_2")
        self.label_assetname_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            2, QFormLayout.LabelRole, self.label_assetname_edit_2)

        self.lineEdit_asset_name_edit_2 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_asset_name_edit_2.setObjectName(
            u"lineEdit_asset_name_edit_2")

        self.formLayout_6.setWidget(
            2, QFormLayout.FieldRole, self.lineEdit_asset_name_edit_2)

        self.label_typeasset_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_typeasset_edit_2.setObjectName(u"label_typeasset_edit_2")
        self.label_typeasset_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            3, QFormLayout.LabelRole, self.label_typeasset_edit_2)

        self.label_groupasset_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_groupasset_edit_2.setObjectName(u"label_groupasset_edit_2")
        self.label_groupasset_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            4, QFormLayout.LabelRole, self.label_groupasset_edit_2)

        self.label_details_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_details_edit_2.setObjectName(u"label_details_edit_2")
        self.label_details_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            5, QFormLayout.LabelRole, self.label_details_edit_2)

        self.lineEdit_details_edit_2 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_details_edit_2.setObjectName(u"lineEdit_details_edit_2")

        self.formLayout_6.setWidget(
            5, QFormLayout.FieldRole, self.lineEdit_details_edit_2)

        self.label_parentid_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_parentid_edit_2.setObjectName(u"label_parentid_edit_2")
        self.label_parentid_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            6, QFormLayout.LabelRole, self.label_parentid_edit_2)

        self.lineEdit_asset_parend_id_edit_2 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_asset_parend_id_edit_2.setObjectName(
            u"lineEdit_asset_parend_id_edit_2")

        self.formLayout_6.setWidget(
            6, QFormLayout.FieldRole, self.lineEdit_asset_parend_id_edit_2)

        self.label_oemname_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_oemname_edit_2.setObjectName(u"label_oemname_edit_2")
        self.label_oemname_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            7, QFormLayout.LabelRole, self.label_oemname_edit_2)

        self.lineEdit_asset_oem_edit_2 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_asset_oem_edit_2.setObjectName(
            u"lineEdit_asset_oem_edit_2")

        self.formLayout_6.setWidget(
            7, QFormLayout.FieldRole, self.lineEdit_asset_oem_edit_2)

        self.label_oemcontactno_edit_2 = QLabel(
            self.scrollAreaWidgetContents_6)
        self.label_oemcontactno_edit_2.setObjectName(
            u"label_oemcontactno_edit_2")
        self.label_oemcontactno_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            8, QFormLayout.LabelRole, self.label_oemcontactno_edit_2)

        self.lineEdit_oem_contact_edit_3 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_oem_contact_edit_3.setObjectName(
            u"lineEdit_oem_contact_edit_3")

        self.formLayout_6.setWidget(
            8, QFormLayout.FieldRole, self.lineEdit_oem_contact_edit_3)

        self.label_oemcontact_esk1_edit_2 = QLabel(
            self.scrollAreaWidgetContents_6)
        self.label_oemcontact_esk1_edit_2.setObjectName(
            u"label_oemcontact_esk1_edit_2")
        self.label_oemcontact_esk1_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            9, QFormLayout.LabelRole, self.label_oemcontact_esk1_edit_2)

        self.lineEdit_oem_contact_edit_4 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_oem_contact_edit_4.setObjectName(
            u"lineEdit_oem_contact_edit_4")

        self.formLayout_6.setWidget(
            9, QFormLayout.FieldRole, self.lineEdit_oem_contact_edit_4)

        self.label_sellername_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_sellername_edit_2.setObjectName(u"label_sellername_edit_2")
        self.label_sellername_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            10, QFormLayout.LabelRole, self.label_sellername_edit_2)

        self.lineEdit_asset_seller_name_edit_2 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_asset_seller_name_edit_2.setObjectName(
            u"lineEdit_asset_seller_name_edit_2")

        self.formLayout_6.setWidget(
            10, QFormLayout.FieldRole, self.lineEdit_asset_seller_name_edit_2)

        self.label_sellercontactno_edit_2 = QLabel(
            self.scrollAreaWidgetContents_6)
        self.label_sellercontactno_edit_2.setObjectName(
            u"label_sellercontactno_edit_2")
        self.label_sellercontactno_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            11, QFormLayout.LabelRole, self.label_sellercontactno_edit_2)

        self.lineEdit_seller_contact_edit_2 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_seller_contact_edit_2.setObjectName(
            u"lineEdit_seller_contact_edit_2")

        self.formLayout_6.setWidget(
            11, QFormLayout.FieldRole, self.lineEdit_seller_contact_edit_2)

        self.label_oememail_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_oememail_edit_2.setObjectName(u"label_oememail_edit_2")
        self.label_oememail_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            12, QFormLayout.LabelRole, self.label_oememail_edit_2)

        self.lineEdit_oem_email_edit_2 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_oem_email_edit_2.setObjectName(
            u"lineEdit_oem_email_edit_2")

        self.formLayout_6.setWidget(
            12, QFormLayout.FieldRole, self.lineEdit_oem_email_edit_2)

        self.label_oememailesk1_edit_2 = QLabel(
            self.scrollAreaWidgetContents_6)
        self.label_oememailesk1_edit_2.setObjectName(
            u"label_oememailesk1_edit_2")
        self.label_oememailesk1_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            13, QFormLayout.LabelRole, self.label_oememailesk1_edit_2)

        self.lineEdit_oem_email1_edit_2 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_oem_email1_edit_2.setObjectName(
            u"lineEdit_oem_email1_edit_2")

        self.formLayout_6.setWidget(
            13, QFormLayout.FieldRole, self.lineEdit_oem_email1_edit_2)

        self.label_selleremail_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_selleremail_edit_2.setObjectName(
            u"label_selleremail_edit_2")
        self.label_selleremail_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            14, QFormLayout.LabelRole, self.label_selleremail_edit_2)

        self.lineEdit_seller_email_edit_2 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_seller_email_edit_2.setObjectName(
            u"lineEdit_seller_email_edit_2")

        self.formLayout_6.setWidget(
            14, QFormLayout.FieldRole, self.lineEdit_seller_email_edit_2)

        self.label_Purchasedate_edit_2 = QLabel(
            self.scrollAreaWidgetContents_6)
        self.label_Purchasedate_edit_2.setObjectName(
            u"label_Purchasedate_edit_2")
        self.label_Purchasedate_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            15, QFormLayout.LabelRole, self.label_Purchasedate_edit_2)

        self.dateEdit_purchasedate_edit_2 = QDateEdit(
            self.scrollAreaWidgetContents_6)
        self.dateEdit_purchasedate_edit_2.setObjectName(
            u"dateEdit_purchasedate_edit_2")

        self.formLayout_6.setWidget(
            15, QFormLayout.FieldRole, self.dateEdit_purchasedate_edit_2)

        self.label_warrentydetails_edit_2 = QLabel(
            self.scrollAreaWidgetContents_6)
        self.label_warrentydetails_edit_2.setObjectName(
            u"label_warrentydetails_edit_2")
        self.label_warrentydetails_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            16, QFormLayout.LabelRole, self.label_warrentydetails_edit_2)

        self.lineEdit_warranty_details_edit_2 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_warranty_details_edit_2.setObjectName(
            u"lineEdit_warranty_details_edit_2")

        self.formLayout_6.setWidget(
            16, QFormLayout.FieldRole, self.lineEdit_warranty_details_edit_2)

        self.dateEdit_warranty_enddate_edit_2 = QDateEdit(
            self.scrollAreaWidgetContents_6)
        self.dateEdit_warranty_enddate_edit_2.setObjectName(
            u"dateEdit_warranty_enddate_edit_2")

        self.formLayout_6.setWidget(
            17, QFormLayout.FieldRole, self.dateEdit_warranty_enddate_edit_2)

        self.label_assetstatus_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_assetstatus_edit_2.setObjectName(
            u"label_assetstatus_edit_2")
        self.label_assetstatus_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            18, QFormLayout.LabelRole, self.label_assetstatus_edit_2)

        self.label_price_edit_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_price_edit_2.setObjectName(u"label_price_edit_2")
        self.label_price_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            19, QFormLayout.LabelRole, self.label_price_edit_2)

        self.lineEdit_asset_price_edit_2 = QLineEdit(
            self.scrollAreaWidgetContents_6)
        self.lineEdit_asset_price_edit_2.setObjectName(
            u"lineEdit_asset_price_edit_2")

        self.formLayout_6.setWidget(
            19, QFormLayout.FieldRole, self.lineEdit_asset_price_edit_2)

        self.comboBox_type_asset_edit_2 = QComboBox(
            self.scrollAreaWidgetContents_6)
        self.comboBox_type_asset_edit_2.setObjectName(
            u"comboBox_type_asset_edit_2")

        self.formLayout_6.setWidget(
            3, QFormLayout.FieldRole, self.comboBox_type_asset_edit_2)

        self.comboBox_group_asset_edit_2 = QComboBox(
            self.scrollAreaWidgetContents_6)
        self.comboBox_group_asset_edit_2.setObjectName(
            u"comboBox_group_asset_edit_2")

        self.formLayout_6.setWidget(
            4, QFormLayout.FieldRole, self.comboBox_group_asset_edit_2)

        self.comboBox_asset_status_edit_2 = QComboBox(
            self.scrollAreaWidgetContents_6)
        self.comboBox_asset_status_edit_2.setObjectName(
            u"comboBox_asset_status_edit_2")

        self.formLayout_6.setWidget(
            18, QFormLayout.FieldRole, self.comboBox_asset_status_edit_2)

        self.label_warrentyenddate_edit_2 = QLabel(
            self.scrollAreaWidgetContents_6)
        self.label_warrentyenddate_edit_2.setObjectName(
            u"label_warrentyenddate_edit_2")
        self.label_warrentyenddate_edit_2.setMinimumSize(QSize(0, 60))
        self.label_warrentyenddate_edit_2.setFont(font3)

        self.formLayout_6.setWidget(
            17, QFormLayout.LabelRole, self.label_warrentyenddate_edit_2)

        self.label_Asset_id_edit_input = QLabel(
            self.scrollAreaWidgetContents_6)
        self.label_Asset_id_edit_input.setObjectName(
            u"label_Asset_id_edit_input")

        self.formLayout_6.setWidget(
            0, QFormLayout.FieldRole, self.label_Asset_id_edit_input)

        self.scrollArea_editasset_2.setWidget(self.scrollAreaWidgetContents_6)
        self.label_52 = QLabel(self.page_asset_edit_nxt)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(60, 0, 301, 31))
        self.label_52.setFont(font2)
        self.label_52.setCursor(QCursor(Qt.ArrowCursor))
        self.label_52.setAutoFillBackground(False)
        self.label_52.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.page_asset_edit_nxt)
        self.page_assetview = QWidget()
        self.page_assetview.setObjectName(u"page_assetview")
        self.label_asset_view_id = QLabel(self.page_assetview)
        self.label_asset_view_id.setObjectName(u"label_asset_view_id")
        self.label_asset_view_id.setGeometry(QRect(60, 130, 121, 20))
        self.pushButton_assetview_find = QPushButton(self.page_assetview)
        self.pushButton_assetview_find.setObjectName(
            u"pushButton_assetview_find")
        self.pushButton_assetview_find.setGeometry(QRect(170, 250, 81, 31))
        self.asset_view_id = QComboBox(self.page_assetview)
        self.asset_view_id.setEditable(True)
        self.asset_view_id.setObjectName(u"asset_view_id")
        self.asset_view_id.setGeometry(QRect(230, 130, 141, 31))
        self.label_54 = QLabel(self.page_assetview)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(40, 30, 331, 41))
        self.label_54.setFont(font2)
        self.label_54.setCursor(QCursor(Qt.ArrowCursor))
        self.label_54.setAutoFillBackground(False)
        self.label_54.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.page_assetview)
        self.page_assetview_nxt = QWidget()
        self.page_assetview_nxt.setObjectName(u"page_assetview_nxt")
        self.scrollArea_2 = QScrollArea(self.page_assetview_nxt)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(10, 50, 421, 331))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(
            u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 402, 496))
        self.formLayout_2 = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_assetview_id_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_assetview_id_2.setObjectName(u"label_assetview_id_2")
        self.label_assetview_id_2.setFont(font3)

        self.formLayout_2.setWidget(
            0, QFormLayout.LabelRole, self.label_assetview_id_2)

        self.label_assetview_srlno = QLabel(self.scrollAreaWidgetContents_2)
        self.label_assetview_srlno.setObjectName(u"label_assetview_srlno")
        self.label_assetview_srlno.setFont(font3)

        self.formLayout_2.setWidget(
            1, QFormLayout.LabelRole, self.label_assetview_srlno)

        self.label_assetview_assetname = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_assetname.setObjectName(
            u"label_assetview_assetname")
        self.label_assetview_assetname.setFont(font3)

        self.formLayout_2.setWidget(
            2, QFormLayout.LabelRole, self.label_assetview_assetname)

        self.label_assetview_type = QLabel(self.scrollAreaWidgetContents_2)
        self.label_assetview_type.setObjectName(u"label_assetview_type")
        self.label_assetview_type.setFont(font3)

        self.formLayout_2.setWidget(
            3, QFormLayout.LabelRole, self.label_assetview_type)

        self.label_assetview_group = QLabel(self.scrollAreaWidgetContents_2)
        self.label_assetview_group.setObjectName(u"label_assetview_group")
        self.label_assetview_group.setFont(font3)

        self.formLayout_2.setWidget(
            4, QFormLayout.LabelRole, self.label_assetview_group)

        self.label_assetview_details = QLabel(self.scrollAreaWidgetContents_2)
        self.label_assetview_details.setObjectName(u"label_assetview_details")
        self.label_assetview_details.setFont(font3)

        self.formLayout_2.setWidget(
            5, QFormLayout.LabelRole, self.label_assetview_details)

        self.label_assetview_assetparentid = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_assetparentid.setObjectName(
            u"label_assetview_assetparentid")
        self.label_assetview_assetparentid.setFont(font3)

        self.formLayout_2.setWidget(
            6, QFormLayout.LabelRole, self.label_assetview_assetparentid)

        self.label_assetview_oemname = QLabel(self.scrollAreaWidgetContents_2)
        self.label_assetview_oemname.setObjectName(u"label_assetview_oemname")
        self.label_assetview_oemname.setFont(font3)

        self.formLayout_2.setWidget(
            7, QFormLayout.LabelRole, self.label_assetview_oemname)

        self.label_assetview_oemcontactno = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_oemcontactno.setObjectName(
            u"label_assetview_oemcontactno")
        self.label_assetview_oemcontactno.setFont(font3)

        self.formLayout_2.setWidget(
            8, QFormLayout.LabelRole, self.label_assetview_oemcontactno)

        self.label_assetview_oemcontactnoesk1 = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_oemcontactnoesk1.setObjectName(
            u"label_assetview_oemcontactnoesk1")
        self.label_assetview_oemcontactnoesk1.setFont(font3)

        self.formLayout_2.setWidget(
            9, QFormLayout.LabelRole, self.label_assetview_oemcontactnoesk1)

        self.label_assetview_sellername = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_sellername.setObjectName(
            u"label_assetview_sellername")
        self.label_assetview_sellername.setFont(font3)

        self.formLayout_2.setWidget(
            10, QFormLayout.LabelRole, self.label_assetview_sellername)

        self.label_assetview_sellerno = QLabel(self.scrollAreaWidgetContents_2)
        self.label_assetview_sellerno.setObjectName(
            u"label_assetview_sellerno")
        self.label_assetview_sellerno.setFont(font3)

        self.formLayout_2.setWidget(
            11, QFormLayout.LabelRole, self.label_assetview_sellerno)

        self.label_assetview_oememail = QLabel(self.scrollAreaWidgetContents_2)
        self.label_assetview_oememail.setObjectName(
            u"label_assetview_oememail")
        self.label_assetview_oememail.setFont(font3)

        self.formLayout_2.setWidget(
            12, QFormLayout.LabelRole, self.label_assetview_oememail)

        self.label_assetview_oememailesk1 = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_oememailesk1.setObjectName(
            u"label_assetview_oememailesk1")
        self.label_assetview_oememailesk1.setFont(font3)

        self.formLayout_2.setWidget(
            13, QFormLayout.LabelRole, self.label_assetview_oememailesk1)

        self.label_assetview_selleremail = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_selleremail.setObjectName(
            u"label_assetview_selleremail")
        self.label_assetview_selleremail.setFont(font3)

        self.formLayout_2.setWidget(
            14, QFormLayout.LabelRole, self.label_assetview_selleremail)

        self.label_assetview_purchasedate = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_purchasedate.setObjectName(
            u"label_assetview_purchasedate")
        self.label_assetview_purchasedate.setFont(font3)

        self.formLayout_2.setWidget(
            15, QFormLayout.LabelRole, self.label_assetview_purchasedate)

        self.label_assetview_Warrentydetails = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_Warrentydetails.setObjectName(
            u"label_assetview_Warrentydetails")
        self.label_assetview_Warrentydetails.setFont(font3)

        self.formLayout_2.setWidget(
            16, QFormLayout.LabelRole, self.label_assetview_Warrentydetails)

        self.label_assetview_status = QLabel(self.scrollAreaWidgetContents_2)
        self.label_assetview_status.setObjectName(u"label_assetview_status")
        self.label_assetview_status.setFont(font3)

        self.formLayout_2.setWidget(
            18, QFormLayout.LabelRole, self.label_assetview_status)

        self.label_assetview_price = QLabel(self.scrollAreaWidgetContents_2)
        self.label_assetview_price.setObjectName(u"label_assetview_price")
        self.label_assetview_price.setFont(font3)

        self.formLayout_2.setWidget(
            19, QFormLayout.LabelRole, self.label_assetview_price)

        self.label_assetview_warrentyenddate = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_warrentyenddate.setObjectName(
            u"label_assetview_warrentyenddate")
        self.label_assetview_warrentyenddate.setMinimumSize(QSize(0, 60))
        self.label_assetview_warrentyenddate.setFont(font3)

        self.formLayout_2.setWidget(
            17, QFormLayout.LabelRole, self.label_assetview_warrentyenddate)

        self.label_assetview_id_2_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_id_2_input.setObjectName(
            u"label_assetview_id_2_input")

        self.formLayout_2.setWidget(
            0, QFormLayout.FieldRole, self.label_assetview_id_2_input)

        self.label_assetview_srlno_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_srlno_input.setObjectName(
            u"label_assetview_srlno_input")

        self.formLayout_2.setWidget(
            1, QFormLayout.FieldRole, self.label_assetview_srlno_input)

        self.label_assetview_assetname_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_assetname_input.setObjectName(
            u"label_assetview_assetname_input")

        self.formLayout_2.setWidget(
            2, QFormLayout.FieldRole, self.label_assetview_assetname_input)

        self.label_assetview_type_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_type_input.setObjectName(
            u"label_assetview_type_input")

        self.formLayout_2.setWidget(
            3, QFormLayout.FieldRole, self.label_assetview_type_input)

        self.label_assetview_group_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_group_input.setObjectName(
            u"label_assetview_group_input")

        self.formLayout_2.setWidget(
            4, QFormLayout.FieldRole, self.label_assetview_group_input)

        self.label_assetview_details_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_details_input.setObjectName(
            u"label_assetview_details_input")

        self.formLayout_2.setWidget(
            5, QFormLayout.FieldRole, self.label_assetview_details_input)

        self.label_assetview_assetparentid_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_assetparentid_input.setObjectName(
            u"label_assetview_assetparentid_input")

        self.formLayout_2.setWidget(
            6, QFormLayout.FieldRole, self.label_assetview_assetparentid_input)

        self.label_assetview_oemname_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_oemname_input.setObjectName(
            u"label_assetview_oemname_input")

        self.formLayout_2.setWidget(
            7, QFormLayout.FieldRole, self.label_assetview_oemname_input)

        self.label_assetview_oemcontactno_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_oemcontactno_input.setObjectName(
            u"label_assetview_oemcontactno_input")

        self.formLayout_2.setWidget(
            8, QFormLayout.FieldRole, self.label_assetview_oemcontactno_input)

        self.label_assetview_oemcontactnoesk1_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_oemcontactnoesk1_input.setObjectName(
            u"label_assetview_oemcontactnoesk1_input")

        self.formLayout_2.setWidget(
            9, QFormLayout.FieldRole, self.label_assetview_oemcontactnoesk1_input)

        self.label_assetview_sellername_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_sellername_input.setObjectName(
            u"label_assetview_sellername_input")

        self.formLayout_2.setWidget(
            10, QFormLayout.FieldRole, self.label_assetview_sellername_input)

        self.label_assetview_sellerno_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_sellerno_input.setObjectName(
            u"label_assetview_sellerno_input")

        self.formLayout_2.setWidget(
            11, QFormLayout.FieldRole, self.label_assetview_sellerno_input)

        self.label_assetview_oememail_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_oememail_input.setObjectName(
            u"label_assetview_oememail_input")

        self.formLayout_2.setWidget(
            12, QFormLayout.FieldRole, self.label_assetview_oememail_input)

        self.label_assetview_oememailesk1_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_oememailesk1_input.setObjectName(
            u"label_assetview_oememailesk1_input")

        self.formLayout_2.setWidget(
            13, QFormLayout.FieldRole, self.label_assetview_oememailesk1_input)

        self.label_assetview_selleremail_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_selleremail_input.setObjectName(
            u"label_assetview_selleremail_input")

        self.formLayout_2.setWidget(
            14, QFormLayout.FieldRole, self.label_assetview_selleremail_input)

        self.label_assetview_purchasedate_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_purchasedate_input.setObjectName(
            u"label_assetview_purchasedate_input")

        self.formLayout_2.setWidget(
            15, QFormLayout.FieldRole, self.label_assetview_purchasedate_input)

        self.label_assetview_Warrentydetails_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_Warrentydetails_input.setObjectName(
            u"label_assetview_Warrentydetails_input")

        self.formLayout_2.setWidget(
            16, QFormLayout.FieldRole, self.label_assetview_Warrentydetails_input)

        self.label_assetview_warrentyenddate_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_warrentyenddate_input.setObjectName(
            u"label_assetview_warrentyenddate_input")

        self.formLayout_2.setWidget(
            17, QFormLayout.FieldRole, self.label_assetview_warrentyenddate_input)

        self.label_assetview_status_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_status_input.setObjectName(
            u"label_assetview_status_input")

        self.formLayout_2.setWidget(
            18, QFormLayout.FieldRole, self.label_assetview_status_input)

        self.label_assetview_price_input = QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_assetview_price_input.setObjectName(
            u"label_assetview_price_input")

        self.formLayout_2.setWidget(
            19, QFormLayout.FieldRole, self.label_assetview_price_input)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_55 = QLabel(self.page_assetview_nxt)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(40, 0, 331, 41))
        self.label_55.setFont(font2)
        self.label_55.setCursor(QCursor(Qt.ArrowCursor))
        self.label_55.setAutoFillBackground(False)
        self.label_55.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.page_assetview_nxt)

        self.page_asset_bulk = QtWidgets.QWidget()
        self.page_asset_bulk.setObjectName("page_asset_bulk")
        self.label_asset_view_id_edit_2 = QtWidgets.QLabel(
            self.page_asset_bulk)
        self.label_asset_view_id_edit_2.setGeometry(
            QtCore.QRect(50, 170, 121, 20))
        self.label_asset_view_id_edit_2.setObjectName(
            "label_asset_view_id_edit_2")
        self.pushButton_asset_bulk = QtWidgets.QPushButton(
            self.page_asset_bulk)
        self.pushButton_asset_bulk.setGeometry(QtCore.QRect(180, 270, 75, 23))
        self.pushButton_asset_bulk.setObjectName("pushButton_asset_bulk")
        self.label_56 = QtWidgets.QLabel(self.page_asset_bulk)
        self.label_56.setGeometry(QtCore.QRect(60, 60, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.label_56.setFont(font)
        self.label_56.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_56.setAutoFillBackground(False)
        self.label_56.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_56.setObjectName("label_56")
        self.asset_view_id_edit_bulk = QtWidgets.QComboBox(
            self.page_asset_bulk)
        self.asset_view_id_edit_bulk.setGeometry(
            QtCore.QRect(210, 170, 161, 31))
        self.asset_view_id_edit_bulk.setObjectName("asset_view_id_edit_bulk")
        self.stackedWidget.addWidget(self.page_asset_bulk)
        self.page_asset_bulk_nxt = QtWidgets.QWidget()
        self.page_asset_bulk_nxt.setObjectName("page_asset_bulk_nxt")
        self.btn_asset_save_edit_3 = QtWidgets.QPushButton(
            self.page_asset_bulk_nxt)
        self.btn_asset_save_edit_3.setGeometry(QtCore.QRect(160, 350, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_asset_save_edit_3.setFont(font)
        self.btn_asset_save_edit_3.setStyleSheet("color: rgb(47, 175, 255);")
        self.btn_asset_save_edit_3.setObjectName("btn_asset_save_edit_3")
        self.label_57 = QtWidgets.QLabel(self.page_asset_bulk_nxt)
        self.label_57.setGeometry(QtCore.QRect(60, 0, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.label_57.setFont(font)
        self.label_57.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_57.setAutoFillBackground(False)
        self.label_57.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_57.setObjectName("label_57")
        self.scrollArea_editasset_3 = QtWidgets.QScrollArea(
            self.page_asset_bulk_nxt)
        self.scrollArea_editasset_3.setGeometry(QtCore.QRect(0, 40, 431, 301))
        self.scrollArea_editasset_3.setWidgetResizable(True)
        self.scrollArea_editasset_3.setObjectName("scrollArea_editasset_3")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(
            QtCore.QRect(0, -261, 412, 560))
        self.scrollAreaWidgetContents_9.setObjectName(
            "scrollAreaWidgetContents_9")
        self.formLayout_9 = QtWidgets.QFormLayout(
            self.scrollAreaWidgetContents_9)
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_asset_id_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_asset_id_edit_5.setFont(font)
        self.label_asset_id_edit_5.setObjectName("label_asset_id_edit_5")
        self.formLayout_9.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_asset_id_edit_5)
        self.label_srlno_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_srlno_edit_5.setFont(font)
        self.label_srlno_edit_5.setObjectName("label_srlno_edit_5")
        self.formLayout_9.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_srlno_edit_5)
        self.lineEdit_srlno_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_srlno_edit_bulk.setObjectName("lineEdit_srlno_edit_bulk")
        self.formLayout_9.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_srlno_edit_bulk)
        self.label_assetname_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_assetname_edit_5.setFont(font)
        self.label_assetname_edit_5.setObjectName("label_assetname_edit_5")
        self.formLayout_9.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_assetname_edit_5)
        self.lineEdit_asset_name_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_asset_name_edit_bulk.setObjectName(
            "lineEdit_asset_name_edit_bulk")
        self.formLayout_9.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_asset_name_edit_bulk)
        self.label_typeasset_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_typeasset_edit_5.setFont(font)
        self.label_typeasset_edit_5.setObjectName("label_typeasset_edit_5")
        self.formLayout_9.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_typeasset_edit_5)
        self.label_groupasset_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_groupasset_edit_5.setFont(font)
        self.label_groupasset_edit_5.setObjectName("label_groupasset_edit_5")
        self.formLayout_9.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_groupasset_edit_5)
        self.label_details_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_details_edit_5.setFont(font)
        self.label_details_edit_5.setObjectName("label_details_edit_5")
        self.formLayout_9.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.label_details_edit_5)
        self.lineEdit_details_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_details_edit_bulk.setObjectName(
            "lineEdit_details_edit_bulk")
        self.formLayout_9.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_details_edit_bulk)
        self.label_parentid_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_parentid_edit_5.setFont(font)
        self.label_parentid_edit_5.setObjectName("label_parentid_edit_5")
        self.formLayout_9.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.label_parentid_edit_5)
        self.lineEdit_asset_parend_id_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_asset_parend_id_edit_bulk.setObjectName(
            "lineEdit_asset_parend_id_edit_bulk")
        self.formLayout_9.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_asset_parend_id_edit_bulk)
        self.label_oemname_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_oemname_edit_5.setFont(font)
        self.label_oemname_edit_5.setObjectName("label_oemname_edit_5")
        self.formLayout_9.setWidget(
            7, QtWidgets.QFormLayout.LabelRole, self.label_oemname_edit_5)
        self.lineEdit_asset_oem_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_asset_oem_edit_bulk.setObjectName(
            "lineEdit_asset_oem_edit_bulk")
        self.formLayout_9.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_asset_oem_edit_bulk)
        self.label_oemcontactno_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_oemcontactno_edit_5.setFont(font)
        self.label_oemcontactno_edit_5.setObjectName(
            "label_oemcontactno_edit_5")
        self.formLayout_9.setWidget(
            8, QtWidgets.QFormLayout.LabelRole, self.label_oemcontactno_edit_5)
        self.lineEdit_oem_contact_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_oem_contact_edit_bulk.setObjectName(
            "lineEdit_oem_contact_edit_bulk")
        self.formLayout_9.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_oem_contact_edit_bulk)
        self.label_oemcontact_esk1_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_oemcontact_esk1_edit_5.setFont(font)
        self.label_oemcontact_esk1_edit_5.setObjectName(
            "label_oemcontact_esk1_edit_5")
        self.formLayout_9.setWidget(
            9, QtWidgets.QFormLayout.LabelRole, self.label_oemcontact_esk1_edit_5)
        self.lineEdit_oem_contact_edit_2_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_oem_contact_edit_2_bulk.setObjectName(
            "lineEdit_oem_contact_edit_2_bulk")
        self.formLayout_9.setWidget(
            9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_oem_contact_edit_2_bulk)
        self.label_sellername_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_sellername_edit_5.setFont(font)
        self.label_sellername_edit_5.setObjectName("label_sellername_edit_5")
        self.formLayout_9.setWidget(
            10, QtWidgets.QFormLayout.LabelRole, self.label_sellername_edit_5)
        self.lineEdit_asset_seller_name_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_asset_seller_name_edit_bulk.setObjectName(
            "lineEdit_asset_seller_name_edit_bulk")
        self.formLayout_9.setWidget(
            10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_asset_seller_name_edit_bulk)
        self.label_sellercontactno_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_sellercontactno_edit_5.setFont(font)
        self.label_sellercontactno_edit_5.setObjectName(
            "label_sellercontactno_edit_5")
        self.formLayout_9.setWidget(
            11, QtWidgets.QFormLayout.LabelRole, self.label_sellercontactno_edit_5)
        self.lineEdit_seller_contact_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_seller_contact_edit_bulk.setObjectName(
            "lineEdit_seller_contact_edit_bulk")
        self.formLayout_9.setWidget(
            11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_seller_contact_edit_bulk)
        self.label_oememail_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_oememail_edit_5.setFont(font)
        self.label_oememail_edit_5.setObjectName("label_oememail_edit_5")
        self.formLayout_9.setWidget(
            12, QtWidgets.QFormLayout.LabelRole, self.label_oememail_edit_5)
        self.lineEdit_oem_email_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_oem_email_edit_bulk.setObjectName(
            "lineEdit_oem_email_edit_bulk")
        self.formLayout_9.setWidget(
            12, QtWidgets.QFormLayout.FieldRole, self.lineEdit_oem_email_edit_bulk)
        self.label_oememailesk1_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_oememailesk1_edit_5.setFont(font)
        self.label_oememailesk1_edit_5.setObjectName(
            "label_oememailesk1_edit_5")
        self.formLayout_9.setWidget(
            13, QtWidgets.QFormLayout.LabelRole, self.label_oememailesk1_edit_5)
        self.lineEdit_oem_email1_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_oem_email1_edit_bulk.setObjectName(
            "lineEdit_oem_email1_edit_bulk")
        self.formLayout_9.setWidget(
            13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_oem_email1_edit_bulk)
        self.label_selleremail_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_selleremail_edit_5.setFont(font)
        self.label_selleremail_edit_5.setObjectName("label_selleremail_edit_5")
        self.formLayout_9.setWidget(
            14, QtWidgets.QFormLayout.LabelRole, self.label_selleremail_edit_5)
        self.lineEdit_seller_email_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_seller_email_edit_bulk.setObjectName(
            "lineEdit_seller_email_edit_bulk")
        self.formLayout_9.setWidget(
            14, QtWidgets.QFormLayout.FieldRole, self.lineEdit_seller_email_edit_bulk)
        self.label_Purchasedate_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Purchasedate_edit_5.setFont(font)
        self.label_Purchasedate_edit_5.setObjectName(
            "label_Purchasedate_edit_5")
        self.formLayout_9.setWidget(
            15, QtWidgets.QFormLayout.LabelRole, self.label_Purchasedate_edit_5)
        self.dateEdit_purchasedate_edit_bulk = QtWidgets.QDateEdit(
            self.scrollAreaWidgetContents_9)
        self.dateEdit_purchasedate_edit_bulk.setObjectName(
            "dateEdit_purchasedate_edit_bulk")
        self.formLayout_9.setWidget(
            15, QtWidgets.QFormLayout.FieldRole, self.dateEdit_purchasedate_edit_bulk)
        self.label_warrentydetails_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_warrentydetails_edit_5.setFont(font)
        self.label_warrentydetails_edit_5.setObjectName(
            "label_warrentydetails_edit_5")
        self.formLayout_9.setWidget(
            16, QtWidgets.QFormLayout.LabelRole, self.label_warrentydetails_edit_5)
        self.lineEdit_warranty_details_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_warranty_details_edit_bulk.setObjectName(
            "lineEdit_warranty_details_edit_bulk")
        self.formLayout_9.setWidget(
            16, QtWidgets.QFormLayout.FieldRole, self.lineEdit_warranty_details_edit_bulk)
        self.dateEdit_warranty_enddate_edit_bulk = QtWidgets.QDateEdit(
            self.scrollAreaWidgetContents_9)
        self.dateEdit_warranty_enddate_edit_bulk.setObjectName(
            "dateEdit_warranty_enddate_edit_bulk")
        self.formLayout_9.setWidget(
            17, QtWidgets.QFormLayout.FieldRole, self.dateEdit_warranty_enddate_edit_bulk)
        self.label_assetstatus_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_assetstatus_edit_5.setFont(font)
        self.label_assetstatus_edit_5.setObjectName("label_assetstatus_edit_5")
        self.formLayout_9.setWidget(
            18, QtWidgets.QFormLayout.LabelRole, self.label_assetstatus_edit_5)
        self.label_price_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_price_edit_5.setFont(font)
        self.label_price_edit_5.setObjectName("label_price_edit_5")
        self.formLayout_9.setWidget(
            19, QtWidgets.QFormLayout.LabelRole, self.label_price_edit_5)
        self.lineEdit_asset_price_edit_bulk = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_9)
        self.lineEdit_asset_price_edit_bulk.setObjectName(
            "lineEdit_asset_price_edit_bulk")
        self.formLayout_9.setWidget(
            19, QtWidgets.QFormLayout.FieldRole, self.lineEdit_asset_price_edit_bulk)
        self.comboBox_type_asset_edit_bulk = QtWidgets.QComboBox(
            self.scrollAreaWidgetContents_9)
        self.comboBox_type_asset_edit_bulk.setObjectName(
            "comboBox_type_asset_edit_bulk")
        self.formLayout_9.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.comboBox_type_asset_edit_bulk)
        self.comboBox_group_asset_edit_bulk = QtWidgets.QComboBox(
            self.scrollAreaWidgetContents_9)
        self.comboBox_group_asset_edit_bulk.setObjectName(
            "comboBox_group_asset_edit_bulk")
        self.formLayout_9.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.comboBox_group_asset_edit_bulk)
        self.comboBox_asset_status_edit_bulk = QtWidgets.QComboBox(
            self.scrollAreaWidgetContents_9)
        self.comboBox_asset_status_edit_bulk.setObjectName(
            "comboBox_asset_status_edit_bulk")
        self.formLayout_9.setWidget(
            18, QtWidgets.QFormLayout.FieldRole, self.comboBox_asset_status_edit_bulk)
        self.label_warrentyenddate_edit_5 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        self.label_warrentyenddate_edit_5.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_warrentyenddate_edit_5.setFont(font)
        self.label_warrentyenddate_edit_5.setObjectName(
            "label_warrentyenddate_edit_5")
        self.formLayout_9.setWidget(
            17, QtWidgets.QFormLayout.LabelRole, self.label_warrentyenddate_edit_5)
        self.label_Asset_id_edit_input_bulk = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_9)
        self.label_Asset_id_edit_input_bulk.setObjectName(
            "label_Asset_id_edit_input_bulk")
        self.formLayout_9.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_Asset_id_edit_input_bulk)
        self.scrollArea_editasset_3.setWidget(self.scrollAreaWidgetContents_9)
        self.stackedWidget.addWidget(self.page_asset_bulk_nxt)

        self.page_assettype = QWidget()
        self.page_assettype.setObjectName(u"page_assettype")
        self.label_5 = QLabel(self.page_assettype)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 90, 301, 41))
        self.label_5.setFont(font2)
        self.label_5.setCursor(QCursor(Qt.ArrowCursor))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setFrameShadow(QFrame.Sunken)
        self.label_8 = QLabel(self.page_assettype)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 170, 121, 21))
        self.label_8.setFont(font3)
        self.lineEdit_assettype_td = QLineEdit(self.page_assettype)
        self.lineEdit_assettype_td.setObjectName(u"lineEdit_assettype_td")
        self.lineEdit_assettype_td.setGeometry(QRect(230, 170, 131, 21))
        self.pushButton_assettype_save = QPushButton(self.page_assettype)
        self.pushButton_assettype_save.setObjectName(
            u"pushButton_assettype_save")
        self.pushButton_assettype_save.setGeometry(QRect(160, 240, 111, 31))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.pushButton_assettype_save.setFont(font4)
        self.pushButton_assettype_save.setStyleSheet(
            u"color: rgb(47, 175, 255);")
        self.stackedWidget.addWidget(self.page_assettype)
        self.page_assettype_edit = QWidget()
        self.page_assettype_edit.setObjectName(u"page_assettype_edit")
        self.label_type_id_edit = QLabel(self.page_assettype_edit)
        self.label_type_id_edit.setObjectName(u"label_type_id_edit")
        self.label_type_id_edit.setGeometry(QRect(50, 170, 121, 21))
        self.label_type_id_edit.setFont(font3)
        self.label_32 = QLabel(self.page_assettype_edit)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(70, 50, 291, 41))
        self.label_32.setFont(font2)
        self.label_32.setCursor(QCursor(Qt.ArrowCursor))
        self.label_32.setAutoFillBackground(False)
        self.label_32.setFrameShadow(QFrame.Sunken)
        self.pushButton_assetview_find_edittype = QPushButton(
            self.page_assettype_edit)
        self.pushButton_assetview_find_edittype.setObjectName(
            u"pushButton_assetview_find_edittype")
        self.pushButton_assetview_find_edittype.setGeometry(
            QRect(170, 260, 75, 23))
        self.lineEdit_assettype_td_edit = QComboBox(self.page_assettype_edit)
        self.lineEdit_assettype_td_edit.setEditable(True)
        self.lineEdit_assettype_td_edit.setObjectName(
            u"lineEdit_assettype_td_edit")
        self.lineEdit_assettype_td_edit.setGeometry(QRect(250, 170, 131, 21))
        self.stackedWidget.addWidget(self.page_assettype_edit)
        self.page_assettype_edit_nxt = QWidget()
        self.page_assettype_edit_nxt.setObjectName(u"page_assettype_edit_nxt")
        self.label_30 = QLabel(self.page_assettype_edit_nxt)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(70, 50, 291, 41))
        self.label_30.setFont(font2)
        self.label_30.setCursor(QCursor(Qt.ArrowCursor))
        self.label_30.setAutoFillBackground(False)
        self.label_30.setFrameShadow(QFrame.Sunken)
        self.pushButton_assettype_save_edit = QPushButton(
            self.page_assettype_edit_nxt)
        self.pushButton_assettype_save_edit.setObjectName(
            u"pushButton_assettype_save_edit")
        self.pushButton_assettype_save_edit.setGeometry(
            QRect(160, 290, 111, 31))
        self.pushButton_assettype_save_edit.setFont(font4)
        self.pushButton_assettype_save_edit.setStyleSheet(
            u"color: rgb(47, 175, 255);")
        self.label_31 = QLabel(self.page_assettype_edit_nxt)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(70, 220, 121, 21))
        self.label_31.setFont(font3)
        self.label_type_id = QLabel(self.page_assettype_edit_nxt)
        self.label_type_id.setObjectName(u"label_type_id")
        self.label_type_id.setGeometry(QRect(70, 150, 121, 21))
        self.label_type_id.setFont(font3)
        self.lineEdit_assettype_description_edit = QLineEdit(
            self.page_assettype_edit_nxt)
        self.lineEdit_assettype_description_edit.setObjectName(
            u"lineEdit_assettype_description_edit")
        self.lineEdit_assettype_description_edit.setGeometry(
            QRect(230, 220, 131, 21))
        self.label_typeid_edit_input = QLabel(self.page_assettype_edit_nxt)
        self.label_typeid_edit_input.setObjectName(u"label_typeid_edit_input")
        self.label_typeid_edit_input.setGeometry(QRect(230, 150, 91, 21))
        self.stackedWidget.addWidget(self.page_assettype_edit_nxt)
        self.page_assettype_view = QWidget()
        self.page_assettype_view.setObjectName(u"page_assettype_view")
        self.label_33 = QLabel(self.page_assettype_view)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(70, 50, 291, 41))
        self.label_33.setFont(font2)
        self.label_33.setCursor(QCursor(Qt.ArrowCursor))
        self.label_33.setAutoFillBackground(False)
        self.label_33.setFrameShadow(QFrame.Sunken)
        self.label_type_id_edit_view = QLabel(self.page_assettype_view)
        self.label_type_id_edit_view.setObjectName(u"label_type_id_edit_view")
        self.label_type_id_edit_view.setGeometry(QRect(60, 150, 121, 21))
        self.label_type_id_edit_view.setFont(font3)
        self.pushButton_assetview_find_typeview = QPushButton(
            self.page_assettype_view)
        self.pushButton_assetview_find_typeview.setObjectName(
            u"pushButton_assetview_find_typeview")
        self.pushButton_assetview_find_typeview.setGeometry(
            QRect(180, 250, 75, 23))
        self.lineEdit_assettype_td_edit_view = QComboBox(
            self.page_assettype_view)
        self.lineEdit_assettype_td_edit_view.setEditable(True)
        self.lineEdit_assettype_td_edit_view.setObjectName(
            u"lineEdit_assettype_td_edit_view")
        self.lineEdit_assettype_td_edit_view.setGeometry(
            QRect(240, 150, 131, 21))
        self.stackedWidget.addWidget(self.page_assettype_view)
        self.page_assettype_view_nxt = QWidget()
        self.page_assettype_view_nxt.setObjectName(u"page_assettype_view_nxt")
        self.label_type_desc_assettype_view_2 = QLabel(
            self.page_assettype_view_nxt)
        self.label_type_desc_assettype_view_2.setObjectName(
            u"label_type_desc_assettype_view_2")
        self.label_type_desc_assettype_view_2.setGeometry(
            QRect(250, 230, 91, 21))
        self.label_type_desc_assettype_view = QLabel(
            self.page_assettype_view_nxt)
        self.label_type_desc_assettype_view.setObjectName(
            u"label_type_desc_assettype_view")
        self.label_type_desc_assettype_view.setGeometry(
            QRect(60, 230, 121, 21))
        self.label_type_desc_assettype_view.setFont(font3)
        self.label_type_id_assettype_view = QLabel(
            self.page_assettype_view_nxt)
        self.label_type_id_assettype_view.setObjectName(
            u"label_type_id_assettype_view")
        self.label_type_id_assettype_view.setGeometry(QRect(70, 150, 121, 21))
        self.label_type_id_assettype_view.setFont(font3)
        self.label_34 = QLabel(self.page_assettype_view_nxt)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(70, 60, 291, 41))
        self.label_34.setFont(font2)
        self.label_34.setCursor(QCursor(Qt.ArrowCursor))
        self.label_34.setAutoFillBackground(False)
        self.label_34.setFrameShadow(QFrame.Sunken)
        self.label_type_id_assettype_view_2 = QLabel(
            self.page_assettype_view_nxt)
        self.label_type_id_assettype_view_2.setObjectName(
            u"label_type_id_assettype_view_2")
        self.label_type_id_assettype_view_2.setGeometry(
            QRect(250, 150, 91, 21))
        self.stackedWidget.addWidget(self.page_assettype_view_nxt)
        self.page_assetgroup = QWidget()
        self.page_assetgroup.setObjectName(u"page_assetgroup")
        self.label_4 = QLabel(self.page_assetgroup)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 70, 301, 41))
        self.label_4.setFont(font2)
        self.label_4.setCursor(QCursor(Qt.ArrowCursor))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setFrameShadow(QFrame.Sunken)
        self.lineEdit_assetgroup_gd = QLineEdit(self.page_assetgroup)
        self.lineEdit_assetgroup_gd.setObjectName(u"lineEdit_assetgroup_gd")
        self.lineEdit_assetgroup_gd.setGeometry(QRect(230, 150, 113, 20))
        self.pushButton_assetgroup_save = QPushButton(self.page_assetgroup)
        self.pushButton_assetgroup_save.setObjectName(
            u"pushButton_assetgroup_save")
        self.pushButton_assetgroup_save.setGeometry(QRect(150, 260, 111, 31))
        self.pushButton_assetgroup_save.setFont(font4)
        self.pushButton_assetgroup_save.setStyleSheet(
            u"color: rgb(47, 175, 255);")
        self.label_6 = QLabel(self.page_assetgroup)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 200, 121, 21))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.label_7 = QLabel(self.page_assetgroup)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 150, 121, 21))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.comboBox_Astgrp_type = QComboBox(self.page_assetgroup)
        self.comboBox_Astgrp_type.setObjectName(u"comboBox_Astgrp_type")
        self.comboBox_Astgrp_type.setGeometry(QRect(230, 200, 111, 22))
        self.stackedWidget.addWidget(self.page_assetgroup)
        self.page_assetgroup_edit = QWidget()
        self.page_assetgroup_edit.setObjectName(u"page_assetgroup_edit")
        self.pushButton_assetgroupedit_find = QPushButton(
            self.page_assetgroup_edit)
        self.pushButton_assetgroupedit_find.setObjectName(
            u"pushButton_assetgroupedit_find")
        self.pushButton_assetgroupedit_find.setGeometry(
            QRect(160, 250, 111, 31))
        self.pushButton_assetgroupedit_find.setFont(font4)
        self.pushButton_assetgroupedit_find.setStyleSheet(
            u"color: rgb(47, 175, 255);")
        self.label_29 = QLabel(self.page_assetgroup_edit)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(60, 40, 301, 41))
        self.label_29.setFont(font2)
        self.label_29.setCursor(QCursor(Qt.ArrowCursor))
        self.label_29.setAutoFillBackground(False)
        self.label_29.setFrameShadow(QFrame.Sunken)
        self.lineEdit_groupedit_id = QComboBox(self.page_assetgroup_edit)
        self.lineEdit_groupedit_id.setEditable(True)
        self.lineEdit_groupedit_id.setObjectName(u"lineEdit_groupedit_id")
        self.lineEdit_groupedit_id.setGeometry(QRect(240, 160, 113, 20))
        self.label_groupedit_id = QLabel(self.page_assetgroup_edit)
        self.label_groupedit_id.setObjectName(u"label_groupedit_id")
        self.label_groupedit_id.setGeometry(QRect(80, 160, 121, 21))
        self.label_groupedit_id.setFont(font3)
        self.label_groupedit_id.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.stackedWidget.addWidget(self.page_assetgroup_edit)
        self.page_assetgroup_edit_nxt = QWidget()
        self.page_assetgroup_edit_nxt.setObjectName(
            u"page_assetgroup_edit_nxt")
        self.label_groupedit_id_2 = QLabel(self.page_assetgroup_edit_nxt)
        self.label_groupedit_id_2.setObjectName(u"label_groupedit_id_2")
        self.label_groupedit_id_2.setGeometry(QRect(80, 110, 121, 21))
        self.label_groupedit_id_2.setFont(font3)
        self.label_groupedit_id_2.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.comboBox_groupedit_type = QComboBox(self.page_assetgroup_edit_nxt)
        self.comboBox_groupedit_type.setObjectName(u"comboBox_groupedit_type")
        self.comboBox_groupedit_type.setGeometry(QRect(250, 210, 111, 22))
        self.label_groupedit_desc = QLabel(self.page_assetgroup_edit_nxt)
        self.label_groupedit_desc.setObjectName(u"label_groupedit_desc")
        self.label_groupedit_desc.setGeometry(QRect(80, 160, 121, 21))
        self.label_groupedit_desc.setFont(font3)
        self.label_groupedit_desc.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.label_groupedit_type = QLabel(self.page_assetgroup_edit_nxt)
        self.label_groupedit_type.setObjectName(u"label_groupedit_type")
        self.label_groupedit_type.setGeometry(QRect(80, 210, 121, 21))
        self.label_groupedit_type.setFont(font3)
        self.label_groupedit_type.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.label_35 = QLabel(self.page_assetgroup_edit_nxt)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(60, 40, 301, 41))
        self.label_35.setFont(font2)
        self.label_35.setCursor(QCursor(Qt.ArrowCursor))
        self.label_35.setAutoFillBackground(False)
        self.label_35.setFrameShadow(QFrame.Sunken)
        self.lineEdit_groupedit_desc = QLineEdit(self.page_assetgroup_edit_nxt)
        self.lineEdit_groupedit_desc.setObjectName(u"lineEdit_groupedit_desc")
        self.lineEdit_groupedit_desc.setGeometry(QRect(250, 160, 113, 20))
        self.label_groupedit_id_3 = QLabel(self.page_assetgroup_edit_nxt)
        self.label_groupedit_id_3.setObjectName(u"label_groupedit_id_3")
        self.label_groupedit_id_3.setGeometry(QRect(250, 110, 111, 16))
        self.pushButton_assetgroupedit_save = QPushButton(
            self.page_assetgroup_edit_nxt)
        self.pushButton_assetgroupedit_save.setObjectName(
            u"pushButton_assetgroupedit_save")
        self.pushButton_assetgroupedit_save.setGeometry(
            QRect(170, 290, 111, 31))
        self.pushButton_assetgroupedit_save.setFont(font4)
        self.pushButton_assetgroupedit_save.setStyleSheet(
            u"color: rgb(47, 175, 255);")
        self.stackedWidget.addWidget(self.page_assetgroup_edit_nxt)
        self.page_assetgroup_view = QWidget()
        self.page_assetgroup_view.setObjectName(u"page_assetgroup_view")
        self.label_36 = QLabel(self.page_assetgroup_view)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(60, 50, 301, 41))
        self.label_36.setFont(font2)
        self.label_36.setCursor(QCursor(Qt.ArrowCursor))
        self.label_36.setAutoFillBackground(False)
        self.label_36.setFrameShadow(QFrame.Sunken)
        self.pushButton_assetgroupeview_find = QPushButton(
            self.page_assetgroup_view)
        self.pushButton_assetgroupeview_find.setObjectName(
            u"pushButton_assetgroupeview_find")
        self.pushButton_assetgroupeview_find.setGeometry(
            QRect(160, 250, 111, 31))
        self.pushButton_assetgroupeview_find.setFont(font4)
        self.pushButton_assetgroupeview_find.setStyleSheet(
            u"color: rgb(47, 175, 255);")
        self.lineEdit_groupeview_id = QComboBox(self.page_assetgroup_view)
        self.lineEdit_groupeview_id.setEditable(True)
        self.lineEdit_groupeview_id.setObjectName(u"lineEdit_groupeview_id")
        self.lineEdit_groupeview_id.setGeometry(QRect(240, 170, 113, 20))
        self.label_groupview_id = QLabel(self.page_assetgroup_view)
        self.label_groupview_id.setObjectName(u"label_groupview_id")
        self.label_groupview_id.setGeometry(QRect(90, 170, 121, 21))
        self.label_groupview_id.setFont(font3)
        self.label_groupview_id.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.stackedWidget.addWidget(self.page_assetgroup_view)
        self.page_assetgroup_view_nxt = QWidget()
        self.page_assetgroup_view_nxt.setObjectName(
            u"page_assetgroup_view_nxt")
        self.label_groupview_id_3 = QLabel(self.page_assetgroup_view_nxt)
        self.label_groupview_id_3.setObjectName(u"label_groupview_id_3")
        self.label_groupview_id_3.setGeometry(QRect(240, 130, 141, 21))
        self.label_37 = QLabel(self.page_assetgroup_view_nxt)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(90, 40, 301, 41))
        self.label_37.setFont(font2)
        self.label_37.setCursor(QCursor(Qt.ArrowCursor))
        self.label_37.setAutoFillBackground(False)
        self.label_37.setFrameShadow(QFrame.Sunken)
        self.label_groupview_id_2 = QLabel(self.page_assetgroup_view_nxt)
        self.label_groupview_id_2.setObjectName(u"label_groupview_id_2")
        self.label_groupview_id_2.setGeometry(QRect(70, 130, 121, 21))
        self.label_groupview_id_2.setFont(font3)
        self.label_groupview_id_2.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.label_groupview_desc_2 = QLabel(self.page_assetgroup_view_nxt)
        self.label_groupview_desc_2.setObjectName(u"label_groupview_desc_2")
        self.label_groupview_desc_2.setGeometry(QRect(250, 200, 131, 21))
        self.label_groupview_type_2 = QLabel(self.page_assetgroup_view_nxt)
        self.label_groupview_type_2.setObjectName(u"label_groupview_type_2")
        self.label_groupview_type_2.setGeometry(QRect(250, 270, 131, 21))
        self.label_groupview_type = QLabel(self.page_assetgroup_view_nxt)
        self.label_groupview_type.setObjectName(u"label_groupview_type")
        self.label_groupview_type.setGeometry(QRect(70, 270, 121, 21))
        self.label_groupview_type.setFont(font3)
        self.label_groupview_type.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.label_groupview_desc = QLabel(self.page_assetgroup_view_nxt)
        self.label_groupview_desc.setObjectName(u"label_groupview_desc")
        self.label_groupview_desc.setGeometry(QRect(70, 200, 121, 21))
        self.label_groupview_desc.setFont(font3)
        self.label_groupview_desc.setStyleSheet(u"color: rgb(47, 175, 255);")
        self.stackedWidget.addWidget(self.page_assetgroup_view_nxt)

        self.verticalLayout.addWidget(self.main_window)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

        # dependent_combobox_asset_add

        self.model = QStandardItemModel()
        self.comboBox_type_asset.setModel(self.model)
        self.comboBox_group_asset.setModel(self.model)
        for k, v in data.items():
            state = QStandardItem(k)
            self.model.appendRow(state)
            for value in v:
                city = QStandardItem(value)
                state.appendRow(city)
        self.comboBox_type_asset.currentIndexChanged.connect(self.updateStateCombo_asset)
        self.updateStateCombo_asset(0)

        # dependent_combobox_asset_add
        self.comboBox_type_asset_edit_2.setModel(self.model)
        self.comboBox_group_asset_edit_2.setModel(self.model)
        self.comboBox_type_asset_edit_2.currentIndexChanged.connect(self.updateStateCombo_asset_edit)
        self.updateStateCombo_asset_edit(0)

        # dependent_combobox_bulkupload
        self.comboBox_type_asset_edit_bulk.setModel(self.model)
        self.comboBox_group_asset_edit_bulk.setModel(self.model)
        self.comboBox_type_asset_edit_bulk.currentIndexChanged.connect(self.updateStateCombo_bulkupload)
        self.updateStateCombo_bulkupload(0)

        # comboBox

        self.comboBox_asset_status.addItems(ast_status)
        self.comboBox_Astgrp_type.addItems(type_list)

        # buttons

        self.btn_asset_add.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_asset))
        self.btn_asset_add.clicked.connect(lambda: self.dependent_combobox)
        self.btn_asset_add.clicked.connect( self.get_ast_cont_id)
        self.btn_assetgroup_add.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_assetgroup))

        self.btn_assettype_add.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_assettype))

        self.btn_asset_view.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_assetview))

        self.pushButton_assetview_find.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_assetview_nxt))

        self.btn_logout.clicked.connect(QApplication.instance().quit)
        self.pushButton_assetview_find.clicked.connect(
            lambda: self.view_asset())
        self.btn_asset_save.clicked.connect(lambda: self.commit_data_asset())
        self.pushButton_assetgroup_save.clicked.connect(
            lambda: self.commit_data_group())
        self.pushButton_assettype_save.clicked.connect(
            lambda: self.commit_data_type())
        self.btn_asset_edit.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_asset_edit))
        self.pushButton_assetview_find_edit.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_asset_edit_nxt))
        self.btn_assettype_edit.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_assettype_edit))
        self.pushButton_assetview_find_edittype.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_assettype_edit_nxt))
        self.btn_assettype_view.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_assettype_view))
        self.pushButton_assetview_find_typeview.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_assettype_view_nxt))
        self.btn_assetgroup_edit.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_assetgroup_edit))
        self.pushButton_assetgroupedit_find.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_assetgroup_edit_nxt))
        self.btn_assetgroup_view.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_assetgroup_view))
        self.pushButton_assetgroupeview_find.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_assetgroup_view_nxt))
        self.pushButton_assetview_find_edit.clicked.connect(lambda: self.edit_asset())
        self.btn_asset_save_edit_2.clicked.connect(lambda: self.edit_asset_commit())
        self.pushButton_assetview_find_edittype.clicked.connect(lambda: self.edit_type())
        self.pushButton_assettype_save_edit.clicked.connect(lambda: self.edit_type_commit())
        self.pushButton_assetview_find_typeview.clicked.connect(lambda: self.type_view())
        self.pushButton_assetgroupedit_find.clicked.connect(lambda: self.edit_group())
        self.pushButton_assetgroupedit_save.clicked.connect(lambda: self.edit_group_commit())
        self.pushButton_assetgroupeview_find.clicked.connect(lambda: self.group_view())
        self.pushButton_bulkupload.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_asset_bulk))
        self.pushButton_asset_bulk.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_asset_bulk_nxt))
        self.pushButton_asset_bulk.clicked.connect(lambda: self.bulkupload())
        #self.pushButton_bulkupload.clicked.connect(lambda: self.callidasset())
        self.btn_asset_save_edit_3.clicked.connect(lambda: self.bulkuoload_commit())
        self.callidasset()
        # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.lable_title.setText(QCoreApplication.translate(
            "MainWindow", u"   Inventory Management", None))
        self.btn_assetgroup_view.setText(
            QCoreApplication.translate("MainWindow", u"View", None))
        self.label_asset.setText(QCoreApplication.translate(
            "MainWindow", u"        Asset", None))
        self.btn_asset_add.setText(
            QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_assettype_view.setText(
            QCoreApplication.translate("MainWindow", u"View", None))
        self.btn_assetgroup_edit.setText(
            QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_assettype_add.setText(
            QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_assetgroup.setText(
            QCoreApplication.translate("MainWindow", u"Asset Group", None))
        self.btn_assetgroup_add.setText(
            QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_asset_edit.setText(
            QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_asset_view.setText(
            QCoreApplication.translate("MainWindow", u"View", None))
        self.btn_logout.setText(
            QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.btn_assettype_edit.setText(
            QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_assettype.setText(
            QCoreApplication.translate("MainWindow", u"Asset Type", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Choose options from", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"left panel to get your", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"work done.", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#d0398a;\">Add Asset</span></p></body></html>",
            None))
        self.label_asset_id.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Asset ID</span></p></body></html>",
            None))
        self.label_12.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Serial Number</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Name</span></p></body></html>",
            None))
        self.label_26.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Type of Asset</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Group of Asset</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Details</span></p></body></html>",
            None))
        self.label_27.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Parent ID</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset OEM (Maker's Name)</span></p></body></html>",
            None))
        self.label_24.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Contact Number</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Contact Number esk1</span></p></body></html>",
            None))
        self.label_13.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Seller Name</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Seller Contact Number</span></p></body></html>",
            None))
        self.label_15.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Email ID</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Email ID esk1</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Seller email ID</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Purchase Date</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Warrenty Details</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Status</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Price</span></p></body></html>",
            None))
        self.label_22.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Warrenty Ending Date</span></p><p><br/></p></body></html>",
            None))
        self.btn_asset_save.setText(
            QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_53.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#ff5500;\">Asset </span></p></body></html>",
            None))
        self.label_asset_view_id_edit.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#005500;\">Enter Asset ID</span></p></body></html>",
            None))
        self.pushButton_assetview_find_edit.setText(
            QCoreApplication.translate("MainWindow", u"Find", None))
        self.btn_asset_save_edit_2.setText(
            QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_asset_id_edit_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Asset ID</span></p></body></html>",
            None))
        self.label_srlno_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Serial Number</span></p></body></html>", None))
        self.label_assetname_edit_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Name</span></p></body></html>",
            None))
        self.label_typeasset_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Type of Asset</span></p></body></html>", None))
        self.label_groupasset_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Group of Asset</span></p></body></html>", None))
        self.label_details_edit_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Details</span></p></body></html>",
            None))
        self.label_parentid_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Parent ID</span></p></body></html>", None))
        self.label_oemname_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset OEM (Maker's Name)</span></p></body></html>",
            None))
        self.label_oemcontactno_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Contact Number</span></p></body></html>", None))
        self.label_oemcontact_esk1_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Contact Number esk1</span></p></body></html>",
            None))
        self.label_sellername_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Seller Name</span></p></body></html>", None))
        self.label_sellercontactno_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Seller Contact Number</span></p></body></html>",
            None))
        self.label_oememail_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Email ID</span></p></body></html>", None))
        self.label_oememailesk1_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Email ID esk1</span></p></body></html>", None))
        self.label_selleremail_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Seller email ID</span></p></body></html>", None))
        self.label_Purchasedate_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Purchase Date</span></p></body></html>", None))
        self.label_warrentydetails_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Warrenty Details</span></p></body></html>", None))
        self.label_assetstatus_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Status</span></p></body></html>", None))
        self.label_price_edit_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Price</span></p></body></html>",
            None))
        self.label_warrentyenddate_edit_2.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Warrenty Ending Date</span></p><p><br/></p></body></html>",
            None))
        self.label_Asset_id_edit_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_52.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#ff5500;\">Asset </span></p></body></html>",
            None))
        self.label_asset_view_id.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#005500;\">Enter Asset ID</span></p></body></html>",
            None))
        self.pushButton_assetview_find.setText(
            QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_asset_view_id_edit_2.setText(QCoreApplication.translate("MainWindow",
                                                                           u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#005500;\">Enter Asset ID</span></p></body></html>",
                                                                           None))
        self.pushButton_asset_bulk.setText(
            QCoreApplication.translate("MainWindow", "Find"))
        self.label_56.setText(QCoreApplication.translate("MainWindow",
                                                         "<html><head/><body><p align=\"center\"><span style=\" color:#ff5500;\">Asset </span></p></body></html>"))
        self.btn_asset_save_edit_3.setText(
            QCoreApplication.translate("MainWindow", "Save"))
        self.label_57.setText(QCoreApplication.translate("MainWindow",
                                                         "<html><head/><body><p align=\"center\"><span style=\" color:#ff5500;\">Asset </span></p></body></html>"))
        self.label_asset_id_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                      "<html><head/><body><p><span style=\" color:#00557f;\">Asset ID</span></p></body></html>"))
        self.label_srlno_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                   "<html><head/><body><p><span style=\" color:#00557f;\">Serial Number</span></p></body></html>"))
        self.label_assetname_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                       "<html><head/><body><p><span style=\" color:#00557f;\">Asset Name</span></p></body></html>"))
        self.label_typeasset_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                       "<html><head/><body><p><span style=\" color:#00557f;\">Type of Asset</span></p></body></html>"))
        self.label_groupasset_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                        "<html><head/><body><p><span style=\" color:#00557f;\">Group of Asset</span></p></body></html>"))
        self.label_details_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                     "<html><head/><body><p><span style=\" color:#00557f;\">Details</span></p></body></html>"))
        self.label_parentid_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                      "<html><head/><body><p><span style=\" color:#00557f;\">Asset Parent ID</span></p></body></html>"))
        self.label_oemname_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                     "<html><head/><body><p><span style=\" color:#00557f;\">Asset OEM (Maker\'s Name)</span></p></body></html>"))
        self.label_oemcontactno_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                          "<html><head/><body><p><span style=\" color:#00557f;\">OEM Contact Number</span></p></body></html>"))
        self.label_oemcontact_esk1_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                             "<html><head/><body><p><span style=\" color:#00557f;\">OEM Contact Number esk1</span></p></body></html>"))
        self.label_sellername_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                        "<html><head/><body><p><span style=\" color:#00557f;\">Asset Seller Name</span></p></body></html>"))
        self.label_sellercontactno_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                             "<html><head/><body><p><span style=\" color:#00557f;\">Seller Contact Number</span></p></body></html>"))
        self.label_oememail_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                      "<html><head/><body><p><span style=\" color:#00557f;\">OEM Email ID</span></p></body></html>"))
        self.label_oememailesk1_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                          "<html><head/><body><p><span style=\" color:#00557f;\">OEM Email ID esk1</span></p></body></html>"))
        self.label_selleremail_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                         "<html><head/><body><p><span style=\" color:#00557f;\">Seller email ID</span></p></body></html>"))
        self.label_Purchasedate_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                          "<html><head/><body><p><span style=\" color:#00557f;\">Purchase Date</span></p></body></html>"))
        self.label_warrentydetails_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                             "<html><head/><body><p><span style=\" color:#00557f;\">Warrenty Details</span></p></body></html>"))
        self.label_assetstatus_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                         "<html><head/><body><p><span style=\" color:#00557f;\">Asset Status</span></p></body></html>"))
        self.label_price_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                   "<html><head/><body><p><span style=\" color:#00557f;\">Price</span></p></body></html>"))
        self.label_warrentyenddate_edit_5.setText(QCoreApplication.translate("MainWindow",
                                                                             "<html><head/><body><p><span style=\" color:#00557f;\">Warrenty Ending Date</span></p><p><br/></p></body></html>"))
        self.label_Asset_id_edit_input_bulk.setText(
            QCoreApplication.translate("MainWindow", "TextLabel"))
        self.label_54.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#00557f;\">View Asset</span></p></body></html>",
            None))
        self.label_assetview_id_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Asset ID</span></p></body></html>",
            None))
        self.label_assetview_srlno.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Serial Number</span></p></body></html>", None))
        self.label_assetview_assetname.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Name</span></p></body></html>",
            None))
        self.label_assetview_type.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Type of Asset</span></p></body></html>", None))
        self.label_assetview_group.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Group of Asset</span></p></body></html>", None))
        self.label_assetview_details.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Details</span></p></body></html>",
            None))
        self.label_assetview_assetparentid.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Parent ID</span></p></body></html>", None))
        self.label_assetview_oemname.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset OEM (Maker's Name)</span></p></body></html>",
            None))
        self.label_assetview_oemcontactno.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Contact Number</span></p></body></html>", None))
        self.label_assetview_oemcontactnoesk1.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Contact Number esk1</span></p></body></html>",
            None))
        self.label_assetview_sellername.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Seller Name</span></p></body></html>", None))
        self.label_assetview_sellerno.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Seller Contact Number</span></p></body></html>",
            None))
        self.label_assetview_oememail.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Email ID</span></p></body></html>", None))
        self.label_assetview_oememailesk1.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">OEM Email ID esk1</span></p></body></html>", None))
        self.label_assetview_selleremail.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Seller email ID</span></p></body></html>", None))
        self.label_assetview_purchasedate.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Purchase Date</span></p></body></html>", None))
        self.label_assetview_Warrentydetails.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Warrenty Details</span></p></body></html>", None))
        self.label_assetview_status.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Asset Status</span></p></body></html>", None))
        self.label_assetview_price.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#00557f;\">Price</span></p></body></html>",
            None))
        self.label_assetview_warrentyenddate.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#00557f;\">Warrenty Ending Date</span></p><p><br/></p></body></html>",
            None))
        self.label_assetview_id_2_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_srlno_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_assetname_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_type_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_group_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_details_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_assetparentid_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_oemname_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_oemcontactno_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_oemcontactnoesk1_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_sellername_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_sellerno_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_oememail_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_oememailesk1_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_selleremail_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_purchasedate_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_Warrentydetails_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_warrentyenddate_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_status_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_assetview_price_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_55.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#00557f;\">View Asset</span></p></body></html>",
            None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#ffa508;\">Asset TYPE</span></p></body></html>",
            None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#ffa508;\">Type Description</span></p></body></html>", None))
        self.pushButton_assettype_save.setText(
            QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_type_id_edit.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#ffaa00;\">Enter Type ID</span></p></body></html>",
            None))
        self.label_32.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#55ff00;\">Edit Asset TYPE</span></p></body></html>",
            None))
        # if QT_CONFIG(tooltip)
        self.pushButton_assetview_find_edittype.setToolTip(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#00aa00;\">Find</span></p></body></html>",
            None))
        # endif // QT_CONFIG(tooltip)
        self.pushButton_assetview_find_edittype.setText(
            QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_30.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#55ff00;\">Edit Asset TYPE</span></p></body></html>",
            None))
        self.pushButton_assettype_save_edit.setText(
            QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_31.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#ffa508;\">Type Description</span></p></body></html>", None))
        self.label_type_id.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#ffa508;\">Type ID</span></p></body></html>",
            None))
        self.label_typeid_edit_input.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#00007f;\">View Asset TYPE</span></p></body></html>",
            None))
        self.label_type_id_edit_view.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#ffaa00;\">Enter Type ID</span></p></body></html>",
            None))
        # if QT_CONFIG(tooltip)
        self.pushButton_assetview_find_typeview.setToolTip(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#00aa00;\">Find</span></p></body></html>",
            None))
        # endif // QT_CONFIG(tooltip)
        self.pushButton_assetview_find_typeview.setText(
            QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_type_desc_assettype_view_2.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_type_desc_assettype_view.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p><span style=\" color:#ffa508;\">Type Description</span></p></body></html>", None))
        self.label_type_id_assettype_view.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#ffa508;\">Type ID</span></p></body></html>",
            None))
        self.label_34.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#00007f;\">View Asset TYPE</span></p></body></html>",
            None))
        self.label_type_id_assettype_view_2.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#005500;\">Add Asset GROUP</span></p></body></html>",
            None))
        self.pushButton_assetgroup_save.setText(
            QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Type of Asset", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Group Description", None))
        self.pushButton_assetgroupedit_find.setText(
            QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_29.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#55aa7f;\">Edit Asset GROUP</span></p></body></html>",
            None))
        self.label_groupedit_id.setText(QCoreApplication.translate(
            "MainWindow", u"Enter group ID", None))
        self.label_groupedit_id_2.setText(
            QCoreApplication.translate("MainWindow", u"Group ID", None))
        self.label_groupedit_desc.setText(QCoreApplication.translate(
            "MainWindow", u"Group Description", None))
        self.label_groupedit_type.setText(
            QCoreApplication.translate("MainWindow", u"Type of Asset", None))
        self.label_35.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#55aa7f;\">Edit Asset GROUP</span></p></body></html>",
            None))
        self.label_groupedit_id_3.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_assetgroupedit_save.setText(
            QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_36.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#55557f;\">View Asset GROUP</span></p></body></html>",
            None))
        self.pushButton_assetgroupeview_find.setText(
            QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_groupview_id.setText(QCoreApplication.translate(
            "MainWindow", u"Enter group ID", None))
        self.label_groupview_id_3.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_37.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\"><span style=\" color:#55557f;\">View Asset GROUP</span></p></body></html>",
            None))
        self.label_groupview_id_2.setText(
            QCoreApplication.translate("MainWindow", u"Group ID", None))
        self.label_groupview_desc_2.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_groupview_type_2.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_groupview_type.setText(
            QCoreApplication.translate("MainWindow", u"Type of Asset", None))
        self.label_groupview_desc.setText(QCoreApplication.translate(
            "MainWindow", u"Group Description", None))
        self.pushButton_bulkupload.setText(
            QCoreApplication.translate("MainWindow", u"Copy", None))
    # retranslateUi

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

'''
Note: 
asset_view_id_edit --> changed to combo_box from line_edit
asset_view_id --> changed to combo_box from line_edit
lineEdit_assettype_td_edit --> changed to combo_box from line_edit
lineEdit_assettype_td_edit_view --> changed to combo_box from line_edit
lineEdit_groupedit_id --> changed to combo_box from line_edit
lineEdit_groupeview_id --> changed to combo_box from line_edit
'''
