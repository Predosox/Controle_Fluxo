# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Verifyfornecedor.ui'
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
class UI_VerificarFornecedor(object):
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
        __qtreewidgetitem.setTextAlignment(6, Qt.AlignCenter);
        __qtreewidgetitem.setFont(6, font);
        __qtreewidgetitem.setTextAlignment(5, Qt.AlignCenter);
        __qtreewidgetitem.setFont(5, font);
        __qtreewidgetitem.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem.setFont(4, font);
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem.setFont(3, font);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setFont(2, font);
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_empresa.setText("")
        self.Btn_Voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.Edit_Nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do fornecedor", None))
        self.Btn_Consultar.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">CONSULTAR FORNECEDORES</span></p></body></html>", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"I.ESTADUAL", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"NOME", None));
    # retranslateUi

