# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdicionarItens.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import os
import sys


def resource_path(relative_path):
    """Obtem o caminho absoluto para o recurso."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
class Ui_addspecs(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"background-color:rgb(0, 74, 112);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Btn_Adicionar = QPushButton(self.centralwidget)
        self.Btn_Adicionar.setObjectName(u"Btn_Adicionar")
        self.Btn_Adicionar.setGeometry(QRect(310, 530, 181, 61))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Btn_Adicionar.setFont(font)
        self.Btn_Adicionar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Edit_unidade = QLineEdit(self.centralwidget)
        self.Edit_unidade.setObjectName(u"Edit_unidade")
        self.Edit_unidade.setGeometry(QRect(310, 340, 181, 51))
        self.Edit_unidade.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas */\n"
"")
        self.Edit_unidade.setAlignment(Qt.AlignCenter)
        self.Edit_quantidade = QLineEdit(self.centralwidget)
        self.Edit_quantidade.setObjectName(u"Edit_quantidade")
        self.Edit_quantidade.setGeometry(QRect(310, 260, 181, 51))
        self.Edit_quantidade.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas */\n"
"")
        self.Edit_quantidade.setAlignment(Qt.AlignCenter)
        self.Edit_desc = QLineEdit(self.centralwidget)
        self.Edit_desc.setObjectName(u"Edit_desc")
        self.Edit_desc.setGeometry(QRect(310, 180, 181, 51))
        self.Edit_desc.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas */\n"
"")
        self.Edit_desc.setAlignment(Qt.AlignCenter)
        self.Edit_codigo = QLineEdit(self.centralwidget)
        self.Edit_codigo.setObjectName(u"Edit_codigo")
        self.Edit_codigo.setGeometry(QRect(310, 100, 181, 51))
        self.Edit_codigo.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas */\n"
"")
        self.Edit_codigo.setAlignment(Qt.AlignCenter)
        self.Edit_dataprevista = QLineEdit(self.centralwidget)
        self.Edit_dataprevista.setObjectName(u"Edit_dataprevista")
        self.Edit_dataprevista.setGeometry(QRect(310, 420, 181, 51))
        self.Edit_dataprevista.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas */\n"
"")
        self.Edit_dataprevista.setAlignment(Qt.AlignCenter)
        self.Label_codigo = QLabel(self.centralwidget)
        self.Label_codigo.setObjectName(u"Label_codigo")
        self.Label_codigo.setGeometry(QRect(320, 80, 161, 16))
        self.Label_desc = QLabel(self.centralwidget)
        self.Label_desc.setObjectName(u"Label_desc")
        self.Label_desc.setGeometry(QRect(320, 160, 161, 16))
        self.Label_ItensDiferentes = QLabel(self.centralwidget)
        self.Label_ItensDiferentes.setObjectName(u"Label_ItensDiferentes")
        self.Label_ItensDiferentes.setGeometry(QRect(320, 240, 161, 16))
        self.Label_unidade = QLabel(self.centralwidget)
        self.Label_unidade.setObjectName(u"Label_unidade")
        self.Label_unidade.setGeometry(QRect(320, 320, 161, 16))
        self.Label_data = QLabel(self.centralwidget)
        self.Label_data.setObjectName(u"Label_data")
        self.Label_data.setGeometry(QRect(320, 400, 161, 16))
        self.logo_empresa = QLabel(self.centralwidget)
        self.logo_empresa.setObjectName(u"logo_empresa")
        self.logo_empresa.setGeometry(QRect(-20, -10, 161, 121))
        self.logo_empresa.setPixmap(QPixmap("./imgs/logo.png"))
        self.Btn_Voltar = QPushButton(self.centralwidget)
        self.Btn_Voltar.setObjectName(u"Btn_Voltar")
        self.Btn_Voltar.setGeometry(QRect(690, 560, 101, 31))
        self.Btn_Voltar.setFont(font)
        self.Btn_Voltar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.label_aviso = QLabel(self.centralwidget)
        self.label_aviso.setObjectName(u"label_aviso")
        self.label_aviso.setGeometry(QRect(310, 30, 181, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Adicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.Edit_unidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite aqui", None))
        self.Edit_quantidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite aqui", None))
        self.Edit_desc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite aqui", None))
        self.Edit_codigo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite aqui", None))
        self.Edit_dataprevista.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite aqui", None))
        self.Label_codigo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">C\u00d3DIGO DO ITEM</span></p></body></html>", None))
        self.Label_desc.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">DESCRI\u00c7\u00c3O</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.Label_ItensDiferentes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">QUANTIDADE</span></p></body></html>", None))
        self.Label_unidade.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">UNIDADE</span></p></body></html>", None))
        self.Label_data.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">DATA PREVISTA</span></p></body></html>", None))
        self.logo_empresa.setText("")
        self.Btn_Voltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_aviso.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

