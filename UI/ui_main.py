# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(865, 490)
        MainWindow.setStyleSheet(u"background: #252422;\n"
"color: #FFFCF2;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.image = QLabel(self.centralwidget)
        self.image.setObjectName(u"image")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setStyleSheet(u"background: #403D39")
        self.image.setScaledContents(True)
        self.image.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.image, 0, 1, 1, 2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(150, 0))
        self.groupBox.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tools = QListWidget(self.groupBox)
        QListWidgetItem(self.tools)
        QListWidgetItem(self.tools)
        QListWidgetItem(self.tools)
        QListWidgetItem(self.tools)
        QListWidgetItem(self.tools)
        self.tools.setObjectName(u"tools")
        self.tools.setStyleSheet(u"border: 0;")

        self.verticalLayout_3.addWidget(self.tools)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(150, 150))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"	border-bottom: 0;\n"
"	border-right: 0;\n"
"	border-left: 0;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.select_brush_color = QPushButton(self.groupBox_2)
        self.select_brush_color.setObjectName(u"select_brush_color")
        self.select_brush_color.setStyleSheet(u"background: rgb(0,0,0);")

        self.verticalLayout.addWidget(self.select_brush_color)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.thickness_spinbox = QSpinBox(self.groupBox_2)
        self.thickness_spinbox.setObjectName(u"thickness_spinbox")
        self.thickness_spinbox.setMinimum(1)
        self.thickness_spinbox.setMaximum(1000)
        self.thickness_spinbox.setValue(1)

        self.horizontalLayout_2.addWidget(self.thickness_spinbox)

        self.thickness_slider = QSlider(self.groupBox_2)
        self.thickness_slider.setObjectName(u"thickness_slider")
        self.thickness_slider.setMinimum(1)
        self.thickness_slider.setMaximum(20)
        self.thickness_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.thickness_slider)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.fill = QCheckBox(self.groupBox_2)
        self.fill.setObjectName(u"fill")

        self.verticalLayout.addWidget(self.fill)

        self.stackedWidget = QStackedWidget(self.groupBox_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 6, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.show_red_dots = QCheckBox(self.centralwidget)
        self.show_red_dots.setObjectName(u"show_red_dots")

        self.horizontalLayout.addWidget(self.show_red_dots)

        self.show_infos = QCheckBox(self.centralwidget)
        self.show_infos.setObjectName(u"show_infos")

        self.horizontalLayout.addWidget(self.show_infos)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image.setText(QCoreApplication.translate("MainWindow", u"Could not load image data", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))

        __sortingEnabled = self.tools.isSortingEnabled()
        self.tools.setSortingEnabled(False)
        ___qlistwidgetitem = self.tools.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Brush", None));
        ___qlistwidgetitem1 = self.tools.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Eraser", None));
        ___qlistwidgetitem2 = self.tools.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Rect", None));
        ___qlistwidgetitem3 = self.tools.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Circle", None));
        ___qlistwidgetitem4 = self.tools.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tools.setSortingEnabled(__sortingEnabled)

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.select_brush_color.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Thickness", None))
        self.fill.setText(QCoreApplication.translate("MainWindow", u"Filled", None))
        self.show_red_dots.setText(QCoreApplication.translate("MainWindow", u"Show Red Dots", None))
        self.show_infos.setText(QCoreApplication.translate("MainWindow", u"Show Geometric Infos", None))
    # retranslateUi

