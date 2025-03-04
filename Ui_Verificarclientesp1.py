# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vendas_OS.ui'
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
class Ui_Verify1(object):
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
        self.Edit_OS = QLineEdit(self.centralwidget)
        self.Edit_OS.setObjectName(u"Edit_OS")
        self.Edit_OS.setGeometry(QRect(310, 260, 181, 51))
        self.Edit_OS.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); /* Cor de fundo azul */\n"
"border-radius: 15px; /* Arredondamento das bordas *")
        self.Edit_OS.setAlignment(Qt.AlignCenter)
        self.Label_Telefone = QLabel(self.centralwidget)
        self.Label_Telefone.setObjectName(u"Label_Telefone")
        self.Label_Telefone.setGeometry(QRect(320, 240, 161, 16))
        font1 = QFont()
        font1.setBold(True)
        self.Label_Telefone.setFont(font1)
        self.logo_empresa = QLabel(self.centralwidget)
        self.logo_empresa.setObjectName(u"logo_empresa")
        self.logo_empresa.setGeometry(QRect(20, 10, 161, 121))
        self.logo_empresa.setPixmap(QPixmap("./imgs/logo.png"))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Avancar.setText(QCoreApplication.translate("MainWindow", u"VERIFICAR", None))
        self.Edit_OS.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.Label_Telefone.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">CNPJ:</span></p></body></html>", None))
        self.logo_empresa.setText("")
        self.Label_Aviso.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.Btn_Voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
    # retranslateUi

