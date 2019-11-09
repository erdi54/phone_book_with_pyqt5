import sys
import os
from PyQt5.QtCore import pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import  QApplication,QDialog,QLineEdit,QPushButton,QTableWidgetItem,QMessageBox,QWidget
from PyQt5 import uic,QtGui,QtCore
from epostaDb import epostaEkleme

class EpostaApp(QWidget):
    listeID=" "
    def __init__(self,parent=None): 
        super(EpostaApp,self).__init__(parent)
        self.epostaDialog= uic.loadUi(os.getcwd()+os.sep+"epostaEkleme.ui")
        self.database = epostaEkleme ()
        self.initUI()
   
    def initUI(self):
        self.epostaDialog.btnKaydet.clicked.connect(self.epostaDialog.close)
    
    def gosterme(self):
        self.listeleme(self.listeID)
        self.epostaDialog.show()
   
    def listeleme(self,val=0):
 
        liste = self.database.epostaDB(val)
        self.epostaDialog.listeEposta.clear()
        for item in liste:
           self.epostaDialog.listeEposta.addItem(item[1])
  

