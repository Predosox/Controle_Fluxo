# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PCP_Estoque.ui'
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
class Ui_PCP_Estoque(object):
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
        self.VerificarEstoqueLabel = QLabel(self.centralwidget)
        self.VerificarEstoqueLabel.setObjectName(u"VerificarEstoqueLabel")
        self.VerificarEstoqueLabel.setGeometry(QRect(200, 50, 401, 61))
        font1 = QFont()
        font1.setPointSize(50)
        font1.setBold(True)
        self.VerificarEstoqueLabel.setFont(font1)
        self.Tabela_pcp = QTreeWidget(self.centralwidget)
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(10)
        font2.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem.setFont(3, font2);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setFont(2, font2);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, font);
        self.Tabela_pcp.setHeaderItem(__qtreewidgetitem)
        self.Tabela_pcp.setObjectName(u"Tabela_pcp")
        self.Tabela_pcp.setGeometry(QRect(120, 200, 561, 251))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.Tabela_pcp.setFont(font3)
        self.Tabela_pcp.setStyleSheet(u"background-color:rgb(255, 166, 64)")
        self.Btn_Estoque = QPushButton(self.centralwidget)
        self.Btn_Estoque.setObjectName(u"Btn_Estoque")
        self.Btn_Estoque.setGeometry(QRect(230, 460, 101, 31))
        self.Btn_Estoque.setFont(font)
        self.Btn_Estoque.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Fallta = QPushButton(self.centralwidget)
        self.Btn_Fallta.setObjectName(u"Btn_Fallta")
        self.Btn_Fallta.setGeometry(QRect(340, 460, 101, 31))
        self.Btn_Fallta.setFont(font)
        self.Btn_Fallta.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Edit_Quantidade = QLineEdit(self.centralwidget)
        self.Edit_Quantidade.setObjectName(u"Edit_Quantidade")
        self.Edit_Quantidade.setGeometry(QRect(120, 460, 101, 31))
        self.Edit_Quantidade.setStyleSheet(u"\n"
"color: white;\n"
"")
        self.Edit_Quantidade.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_empresa.setText("")
        self.Btn_Voltar_os.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.VerificarEstoqueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">VERIFICAR ESTOQUE</span></p></body></html>", None))
        ___qtreewidgetitem = self.Tabela_pcp.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"UNIDADE", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"C\u00d3DIGO", None));
        self.Btn_Estoque.setText(QCoreApplication.translate("MainWindow", u"EM ESTOQUE", None))
        self.Btn_Fallta.setText(QCoreApplication.translate("MainWindow", u"FALTANDO", None))
        self.Edit_Quantidade.setText("")
        self.Edit_Quantidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None))
    # retranslateUi

