# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vendas_Menu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import os
import sys


def resource_path(relative_path):
    """Obtem o caminho absoluto para o recurso."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
class Ui_MenuVendas(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"background-color:rgb(0, 74, 112)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo_empresa = QLabel(self.centralwidget)
        self.logo_empresa.setObjectName(u"logo_empresa")
        self.logo_empresa.setGeometry(QRect(340, 80, 151, 121))
        self.logo_empresa.setPixmap(QPixmap("./imgs/logo.png"))
        self.Btn_Voltar = QPushButton(self.centralwidget)
        self.Btn_Voltar.setObjectName(u"Btn_Voltar")
        self.Btn_Voltar.setGeometry(QRect(690, 560, 101, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Btn_Voltar.setFont(font)
        self.Btn_Voltar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_AddClientes = QPushButton(self.centralwidget)
        self.Btn_AddClientes.setObjectName(u"Btn_AddClientes")
        self.Btn_AddClientes.setGeometry(QRect(270, 260, 261, 71))
        self.Btn_AddClientes.setFont(font)
        self.Btn_AddClientes.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Verify = QPushButton(self.centralwidget)
        self.Btn_Verify.setObjectName(u"Btn_Verify")
        self.Btn_Verify.setGeometry(QRect(270, 440, 261, 71))
        self.Btn_Verify.setFont(font)
        self.Btn_Verify.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_AddItens = QPushButton(self.centralwidget)
        self.Btn_AddItens.setObjectName(u"Btn_AddItens")
        self.Btn_AddItens.setGeometry(QRect(270, 350, 261, 71))
        self.Btn_AddItens.setFont(font)
        self.Btn_AddItens.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Check = QPushButton(self.centralwidget)
        self.Btn_Check.setObjectName(u"Btn_Check")
        self.Btn_Check.setGeometry(QRect(690, 520, 101, 31))
        self.Btn_Check.setFont(font)
        self.Btn_Check.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_empresa.setText("")
        self.Btn_Voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.Btn_AddClientes.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR CLIENTES", None))
        self.Btn_Verify.setText(QCoreApplication.translate("MainWindow", u"VERIFICAR CLIENTES", None))
        self.Btn_AddItens.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR ITENS", None))
        self.Btn_Check.setText(QCoreApplication.translate("MainWindow", u"CHECAR", None))
    # retranslateUi

