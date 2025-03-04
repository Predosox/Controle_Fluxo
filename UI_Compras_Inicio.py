# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Compras_Inicio.ui'
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

class UI_Compras_Inicio(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 74, 112);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 161, 121))
        self.label.setPixmap(QPixmap("./imgs/logo.png"))
        self.Btn_Voltar = QPushButton(self.centralwidget)
        self.Btn_Voltar.setObjectName(u"Btn_Voltar")
        self.Btn_Voltar.setGeometry(QRect(680, 550, 101, 31))
        font = QFont()
        font.setBold(True)
        self.Btn_Voltar.setFont(font)
        self.Btn_Voltar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Pedidos = QPushButton(self.centralwidget)
        self.Btn_Pedidos.setObjectName(u"Btn_Pedidos")
        self.Btn_Pedidos.setGeometry(QRect(280, 270, 241, 61))
        self.Btn_Pedidos.setFont(font)
        self.Btn_Pedidos.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Add = QPushButton(self.centralwidget)
        self.Btn_Add.setObjectName(u"Btn_Add")
        self.Btn_Add.setGeometry(QRect(280, 180, 241, 61))
        self.Btn_Add.setFont(font)
        self.Btn_Add.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Verify = QPushButton(self.centralwidget)
        self.Btn_Verify.setObjectName(u"Btn_Verify")
        self.Btn_Verify.setGeometry(QRect(280, 360, 241, 61))
        self.Btn_Verify.setFont(font)
        self.Btn_Verify.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Checar = QPushButton(self.centralwidget)
        self.Btn_Checar.setObjectName(u"Btn_Checar")
        self.Btn_Checar.setGeometry(QRect(680, 510, 101, 31))
        self.Btn_Checar.setFont(font)
        self.Btn_Checar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.Btn_Voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.Btn_Pedidos.setText(QCoreApplication.translate("MainWindow", u"PEDIDOS", None))
        self.Btn_Add.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR FORNECEDOR", None))
        self.Btn_Verify.setText(QCoreApplication.translate("MainWindow", u"VERIFICAR FORNECEDOR", None))
        self.Btn_Checar.setText(QCoreApplication.translate("MainWindow", u"Checar", None))
    # retranslateUi

