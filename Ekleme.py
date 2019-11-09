import sys
import os
from PyQt5.QtCore import pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import  QApplication,QDialog,QLineEdit,QPushButton,QTableWidgetItem,QMessageBox,QWidget
from PyQt5 import uic,QtGui,QtCore
from TelEklemeDB import telEkleme

class TelApp(QWidget):

    def __init__(self,parent=None): 
        super(TelApp,self).__init__(parent)
        self.telDialog = uic.loadUi(os.getcwd()+os.sep+"Ekleme.ui")
        self.database = telEkleme()
        self.initUI()
   
    def initUI(self):
        self.telDialog.btnKaydet.clicked.connect(self.telDialog.close)
    
    @pyqtSlot(int)
    def isimDegis(self,val=0):
 
        liste = self.database.telListele(val)
        self.telDialog.telList.clear()
        for item in liste:
           self.telDialog.telList.addItem(item[1])
       
        #print(liste)
    def tetikleme(self,anaMenu=None):
        anaMenu.kayitId.connect(self.isimDegis)
       

