from Db import DBGenel
import os 

class epostaEkleme(DBGenel):
    def __init__(self, *args, **kwargs):
        super().__init__(os.getcwd()+ os.sep +"TDF.db")
    
    def epostaDB(self,kayitId):
        liste = self.select(TABLO="TDF_EPOSTA ",SUTUN=["EP_ID","EPOSTA"],SART=[("1","KAYIT_ID",str(kayitId))])
        return liste