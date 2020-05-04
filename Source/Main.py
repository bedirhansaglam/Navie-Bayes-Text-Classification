import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
import random
from PySide2 import QtCore, QtWidgets, QtGui
from tasarim import Ui_MainWindow
import NavieBayes
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) #Gorsel arayuz set ediliyor
        self.ui.pb_navie_veriekle.clicked.connect(self.navie_item_add) #yeni kategori ve veri eklerken kullanacagimiz butonun fonksiyonu set ediliyor
        self.ui.pb_navie_siniflandir.clicked.connect(self.navie_bayes_siniflandir) #var olan verilere gore girilen metni siniflandirmak icin kullandigimiz butonun fonksiyonu set ediliyor
        self.navie_bayes_data_set=NavieBayes.default_training_data() # default olarak spor ve ekonomi kategorilerini iceren veriler set ediliyor
        self.verileri_tabloya_dok(self.navie_bayes_data_set,self.ui.tbl_navie_data_set) # set edilen veriler tabloda gosteriliyor
    

    def navie_item_add(self):#var olan default datasetimize yeni kategori ve kategori anahtar kelimlerini bu fonksiyon ile ekliyoruz
        kelime=self.ui.le_navie_kelime.text() #key value textboxtan aliniyor 
        kategori=self.ui.le_naive_kategori.text()#kategori value textboxtan aliniyor
        kelime=kelime.lower() #kelimenin harfleri kucuk harfe cevriliyor
        kategori=kategori.lower()#kategorinin harfleri kucuk harfe cevriliyor
        self.navie_bayes_data_set.append((kelime,kategori)) #default olarak set ettigimiz datasete yeni anahtar deger ikilisi ekleniyor
        self.verileri_tabloya_dok(self.navie_bayes_data_set,self.ui.tbl_navie_data_set) #yeni eklenen degerlerin gozukebilmesi icin veriler tekrar tabloya dokuluyor
        self.ui.le_navie_kelime.setText("") #yeni degerler icin kelime textboxi sifirlaniyor
    
    def navie_bayes_siniflandir(self):
        sonuc=NavieBayes.predict(self.ui.le_metin.toPlainText(),NavieBayes.fit(self.navie_bayes_data_set))#girilen metin navie bayes ile siniflandiriliyor ve sonuc aktariliyor
        sonuc=sonuc.upper() #sonuc buyuk harfe cevriliyor
        self.ui.lbl_navie_sonuc.setText(sonuc) #sonuc ui katmanindaki labele set ediliyor
    
    def verileri_tabloya_dok(self,table_value,table_name):
        num_rows=len(table_value) #tablonun satir sayisi aliniyor
        num_column=len(table_value[0]) #tablonun sutun sayisi aliniyor
        table_name.clear()        #tabloda onceden deger var ise temizleniyor
        table_name.setColumnCount(num_column) #tablonun sutun sayisi set ediliyor
        table_name.setRowCount(num_rows) #tablonun satir sayisi set ediliyor
        for rowNumber,row in enumerate(table_value):#tabloya eklenecek deger satir satir ve
            for columnNumber in range(0,len(table_value[0])):#sutun sutun okunuyor
                table_name.setItem(rowNumber,columnNumber,QtWidgets.QTableWidgetItem(str(row[columnNumber]))) #okunan degerler tabloya set ediliyor

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())