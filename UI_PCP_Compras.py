# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PCP_Check_Compras.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QWidget)
import os
import sys


def resource_path(relative_path):
    """Obtem o caminho absoluto para o recurso."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class UI_PCP_Compras(object):
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
        self.logo_empresa.setGeometry(QRect(30, 30, 151, 121))
        self.logo_empresa.setPixmap(QPixmap("./imgs/logo.png"))
        self.Btn_Voltar_os = QPushButton(self.centralwidget)
        self.Btn_Voltar_os.setObjectName(u"Btn_Voltar_os")
        self.Btn_Voltar_os.setGeometry(QRect(690, 560, 101, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Btn_Voltar_os.setFont(font)
        self.Btn_Voltar_os.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Vendas = QPushButton(self.centralwidget)
        self.Btn_Vendas.setObjectName(u"Btn_Vendas")
        self.Btn_Vendas.setGeometry(QRect(50, 200, 121, 51))
        self.Btn_Vendas.setFont(font)
        self.Btn_Vendas.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Engenharia = QPushButton(self.centralwidget)
        self.Btn_Engenharia.setObjectName(u"Btn_Engenharia")
        self.Btn_Engenharia.setGeometry(QRect(50, 290, 121, 51))
        self.Btn_Engenharia.setFont(font)
        self.Btn_Engenharia.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_PCP = QPushButton(self.centralwidget)
        self.Btn_PCP.setObjectName(u"Btn_PCP")
        self.Btn_PCP.setGeometry(QRect(50, 380, 121, 51))
        self.Btn_PCP.setFont(font)
        self.Btn_PCP.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Compras = QPushButton(self.centralwidget)
        self.Btn_Compras.setObjectName(u"Btn_Compras")
        self.Btn_Compras.setGeometry(QRect(50, 470, 121, 51))
        self.Btn_Compras.setFont(font)
        self.Btn_Compras.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 100, 191, 41))
        font1 = QFont()
        font1.setPointSize(21)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.treeWidget_2 = QTreeWidget(self.centralwidget)
        font2 = QFont()
        font2.setBold(True)
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(8, Qt.AlignCenter);
        __qtreewidgetitem.setFont(8, font2);
        __qtreewidgetitem.setTextAlignment(7, Qt.AlignCenter);
        __qtreewidgetitem.setFont(7, font2);
        __qtreewidgetitem.setTextAlignment(6, Qt.AlignCenter);
        __qtreewidgetitem.setFont(6, font3);
        __qtreewidgetitem.setTextAlignment(5, Qt.AlignCenter);
        __qtreewidgetitem.setFont(5, font2);
        __qtreewidgetitem.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem.setFont(4, font2);
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem.setFont(3, font2);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setFont(2, font2);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setFont(1, font2);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, font2);
        self.treeWidget_2.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.setGeometry(QRect(230, 190, 521, 341))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_empresa.setText("")
        self.Btn_Voltar_os.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.Btn_Vendas.setText(QCoreApplication.translate("MainWindow", u"Vendas", None))
        self.Btn_Engenharia.setText(QCoreApplication.translate("MainWindow", u"Engenharia", None))
        self.Btn_PCP.setText(QCoreApplication.translate("MainWindow", u"Pcp", None))
        self.Btn_Compras.setText(QCoreApplication.translate("MainWindow", u"Compras", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">COMPRAS</span></p></body></html>", None))
        ___qtreewidgetitem = self.treeWidget_2.headerItem()
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Atualiza\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Previs\u00e3o Entrega", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Cnpj Fornecedor", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Transporte", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Unidade", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Mat\u00e9ria Prima", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"OS", None));
    # retranslateUi

