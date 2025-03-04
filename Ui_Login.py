# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import os
import sys


def resource_path(relative_path):
    """Obtem o caminho absoluto para o recurso."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
 
class Ui_Login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(561, 561)
        MainWindow.setMinimumSize(QSize(561, 561))
        MainWindow.setMaximumSize(QSize(561, 561))
        MainWindow.setStyleSheet(u"background-color:rgb(0, 74, 112)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo_empresa = QLabel(self.centralwidget)
        self.logo_empresa.setObjectName(u"logo_empresa")
        self.logo_empresa.setGeometry(QRect(230, 20, 151, 121))
        self.logo_empresa.setStyleSheet(u"border-radius: 15px")
        self.logo_empresa.setPixmap(QPixmap("./imgs/logo.png"))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 150, 501, 361))
        self.frame.setStyleSheet(u"background-color:rgba(0, 0, 0,0.2)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Edit_User = QLineEdit(self.frame)
        self.Edit_User.setObjectName(u"Edit_User")
        self.Edit_User.setGeometry(QRect(100, 140, 300, 50))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Edit_User.setFont(font)
        self.Edit_User.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Edit_User.setAlignment(Qt.AlignCenter)
        self.Edit_Pass = QLineEdit(self.frame)
        self.Edit_Pass.setObjectName(u"Edit_Pass")
        self.Edit_Pass.setGeometry(QRect(100, 210, 300, 50))
        self.Edit_Pass.setFont(font)
        self.Edit_Pass.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Edit_Pass.setEchoMode(QLineEdit.Password)
        self.Edit_Pass.setAlignment(Qt.AlignCenter)
        self.Btn_Logar = QPushButton(self.frame)
        self.Btn_Logar.setObjectName(u"Btn_Logar")
        self.Btn_Logar.setGeometry(QRect(190, 300, 121, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.Btn_Logar.setFont(font1)
        self.Btn_Logar.setStyleSheet(u"background-color:rgb(248, 121, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.Btn_Logar.setAutoRepeatInterval(100)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 40, 300, 50))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.ProspectosLogo = QLabel(self.centralwidget)
        self.ProspectosLogo.setPixmap(QPixmap(resource_path("Paginas/img/Prospectos_Logos.png")))
        self.ProspectosLogo.setGeometry(QRect(410, 520, 121, 31))
        self.ProspectosLogo.setStyleSheet(u"border-radius: 15px")
        self.ProspectosLogo.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_empresa.setText("")
        self.Edit_User.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.Edit_Pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.Btn_Logar.setText(QCoreApplication.translate("MainWindow", u"LOGAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">CONTROLE DE FLUXO</span></p></body></html>", None))
        self.ProspectosLogo.setText("")
    # retranslateUi

