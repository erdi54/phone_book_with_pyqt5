import sys
import os
from PyQt5.QtCore import pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import  QApplication,QMainWindow,QLineEdit,QPushButton,QTableWidgetItem,QMessageBox,QMessageBox 
from PyQt5 import uic,QtGui,QtCore
from  AnaDb import AnaDb
from Ekleme import TelApp 
from epostaEkleme import EpostaApp
class App(QMainWindow):
    kayitId =pyqtSignal(int)
    #Hesap Makinası PyQT
    def __init__(self): 
        super().__init__()
        self.pencere = uic.loadUi(os.getcwd()+os.sep+"AnaEkran.ui")
        self.database = AnaDb()
        self.epostaApp=EpostaApp()
        self.pencere.tblListe.setHorizontalHeaderLabels(["ID","ADI","SOYADI","ILI","ILCESI"])
        self.initUI()
   
    def initUI(self):
        self.tabloDoldur()
        self.comboIlDoldur()
        self.pencere.telEkleme.triggered.connect(self.tiklandi)
        self.pencere.epostaEkleme.triggered.connect(self.tiklandi2)
        self.pencere.btKaydet.clicked.connect(self.KayitEkle)
        self.pencere.show()

    
    def setPencere(self,nesne):
        self.telApp= TelApp(self)
        self.telApp.tetikleme(self) 
    
    def tabloDoldur(self): 
        liste = self.database.kisiListele()
        self.pencere.tblListe.doubleClicked.connect(self.tabloSecim)
        self.pencere.tblListe.setRowCount(10)
        self.pencere.tblListe.setColumnCount(len(liste[0]))
        for i in range(0,len(liste)):
            for j in range(0,len(liste[0])):
                self.pencere.tblListe.setItem(i,j,QTableWidgetItem(str(liste[i][j])))
    def tabloSecim(self):
        for currentQTableWidgetItem in self.pencere.tblListe.selectedItems():
            satir = currentQTableWidgetItem.row()
            self.pencere.lblID.setText(self.pencere.tblListe.item(satir,0).text()) 
            self.pencere.txtAdi.setText(self.pencere.tblListe.item(satir,1).text())
            self.pencere.txtSoyadi.setText(self.pencere. tblListe.item(satir,2).text())
            self.pencere.cmbIl.setCurrentText(self.pencere.tblListe.item(satir,3).text())
            self.pencere.cmbIlce.setCurrentText(self.pencere.tblListe.item(satir,4).text())
            self.kayitId.emit(int((self.pencere.tblListe.item(satir,0).text())))
            self.epostaApp.listeID = (self.pencere.tblListe.item(satir,0).text())
            self.epostaApp.listeleme(self.epostaApp.listeID)
    
    def tiklandi(self):
         
        self.telApp.telDialog.show()
    
    def tiklandi2(self):
         
        self.epostaApp.gosterme()

    def KayitEkle(self):
        messageBox = QMessageBox.question(self,"Soru","Kaydetmek istediğinizden emin misiniz?",QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.Yes)
        if messageBox == QMessageBox.Yes:
            adi = self.pencere.txtAdi.text()
            soyadi = self.pencere.txtSoyadi.text()
            il = self.pencere.cmbIl.currentIndex()
            ilce = self.pencere.cmbIlce.itemData(self.pencere.cmbIlce.currentIndex())
            if self.pencere.lblID.text() == "":
                sonuc = self.database.kisiEkle(adi,soyadi,il,ilce)
                if sonuc == 1:
                    self.pencere.tblListe.clear()
                    self.tabloDoldur()
            else:
                sonuc = self.database.kisiGuncelleme(adi,soyadi,il,ilce,self.pencere.lblID.text())
                if sonuc == 1:
                    self.pencere.tblListe.clear()
                    self.tabloDoldur()

    
    def comboIlDoldur(self):
        
        self.pencere.cmbIl.addItem("Seçiniz", -1)
        liste=self.database.ilListele()
        for a,b in liste:
            self.pencere.cmbIl.addItem(b,a)
        self.pencere.cmbIl.currentIndexChanged.connect(self.comboSecim) 
    
    def comboIlceDoldur(self,ilID):
        liste =self.database.ilceListele(ilID)
        self.pencere.cmbIlce.clear()
        self.pencere.cmbIlce.addItem("Seçiniz", -1)
        for a,b in liste:
            self.pencere.cmbIlce.addItem(b,a)
       
    def comboSecim(self,i):
       sonuc = self.pencere.cmbIl.itemData(i)
       self.comboIlceDoldur(sonuc)
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.setPencere(ex) 
    sys.exit(app.exec_())