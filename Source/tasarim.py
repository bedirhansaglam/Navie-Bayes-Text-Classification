# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tasarim.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gb_navie = QGroupBox(self.centralwidget)
        self.gb_navie.setObjectName(u"gb_navie")
        self.gb_navie.setGeometry(QRect(0, 0, 1280, 720))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75);
        self.gb_navie.setFont(font)
        self.gb_navie.setStyleSheet(u"#gb_navie{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_navie::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}")
        self.gb_navie_create_dataset = QGroupBox(self.gb_navie)
        self.gb_navie_create_dataset.setObjectName(u"gb_navie_create_dataset")
        self.gb_navie_create_dataset.setGeometry(QRect(10, 30, 361, 621))
        self.tbl_navie_data_set = QTableWidget(self.gb_navie_create_dataset)
        self.tbl_navie_data_set.setObjectName(u"tbl_navie_data_set")
        self.tbl_navie_data_set.setGeometry(QRect(20, 170, 301, 431))
        font1 = QFont()
        font1.setPointSize(12)
        self.tbl_navie_data_set.setFont(font1)
        self.groupBox_3 = QGroupBox(self.gb_navie_create_dataset)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 10, 301, 151))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75);
        self.groupBox_3.setFont(font2)
        self.le_navie_kelime = QLineEdit(self.groupBox_3)
        self.le_navie_kelime.setObjectName(u"le_navie_kelime")
        self.le_navie_kelime.setGeometry(QRect(100, 30, 171, 20))
        self.le_navie_kelime.setFont(font1)
        self.label_59 = QLabel(self.groupBox_3)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(20, 25, 61, 31))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75);
        self.label_59.setFont(font3)
        self.le_naive_kategori = QLineEdit(self.groupBox_3)
        self.le_naive_kategori.setObjectName(u"le_naive_kategori")
        self.le_naive_kategori.setGeometry(QRect(100, 65, 171, 20))
        self.le_naive_kategori.setFont(font1)
        self.label_60 = QLabel(self.groupBox_3)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(20, 60, 71, 31))
        self.label_60.setFont(font3)
        self.pb_navie_veriekle = QPushButton(self.groupBox_3)
        self.pb_navie_veriekle.setObjectName(u"pb_navie_veriekle")
        self.pb_navie_veriekle.setGeometry(QRect(180, 90, 91, 31))
        self.pb_navie_veriekle.setFont(font)
        self.pb_navie_veriekle.setStyleSheet(u"QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}")
        self.groupBox_4 = QGroupBox(self.gb_navie)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(390, 20, 671, 631))
        self.groupBox_4.setFont(font)
        self.label_61 = QLabel(self.groupBox_4)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(10, 30, 151, 31))
        self.label_61.setFont(font3)
        self.pb_navie_siniflandir = QPushButton(self.groupBox_4)
        self.pb_navie_siniflandir.setObjectName(u"pb_navie_siniflandir")
        self.pb_navie_siniflandir.setGeometry(QRect(490, 390, 151, 41))
        self.pb_navie_siniflandir.setFont(font)
        self.pb_navie_siniflandir.setStyleSheet(u"QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}")
        self.lbl_navie_sonuc = QLabel(self.groupBox_4)
        self.lbl_navie_sonuc.setObjectName(u"lbl_navie_sonuc")
        self.lbl_navie_sonuc.setGeometry(QRect(160, 400, 141, 31))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75);
        self.lbl_navie_sonuc.setFont(font4)
        self.le_metin = QPlainTextEdit(self.groupBox_4)
        self.le_metin.setObjectName(u"le_metin")
        self.le_metin.setGeometry(QRect(10, 60, 631, 321))
        self.le_metin.setFont(font1)
        self.lbl_navie_sonuc_2 = QLabel(self.groupBox_4)
        self.lbl_navie_sonuc_2.setObjectName(u"lbl_navie_sonuc_2")
        self.lbl_navie_sonuc_2.setGeometry(QRect(20, 400, 141, 31))
        self.lbl_navie_sonuc_2.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Taylan Kundak\u00e7\u0131 & Enes Eren", None))
        self.gb_navie.setTitle(QCoreApplication.translate("MainWindow", u"NAV\u0130E BAYES", None))
        self.gb_navie_create_dataset.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Yeni Kelime veya Kategori Ekle", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Kelime :", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Kategori :", None))
        self.pb_navie_veriekle.setText(QCoreApplication.translate("MainWindow", u"Ekle", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Metin S\u0131n\u0131fland\u0131rma", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Metin Giriniz :", None))
        self.pb_navie_siniflandir.setText(QCoreApplication.translate("MainWindow", u"S\u0131n\u0131fland\u0131r", None))
        self.lbl_navie_sonuc.setText("")
        self.lbl_navie_sonuc_2.setText(QCoreApplication.translate("MainWindow", u"Kategori :", None))
    # retranslateUi

