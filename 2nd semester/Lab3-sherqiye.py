from PyQt5.QtWidgets import (QWidget, QApplication, QTableWidgetItem)
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5.uic import loadUi
from fpdf import FPDF
import xlsxwriter
from PyQt5.QtWidgets import QMessageBox


data=(
    (1, "Watch ", 10, 2, 20, 3.6, 23.6),
    (2, "Necklace", 5, 5, 25, 4.5, 29.5),
    (3, "Bracelet", 2, 5, 10, 1.8, 11.8),
    (4, "Ring", 1, 10, 10, 1.8, 11.8)
    )

pr='sherqiye_quluzade.ui'
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
          self.ui.yekunButton.clicked.connect(self.yekun)
          self.ui.excelButton.clicked.connect(self.excel)
          self.ui.pdfButton.clicked.connect(self.pdf)
          self.ui.tableWidget.setColumnWidth(1, 200) 

      def loaddata(self):
          a = len(data)
          b = len(data[0])
          self.ui.tableWidget.setRowCount(a)
          self.ui.tableWidget.setColumnCount(b)
          for i in range(a):
              for j in range(b):
                  self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))
          self.ui.tableWidget.update()

      def Tarix(self):
         self.ui.calendarWidget.setVisible(True)

      def choose(self):
        gun = self.ui.calendarWidget.selectedDate().day()
        ay = self.ui.calendarWidget.selectedDate().month()
        il = self.ui.calendarWidget.selectedDate().year()
        self.ui.Lcd1.display(gun)
        self.ui.Lcd2.display(ay)
        self.ui.Lcd3.display(il)
        self.ui.calendarWidget.setVisible(False)

      def yekun(self):
          line5 = 0
          line6 = 0
          line7 = 0
          for i in range(len(data)):   #lendata=4 i=0,1,2,3
             line5+=data[i][4]
             line6+=data[i][5]
             line7+=data[i][6]
          self.ui.lineEdit5.setText(str(line5))
          self.ui.lineEdit6.setText(str(line6))
          self.ui.lineEdit7.setText(str(line7))

      def pdf(self):
        PDF = FPDF()
        PDF.add_page()
        PDF.set_font("Times", size=16)
        for x in range(self.ui.tableWidget.rowCount()):
            for y in range(self.ui.tableWidget.columnCount()):
                z = self.ui.tableWidget.item(x, y)
                PDF.cell(30, 5, str(z.text()))
            PDF.ln()
        PDF.output(r'C:\Users\User\Desktop\Lab3-sherqiye.pdf')
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(r'C:\Users\User\Desktop\Lab3-sherqiye.pdf') 
        msg.setInformativeText('PDF file saved')
        msg.setWindowTitle("Bildiriş")
        msg.exec_()

      def excel(self):
          data=(
              (1, "Watch ", 10, 2, 20, 3.6, 23.6),
              (2, "Necklace", 5, 5, 25, 4.5, 29.5),
              (3, "Bracelet", 2, 5, 10, 1.8, 11.8),
              (4, "Ring", 1, 10, 10, 1.8, 11.8)
              )
          new_list = []
          for i in range(len(data)):
              new_list.append(data[i])
          with xlsxwriter.Workbook(r'C:\Users\User\Desktop\Lab3-sherqiye.xlsx') as workbook:
              worksheet = workbook.add_worksheet()
              for row_num, data in enumerate(new_list):
                  worksheet.write_row(row_num, 0, data)
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Information)
          msg.setText(r"C:\Users\User\Desktop\Lab3-sherqiye.xlsx")
          msg.setInformativeText('Excel file saved')
          msg.setWindowTitle("Bildiriş")
          msg.exec_()

    
if __name__ == '__main__':
      appl = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(appl.exec())