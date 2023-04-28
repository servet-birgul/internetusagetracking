# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacehEoLAv.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,QSettings,QTimer,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import QSS_Resources_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(228, 183)
        MainWindow.setStyleSheet(u"*{\n"
"   border: none;\n"
"   background-color: transparent;\n"
"   background: transparent;\n"
"   padding: 0;\n"
"   margin: 0;\n"
"   font: 63 12pt \"Bahnschrift SemiBold Condensed\";\n"
"   color: rgb(85, 255, 127);font-size: 12pt;\n"
"   color: rgb(255, 170, 0);\n"
"   color: rgb(255, 85, 0);\n"
"}\n"
"#widget{background-color: rgb(255, 255, 255,10)}\n"
"QPushButton:hover{background-color: rgb(0, 100, 255,70);}\n"
"QPushButton{\n"
"   color: rgb(0, 170, 255);\n"
"  padding: 1px 1px;\n"
"    border-radius:7px;\n"
"   background-color: rgb(170,100, 255,50);}\n"
"#widget_2{background-color: rgb(255, 255, 255,20);border: 1px solid rgb(0, 0, 250,50)}\n"
"#centralwidget{;border-left: 1px solid rgb(0, 0, 100,150)}\n"
"QSpinBox{  background-color: rgb(0, 0, 0,40);font-size:12;}\n"
"QSpinBox:hover{background-color: rgb(91, 88, 110,120);}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon = QIcon()
        icon.addFile(u":/icon/Icons/window_close_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(33, 29))

        self.horizontalLayout_2.addWidget(self.pushButton_3, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.doubleSpinBox = QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setAccelerated(False)
        self.doubleSpinBox.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setMinimum(0.010000000000000)
        self.doubleSpinBox.setSingleStep(0.150000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icon/Icons/refresh-ccw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(17, 24))

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(0, 255, 255);\n"
"font-size:13pt")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"giden Veri (MB): 0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Gelen Veri (MB): 0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Harcanan  Veri (MB): 0", None))
        self.doubleSpinBox.setPrefix("")
        self.doubleSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u"GB Sonra Uyar", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ba\u015flat", None))
        self.pushButton_2.setText("")
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p% G\u00fcnl\u00fck Uyar\u0131 limiti ", None))
    # retranslateUi