# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdicionarClientes.ui'
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
class Ui_AddClientes(object):
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
        self.Edit_CEP = QLineEdit(self.centralwidget)
        self.Edit_CEP.setObjectName(u"Edit_CEP")
        self.Edit_CEP.setGeometry(QRect(210, 240, 181, 51))
        self.Edit_CEP.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_CEP.setAlignment(Qt.AlignCenter)
        self.Edit_Enderecos = QLineEdit(self.centralwidget)
        self.Edit_Enderecos.setObjectName(u"Edit_Enderecos")
        self.Edit_Enderecos.setGeometry(QRect(410, 240, 181, 51))
        self.Edit_Enderecos.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_Enderecos.setAlignment(Qt.AlignCenter)
        self.Edit_Telefone = QLineEdit(self.centralwidget)
        self.Edit_Telefone.setObjectName(u"Edit_Telefone")
        self.Edit_Telefone.setGeometry(QRect(410, 150, 181, 51))
        self.Edit_Telefone.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_Telefone.setAlignment(Qt.AlignCenter)
        self.Edit_NomeEmpresa = QLineEdit(self.centralwidget)
        self.Edit_NomeEmpresa.setObjectName(u"Edit_NomeEmpresa")
        self.Edit_NomeEmpresa.setGeometry(QRect(210, 150, 181, 51))
        self.Edit_NomeEmpresa.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_NomeEmpresa.setAlignment(Qt.AlignCenter)
        self.Label_NomeEmpresa = QLabel(self.centralwidget)
        self.Label_NomeEmpresa.setObjectName(u"Label_NomeEmpresa")
        self.Label_NomeEmpresa.setGeometry(QRect(220, 130, 161, 16))
        font1 = QFont()
        font1.setBold(True)
        self.Label_NomeEmpresa.setFont(font1)
        self.Label_Telefone = QLabel(self.centralwidget)
        self.Label_Telefone.setObjectName(u"Label_Telefone")
        self.Label_Telefone.setGeometry(QRect(420, 130, 161, 16))
        self.Label_Telefone.setFont(font1)
        self.Label_Endereco = QLabel(self.centralwidget)
        self.Label_Endereco.setObjectName(u"Label_Endereco")
        self.Label_Endereco.setGeometry(QRect(420, 220, 161, 16))
        self.Label_Endereco.setFont(font1)
        self.Label_Cep = QLabel(self.centralwidget)
        self.Label_Cep.setObjectName(u"Label_Cep")
        self.Label_Cep.setGeometry(QRect(220, 220, 161, 16))
        self.Label_Cep.setFont(font1)
        self.Label_Email = QLabel(self.centralwidget)
        self.Label_Email.setObjectName(u"Label_Email")
        self.Label_Email.setGeometry(QRect(220, 310, 161, 16))
        self.Label_Email.setFont(font1)
        self.Label_InscricaoEstadual = QLabel(self.centralwidget)
        self.Label_InscricaoEstadual.setObjectName(u"Label_InscricaoEstadual")
        self.Label_InscricaoEstadual.setGeometry(QRect(420, 310, 161, 16))
        self.Label_InscricaoEstadual.setFont(font1)
        self.logo_empresa = QLabel(self.centralwidget)
        self.logo_empresa.setObjectName(u"logo_empresa")
        self.logo_empresa.setGeometry(QRect(20, 10, 161, 121))
        self.logo_empresa.setPixmap(QPixmap("./imgs/logo.png"))
        self.Edit_CNPJ = QLineEdit(self.centralwidget)
        self.Edit_CNPJ.setObjectName(u"Edit_CNPJ")
        self.Edit_CNPJ.setGeometry(QRect(310, 420, 181, 51))
        self.Edit_CNPJ.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_CNPJ.setAlignment(Qt.AlignCenter)
        self.Label_Email_2 = QLabel(self.centralwidget)
        self.Label_Email_2.setObjectName(u"Label_Email_2")
        self.Label_Email_2.setGeometry(QRect(320, 400, 161, 16))
        self.Label_Email_2.setFont(font1)
        self.Label_Aviso = QLabel(self.centralwidget)
        self.Label_Aviso.setObjectName(u"Label_Aviso")
        self.Label_Aviso.setGeometry(QRect(290, 30, 221, 61))
        self.Label_Aviso.setFont(font1)
        self.Btn_Voltar = QPushButton(self.centralwidget)
        self.Btn_Voltar.setObjectName(u"Btn_Voltar")
        self.Btn_Voltar.setGeometry(QRect(690, 560, 101, 31))
        self.Btn_Voltar.setFont(font)
        self.Btn_Voltar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Edit_Email = QLineEdit(self.centralwidget)
        self.Edit_Email.setObjectName(u"Edit_Email")
        self.Edit_Email.setGeometry(QRect(210, 330, 181, 51))
        self.Edit_Email.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_Email.setAlignment(Qt.AlignCenter)
        self.Edit_InscricaoEstadual = QLineEdit(self.centralwidget)
        self.Edit_InscricaoEstadual.setObjectName(u"Edit_InscricaoEstadual")
        self.Edit_InscricaoEstadual.setGeometry(QRect(410, 330, 181, 51))
        self.Edit_InscricaoEstadual.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_InscricaoEstadual.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Avancar.setText(QCoreApplication.translate("MainWindow", u"AVAN\u00c7AR", None))
        self.Edit_CEP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Edit_Enderecos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Edit_Telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Edit_NomeEmpresa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Label_NomeEmpresa.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">NOME EMPRESA</span></p></body></html>", None))
        self.Label_Telefone.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">TELEFONE</span></p></body></html>", None))
        self.Label_Endereco.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">ENDERE\u00c7O</span></p></body></html>", None))
        self.Label_Cep.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">CEP</span></p></body></html>", None))
        self.Label_Email.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">EMAIL</span></p></body></html>", None))
        self.Label_InscricaoEstadual.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">INSCRI\u00c7\u00c3O ESTADUAL</span></p></body></html>", None))
        self.logo_empresa.setText("")
        self.Edit_CNPJ.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Label_Email_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">CNPJ</span></p></body></html>", None))
        self.Label_Aviso.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.Btn_Voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.Edit_Email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Edit_InscricaoEstadual.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
    # retranslateUi

