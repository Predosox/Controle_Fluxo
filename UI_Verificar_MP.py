# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VerifyMP.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QWidget)
import os
import sys


def resource_path(relative_path):
    """Obtem o caminho absoluto para o recurso."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
class Ui_Verificar_MP(object):
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
        self.logo_empresa.setGeometry(QRect(20, 10, 161, 121))
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
        self.Edit_Nome = QLineEdit(self.centralwidget)
        self.Edit_Nome.setObjectName(u"Edit_Nome")
        self.Edit_Nome.setGeometry(QRect(120, 180, 131, 21))
        self.Edit_Nome.setStyleSheet(u"color: white;")
        self.Edit_Nome.setAlignment(Qt.AlignCenter)
        self.Btn_Consultar = QPushButton(self.centralwidget)
        self.Btn_Consultar.setObjectName(u"Btn_Consultar")
        self.Btn_Consultar.setGeometry(QRect(250, 180, 61, 21))
        self.Btn_Consultar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 50, 401, 61))
        font1 = QFont()
        font1.setPointSize(50)
        font1.setBold(True)
        self.label.setFont(font1)
        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, font);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(120, 200, 561, 251))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.treeWidget.setFont(font2)
        self.treeWidget.setStyleSheet(u"\n"
"background-color:rgb(255, 166, 64)")
        self.Btn_Adicionar = QPushButton(self.centralwidget)
        self.Btn_Adicionar.setObjectName(u"Btn_Adicionar")
        self.Btn_Adicionar.setGeometry(QRect(120, 460, 101, 31))
        self.Btn_Adicionar.setFont(font)
        self.Btn_Adicionar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Remover = QPushButton(self.centralwidget)
        self.Btn_Remover.setObjectName(u"Btn_Remover")
        self.Btn_Remover.setGeometry(QRect(230, 460, 101, 31))
        self.Btn_Remover.setFont(font)
        self.Btn_Remover.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
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
        self.Edit_Nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome da Mat\u00e9ria Prima", None))
        self.Btn_Consultar.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">CONSULTAR MAT\u00c9RIA PRIMA</span></p></body></html>", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"C\u00d3DIGO", None));
        self.Btn_Adicionar.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR", None))
        self.Btn_Remover.setText(QCoreApplication.translate("MainWindow", u"REMOVER", None))
    # retranslateUi

