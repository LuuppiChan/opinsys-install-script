# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(439, 386)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_asenna = QWidget()
        self.tab_asenna.setObjectName(u"tab_asenna")
        self.verticalLayout_2 = QVBoxLayout(self.tab_asenna)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Ohjelma = QLabel(self.tab_asenna)
        self.Ohjelma.setObjectName(u"Ohjelma")
        self.Ohjelma.setMinimumSize(QSize(407, 23))
        self.Ohjelma.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.Ohjelma, 0, Qt.AlignHCenter)

        self.comboBox_ohjelmat_asennus = QComboBox(self.tab_asenna)
        self.comboBox_ohjelmat_asennus.addItem("")
        self.comboBox_ohjelmat_asennus.addItem("")
        self.comboBox_ohjelmat_asennus.addItem("")
        self.comboBox_ohjelmat_asennus.addItem("")
        self.comboBox_ohjelmat_asennus.addItem("")
        self.comboBox_ohjelmat_asennus.addItem("")
        self.comboBox_ohjelmat_asennus.setObjectName(u"comboBox_ohjelmat_asennus")
        self.comboBox_ohjelmat_asennus.setMinimumSize(QSize(407, 0))

        self.verticalLayout_2.addWidget(self.comboBox_ohjelmat_asennus)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_poista = QPushButton(self.tab_asenna)
        self.pushButton_poista.setObjectName(u"pushButton_poista")

        self.horizontalLayout.addWidget(self.pushButton_poista)

        self.pushButton_asenna = QPushButton(self.tab_asenna)
        self.pushButton_asenna.setObjectName(u"pushButton_asenna")

        self.horizontalLayout.addWidget(self.pushButton_asenna)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_asenna, "")
        self.tab_kaynnista = QWidget()
        self.tab_kaynnista.setObjectName(u"tab_kaynnista")
        self.verticalLayout_4 = QVBoxLayout(self.tab_kaynnista)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tab_kaynnista)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setKerning(True)
        self.label_2.setFont(font1)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_2)

        self.tabWidget.addTab(self.tab_kaynnista, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 439, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Opinsys Installer Script", None))
        self.Ohjelma.setText(QCoreApplication.translate("MainWindow", u"Valitse asennettava ohjelma", None))
        self.comboBox_ohjelmat_asennus.setItemText(0, QCoreApplication.translate("MainWindow", u"Steam", None))
        self.comboBox_ohjelmat_asennus.setItemText(1, QCoreApplication.translate("MainWindow", u"Minecraft Launcher", None))
        self.comboBox_ohjelmat_asennus.setItemText(2, QCoreApplication.translate("MainWindow", u"Discord", None))
        self.comboBox_ohjelmat_asennus.setItemText(3, QCoreApplication.translate("MainWindow", u"Vesktop", None))
        self.comboBox_ohjelmat_asennus.setItemText(4, QCoreApplication.translate("MainWindow", u"Brave", None))
        self.comboBox_ohjelmat_asennus.setItemText(5, QCoreApplication.translate("MainWindow", u"Paketin hallinta", None))

        self.pushButton_poista.setText(QCoreApplication.translate("MainWindow", u"Poista", None))
        self.pushButton_asenna.setText(QCoreApplication.translate("MainWindow", u"Asenna", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_asenna), QCoreApplication.translate("MainWindow", u"Asenna", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Voit hakea ohjelmia painamalla ensin Windows n\u00e4pp\u00e4int\u00e4 ja sen j\u00e4lkeen kirjoittamalla ohjelman nimen.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_kaynnista), QCoreApplication.translate("MainWindow", u"K\u00e4ynnist\u00e4", None))
    # retranslateUi

