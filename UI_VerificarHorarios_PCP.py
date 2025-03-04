# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VerificarSituacao_pcp.ui'
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
class UI_VerificarHorarios_PCP(object):
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 50, 401, 61))
        font1 = QFont()
        font1.setPointSize(50)
        font1.setBold(True)
        self.label.setFont(font1)
        self.treeWidget = QTreeWidget(self.centralwidget)
        font2 = QFont()
        font2.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
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
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(120, 200, 561, 251))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.treeWidget.setFont(font3)
        self.treeWidget.setStyleSheet(u"\n"
"background-color:rgb(255, 166, 64)")
        self.Edit_Quantidade = QLineEdit(self.centralwidget)
        self.Edit_Quantidade.setObjectName(u"Edit_Quantidade")
        self.Edit_Quantidade.setGeometry(QRect(120, 160, 101, 31))
        self.Edit_Quantidade.setStyleSheet(u"\n"
"color: white;\n"
"")
        self.Edit_Quantidade.setAlignment(Qt.AlignCenter)
        self.Btn_Estoque = QPushButton(self.centralwidget)
        self.Btn_Estoque.setObjectName(u"Btn_Estoque")
        self.Btn_Estoque.setGeometry(QRect(230, 160, 91, 31))
        self.Btn_Estoque.setFont(font)
        self.Btn_Estoque.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">HOR\u00c1RIOS</span></p></body></html>", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Compras", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"PCP", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Engenharia", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Vendas", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"OS", None));
        self.Edit_Quantidade.setText("")
        self.Edit_Quantidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"OS", None))
        self.Btn_Estoque.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
    # retranslateUi

