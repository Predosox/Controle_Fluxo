# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'REMOVER_MP.ui'
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
class UI_REMOVE_MP(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 74, 112);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Edit_CodigoMP = QLineEdit(self.centralwidget)
        self.Edit_CodigoMP.setObjectName(u"Edit_CodigoMP")
        self.Edit_CodigoMP.setGeometry(QRect(290, 290, 221, 51))
        self.Edit_CodigoMP.setStyleSheet(u"background-color:rgba(214, 214, 214,0.8); \n"
"border-radius: 15px;")
        self.Edit_CodigoMP.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 60, 161, 121))
        self.logo_empresa.setPixmap(QPixmap("./imgs/logo.png"))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 250, 201, 31))
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.Btn_Adicionar = QPushButton(self.centralwidget)
        self.Btn_Adicionar.setObjectName(u"Btn_Adicionar")
        self.Btn_Adicionar.setGeometry(QRect(310, 520, 181, 61))
        font = QFont()
        font.setBold(True)
        self.Btn_Adicionar.setFont(font)
        self.Btn_Adicionar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Voltar = QPushButton(self.centralwidget)
        self.Btn_Voltar.setObjectName(u"Btn_Voltar")
        self.Btn_Voltar.setGeometry(QRect(680, 550, 101, 31))
        self.Btn_Voltar.setFont(font)
        self.Btn_Voltar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(280, 480, 241, 31))
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_5.raise_()
        self.Edit_CodigoMP.raise_()
        self.label.raise_()
        self.Btn_Adicionar.raise_()
        self.Btn_Voltar.raise_()
        self.label_8.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Edit_CodigoMP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">C\u00d3DIGO DA MAT\u00c9RIA PRIMA</span></p></body></html>", None))
        self.Btn_Adicionar.setText(QCoreApplication.translate("MainWindow", u"REMOVER", None))
        self.Btn_Voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

