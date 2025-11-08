from dotenv import load_dotenv
import os
load_dotenv()

import xlwt
from PyQt5.QtWidgets import (QWidget, QTableWidget, QApplication, QTableWidgetItem, QHBoxLayout)
from PyQt5 import QtWidgets, QtGui, QtCore, QtSql
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QSize, Qt
import sys
import mysql.connector
from PyQt5.uic import loadUi
from fpdf import FPDF
import xlsxwriter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PyQt5.QtWidgets import QMessageBox


mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)        

pr = 'sherqiye_quluzade.ui'
Ui_MainWindow, QtBaseClass = uic.loadUiType(pr)

class MainWindow(QtWidgets.QMainWindow): 

    def __init__(self):
          super(MainWindow, self).__init__()
          loadUi("sherqiye_quluzade.ui", self)
          self.mywindow = QWidget()
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.ui.calendarWidget.setVisible(False)
          self.ui.toolButton.clicked.connect(self.Tarix)
          self.ui.calendarWidget.clicked.connect(self.choose)
          self.ui.calendarWidget.selectionChanged.connect(self.loaddata)
          self.ui.tableWidget.setHorizontalHeaderLabels(["KOD", "MALIN ADI", "QİYMƏTİ", "MİQDARI", "MƏBLƏĞİ", "ƏDV", "ÜMUMİ MƏBLƏĞ", "TARIX"])
          self.ui.addButton.clicked.connect(self.add)
          self.ui.saveButton.clicked.connect(self.save)
          self.ui.deleteButton.clicked.connect(self.delete)
          self.ui.yekunButton.clicked.connect(self.yekun)
          self.ui.excelButton.clicked.connect(self.excel)
          self.ui.pdfButton.clicked.connect(self.pdf)
          self.mycursor = mydb.cursor()


    def loaddata(self):
         global tarix
         tarix = self.ui.calendarWidget.selectedDate().toString('yyyy-MM-dd')
         sqlquery = f"SELECT * FROM lab3 WHERE TARİX = '{tarix}'"

         self.mycursor.execute(sqlquery)
         data = self.mycursor.fetchall()
         self.ui.tableWidget.setRowCount(len(data))
         tablerow = 0
         for row in data:
              self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
              self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
              self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
              self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
              self.ui.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
              self.ui.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
              self.ui.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
              self.ui.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
              tablerow+=1
          
              
          
    def Tarix(self):
         self.ui.calendarWidget.setVisible(True)

    def choose(self):
        gun= self.ui.calendarWidget.selectedDate().day()
        ay= self.ui.calendarWidget.selectedDate().month()
        il= self.ui.calendarWidget.selectedDate().year()
        self.ui.Lcd1.display(gun)
        self.ui.Lcd2.display(ay)
        self.ui.Lcd3.display(il)
        self.ui.calendarWidget.setVisible(False)

    def yekun(self):
          line5 = 0
          line6 = 0
          line7 = 0
          a = self.ui.tableWidget.rowCount()
          for x in range(a):
             line5+=float(self.ui.tableWidget.item(x, 4).text())
             line6+=float(self.ui.tableWidget.item(x, 5).text())
             line7+=float(self.ui.tableWidget.item(x, 6).text())
          self.ui.lineEdit5.setText(str(line5))
          self.ui.lineEdit6.setText(str(line6))
          self.ui.lineEdit7.setText(str(line7))

    def add(self):
         rowPosition = self.ui.tableWidget.rowCount()
         self.ui.tableWidget.setRowCount(rowPosition+1)
         msg = QMessageBox()
         msg.setIcon(QMessageBox.Information)
         msg.setText('Sətir əlavə edildi')
         msg.setInformativeText('Yazandan sonra save etməyi unutmayın')
         msg.setWindowTitle("Bildiriş")
         msg.exec_()

    def save(self):
         sqlquery = f"SELECT * FROM lab3 WHERE TARİX = '{tarix}'"
         self.mycursor.execute(sqlquery)
         data = self.mycursor.fetchall()
         list = []
         a = self.ui.tableWidget.rowCount()
         b = self.ui.tableWidget.columnCount()
         for x in range(len(data), a):
              list_1 = []
              for y in range(b):
                    list_1.append(self.ui.tableWidget.item(x, y).text())
              list_1.append(tarix)
              list.append(list_1)
         self.mycursor = mydb.cursor()
         sqlquery = "INSERT INTO lab3 VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
         self.mycursor.executemany(sqlquery, list)
         mydb.commit()
         msg = QMessageBox()
         msg.setIcon(QMessageBox.Information)
         msg.setText('Yadda saxlanıldı')
         msg.setInformativeText('...')
         msg.setWindowTitle("Bildiriş")
         msg.exec_()

    def delete(self):
         msg = QMessageBox()
         msg.setIcon(QMessageBox.Information)
         msg.setText("Setirler silinsinmi?")
         msg.setWindowTitle("Warning")
         msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
         retval = msg.exec_()
         if retval == QMessageBox.Ok:
             index_list = []
             self.mycursor = mydb.cursor()                                                       
             for model_index in self.ui.tableWidget.selectionModel().selectedRows():       
                 index = QtCore.QPersistentModelIndex(model_index)         
                 index_list.append(index)                                             

             for index in index_list: 
                 kod = self.ui.tableWidget.item(index.row(), 0).text()
                 sqlquery = f"DELETE FROM lab3 WHERE KOD = '{kod}'"
                 self.mycursor.execute(sqlquery)
                 mydb.commit()                                   
                 self.ui.tableWidget.removeRow(index.row())

    def pdf(self):
        list = []
        a = self.ui.tableWidget.rowCount()
        b = self.ui.tableWidget.columnCount()
        for x in range(a):
              list_1 = []
              for y in range(b):
                    list_1.append(self.ui.tableWidget.item(x, y).text())
              list.append(list_1)
        df = pd.DataFrame(list, columns = ("KOD", "MALIN ADI", "QİYMƏTİ", "MİQDARI", "MƏBLƏĞİ", "ƏDV", "ÜMUMİ MƏBLƏĞ"))
        fig, ax =plt.subplots(figsize=(12,4))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='left')
        pp = PdfPages("table.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(r'C:\Users\User\Desktop\50bal-sherqiye.pdf')
        msg.setInformativeText('PDF file saved')
        msg.setWindowTitle("Bildiriş")
        msg.exec_()

    def excel(self):
         new_list = []
         a = self.ui.tableWidget.rowCount()
         b = self.ui.tableWidget.columnCount()
         for x in range(a):
              list_1 = []
              for y in range(b):
                   list_1.append(self.ui.tableWidget.item(x, y).text())
              new_list.append(list_1)
         with xlsxwriter.Workbook(r'C:\Users\User\Desktop\50bal-sherqiye.xlsx') as workbook:
              worksheet = workbook.add_worksheet()
              for row_num, data in enumerate(new_list):
                  worksheet.write_row(row_num, 0, data)
         msg = QMessageBox()
         msg.setIcon(QMessageBox.Information)
         msg.setText(r'C:\Users\User\Desktop\50bal-sherqiye.xlsx')
         msg.setInformativeText('Excel file saved')
         msg.setWindowTitle("Bildiriş")
         msg.exec_()
          

if __name__ == '__main__':
      appl = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(appl.exec())