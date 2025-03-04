# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Engenharia_Menu.ui'
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


class Ui_MP_Engenharia(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"background-color:rgb(0, 74, 112)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Btn_Adicionar = QPushButton(self.centralwidget)
        self.Btn_Adicionar.setObjectName(u"Btn_Adicionar")
        self.Btn_Adicionar.setGeometry(QRect(310, 530, 181, 61))
        self.Btn_Adicionar.setMinimumSize(QSize(181, 61))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Btn_Adicionar.setFont(font)
        self.Btn_Adicionar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.logo_empresa = QLabel(self.centralwidget)
        self.logo_empresa.setObjectName(u"logo_empresa")
        self.logo_empresa.setGeometry(QRect(310, 40, 161, 121))
        self.logo_empresa.setPixmap(QPixmap("./imgs/logo.png"))
        self.Btn_Voltar = QPushButton(self.centralwidget)
        self.Btn_Voltar.setObjectName(u"Btn_Voltar")
        self.Btn_Voltar.setGeometry(QRect(690, 560, 101, 31))
        self.Btn_Voltar.setFont(font)
        self.Btn_Voltar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Edit_OS = QLineEdit(self.centralwidget)
        self.Edit_OS.setObjectName(u"Edit_OS")
        self.Edit_OS.setGeometry(QRect(170, 230, 221, 51))
        self.Edit_OS.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8);\n"
"border-radius: 15px")
        self.Edit_OS.setAlignment(Qt.AlignCenter)
        self.Edit_CodigoItem = QLineEdit(self.centralwidget)
        self.Edit_CodigoItem.setObjectName(u"Edit_CodigoItem")
        self.Edit_CodigoItem.setGeometry(QRect(410, 230, 221, 51))
        self.Edit_CodigoItem.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8);\n"
"border-radius: 15px")
        self.Edit_CodigoItem.setAlignment(Qt.AlignCenter)
        self.Edit_Unidade = QLineEdit(self.centralwidget)
        self.Edit_Unidade.setObjectName(u"Edit_Unidade")
        self.Edit_Unidade.setGeometry(QRect(290, 410, 221, 51))
        self.Edit_Unidade.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8);\n"
"border-radius: 15px")
        self.Edit_Unidade.setAlignment(Qt.AlignCenter)
        self.Edit_QuantiaMP = QLineEdit(self.centralwidget)
        self.Edit_QuantiaMP.setObjectName(u"Edit_QuantiaMP")
        self.Edit_QuantiaMP.setGeometry(QRect(410, 320, 221, 51))
        self.Edit_QuantiaMP.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8);\n"
"border-radius: 15px")
        self.Edit_QuantiaMP.setAlignment(Qt.AlignCenter)
        self.Edit_Codigo_MP = QLineEdit(self.centralwidget)
        self.Edit_Codigo_MP.setObjectName(u"Edit_Codigo_MP")
        self.Edit_Codigo_MP.setGeometry(QRect(170, 320, 221, 51))
        self.Edit_Codigo_MP.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8);\n"
"border-radius: 15px")
        self.Edit_Codigo_MP.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 280, 201, 31))
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 190, 201, 31))
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 280, 201, 31))
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 380, 201, 21))
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(420, 190, 201, 31))
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.Btn_Chechar = QPushButton(self.centralwidget)
        self.Btn_Chechar.setObjectName(u"Btn_Chechar")
        self.Btn_Chechar.setGeometry(QRect(690, 520, 101, 31))
        self.Btn_Chechar.setFont(font)
        self.Btn_Chechar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Verify = QPushButton(self.centralwidget)
        self.Btn_Verify.setObjectName(u"Btn_Verify")
        self.Btn_Verify.setGeometry(QRect(10, 30, 181, 61))
        self.Btn_Verify.setFont(font)
        self.Btn_Verify.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 490, 201, 31))
        self.label_8.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Adicionar.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR", None))
        self.logo_empresa.setText("")
        self.Btn_Voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">C\u00d3DIGO DA MAT\u00c9RIA PRIMA</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">OS</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">QUANTIDADE DA MAT\u00c9RIA PRIMA</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">UNIDADE</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">C\u00d3DIGO DO ITEM</span></p></body></html>", None))
        self.Btn_Chechar.setText(QCoreApplication.translate("MainWindow", u"CHECAR", None))
        self.Btn_Verify.setText(QCoreApplication.translate("MainWindow", u"VERIFICAR MAT\u00c9RIA PRIMA", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
    # retranslateUi

