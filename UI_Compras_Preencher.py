# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Compras_Itens.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import os
import sys

def resource_path(relative_path):
    """Obtem o caminho absoluto para o recurso."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class UI_Compras_Preencher(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"background-color:rgb(0, 74, 112)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Btn_Avancar = QPushButton(self.centralwidget)
        self.Btn_Avancar.setObjectName(u"Btn_Avancar")
        self.Btn_Avancar.setGeometry(QRect(310, 530, 181, 61))
        self.Btn_Avancar.setMinimumSize(QSize(181, 61))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Btn_Avancar.setFont(font)
        self.Btn_Avancar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.logo_empresa = QLabel(self.centralwidget)
        self.logo_empresa.setObjectName(u"logo_empresa")
        self.logo_empresa.setGeometry(QRect(320, 20, 161, 121))
        self.logo_empresa.setPixmap(QPixmap("./imgs/logo.png"))
        self.Btn_Voltar = QPushButton(self.centralwidget)
        self.Btn_Voltar.setObjectName(u"Btn_Voltar")
        self.Btn_Voltar.setGeometry(QRect(690, 560, 101, 31))
        self.Btn_Voltar.setFont(font)
        self.Btn_Voltar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Edit_Valor = QLineEdit(self.centralwidget)
        self.Edit_Valor.setObjectName(u"Edit_Valor")
        self.Edit_Valor.setGeometry(QRect(420, 170, 181, 51))
        self.Edit_Valor.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_Valor.setAlignment(Qt.AlignCenter)
        self.Label_InscricaoEstadual = QLabel(self.centralwidget)
        self.Label_InscricaoEstadual.setObjectName(u"Label_InscricaoEstadual")
        self.Label_InscricaoEstadual.setGeometry(QRect(430, 150, 161, 16))
        font1 = QFont()
        font1.setBold(True)
        self.Label_InscricaoEstadual.setFont(font1)
        self.Edit_Quantidade = QLineEdit(self.centralwidget)
        self.Edit_Quantidade.setObjectName(u"Edit_Quantidade")
        self.Edit_Quantidade.setGeometry(QRect(210, 270, 181, 51))
        self.Edit_Quantidade.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_Quantidade.setAlignment(Qt.AlignCenter)
        self.Label_InscricaoEstadual_2 = QLabel(self.centralwidget)
        self.Label_InscricaoEstadual_2.setObjectName(u"Label_InscricaoEstadual_2")
        self.Label_InscricaoEstadual_2.setGeometry(QRect(220, 250, 161, 16))
        self.Label_InscricaoEstadual_2.setFont(font1)
        self.Edit_Nome = QLineEdit(self.centralwidget)
        self.Edit_Nome.setObjectName(u"Edit_Nome")
        self.Edit_Nome.setGeometry(QRect(210, 170, 181, 51))
        self.Edit_Nome.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_Nome.setAlignment(Qt.AlignCenter)
        self.Label_InscricaoEstadual_3 = QLabel(self.centralwidget)
        self.Label_InscricaoEstadual_3.setObjectName(u"Label_InscricaoEstadual_3")
        self.Label_InscricaoEstadual_3.setGeometry(QRect(220, 150, 161, 16))
        self.Label_InscricaoEstadual_3.setFont(font1)
        self.Edit_Previsao = QLineEdit(self.centralwidget)
        self.Edit_Previsao.setObjectName(u"Edit_Previsao")
        self.Edit_Previsao.setGeometry(QRect(420, 370, 181, 51))
        self.Edit_Previsao.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_Previsao.setAlignment(Qt.AlignCenter)
        self.Label_InscricaoEstadual_4 = QLabel(self.centralwidget)
        self.Label_InscricaoEstadual_4.setObjectName(u"Label_InscricaoEstadual_4")
        self.Label_InscricaoEstadual_4.setGeometry(QRect(430, 350, 161, 16))
        self.Label_InscricaoEstadual_4.setFont(font1)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(320, 450, 181, 21))
        self.comboBox.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 5px;\n"
"")
        self.Label_InscricaoEstadual_5 = QLabel(self.centralwidget)
        self.Label_InscricaoEstadual_5.setObjectName(u"Label_InscricaoEstadual_5")
        self.Label_InscricaoEstadual_5.setGeometry(QRect(330, 430, 161, 16))
        self.Label_InscricaoEstadual_5.setFont(font1)
        self.Edit_Previsao_2 = QLineEdit(self.centralwidget)
        self.Edit_Previsao_2.setObjectName(u"Edit_Previsao_2")
        self.Edit_Previsao_2.setGeometry(QRect(210, 370, 181, 51))
        self.Edit_Previsao_2.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_Previsao_2.setAlignment(Qt.AlignCenter)
        self.Label_InscricaoEstadual_6 = QLabel(self.centralwidget)
        self.Label_InscricaoEstadual_6.setObjectName(u"Label_InscricaoEstadual_6")
        self.Label_InscricaoEstadual_6.setGeometry(QRect(220, 350, 161, 16))
        self.Label_InscricaoEstadual_6.setFont(font1)
        self.Edit_Unidade = QLineEdit(self.centralwidget)
        self.Edit_Unidade.setObjectName(u"Edit_Unidade")
        self.Edit_Unidade.setGeometry(QRect(420, 270, 181, 51))
        self.Edit_Unidade.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_Unidade.setAlignment(Qt.AlignCenter)
        self.Label_InscricaoEstadual_7 = QLabel(self.centralwidget)
        self.Label_InscricaoEstadual_7.setObjectName(u"Label_InscricaoEstadual_7")
        self.Label_InscricaoEstadual_7.setGeometry(QRect(430, 250, 161, 16))
        self.Label_InscricaoEstadual_7.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Avancar.setText(QCoreApplication.translate("MainWindow", u"AVAN\u00c7AR", None))
        self.logo_empresa.setText("")
        self.Btn_Voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.Edit_Valor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Label_InscricaoEstadual.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">VALOR</span></p></body></html>", None))
        self.Edit_Quantidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Label_InscricaoEstadual_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">QUANTIDADE</span></p></body></html>", None))
        self.Edit_Nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Label_InscricaoEstadual_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">NOME</span></p></body></html>", None))
        self.Edit_Previsao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Label_InscricaoEstadual_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">PREVIS\u00c3O ENTREGA</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"EMPRESA", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"FORNECEDOR", None))

        self.Label_InscricaoEstadual_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">TRANSPORTE</span></p></body></html>", None))
        self.Edit_Previsao_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Label_InscricaoEstadual_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">CNPJ</span></p></body></html>", None))
        self.Edit_Unidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Label_InscricaoEstadual_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">UNIDADE</span></p></body></html>", None))
    # retranslateUi

