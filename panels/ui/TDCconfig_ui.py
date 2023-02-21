# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TDCconfig.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(262, 205)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_3.addWidget(self.label_16)

        self.exposure_time = QLineEdit(self.groupBox)
        self.exposure_time.setObjectName(u"exposure_time")

        self.horizontalLayout_3.addWidget(self.exposure_time)

        self.time_multi = QComboBox(self.groupBox)
        self.time_multi.addItem("")
        self.time_multi.addItem("")
        self.time_multi.setObjectName(u"time_multi")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_multi.sizePolicy().hasHeightForWidth())
        self.time_multi.setSizePolicy(sizePolicy)
        self.time_multi.setMaximumSize(QSize(70, 16777215))
        self.time_multi.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.time_multi)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.deinitialize_pushButton = QPushButton(self.groupBox)
        self.deinitialize_pushButton.setObjectName(u"deinitialize_pushButton")

        self.horizontalLayout.addWidget(self.deinitialize_pushButton)

        self.initialize_pushButton = QPushButton(self.groupBox)
        self.initialize_pushButton.setObjectName(u"initialize_pushButton")

        self.horizontalLayout.addWidget(self.initialize_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(Form)

        self.time_multi.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"TDC Config", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Exposure time", None))
        self.exposure_time.setInputMask("")
        self.exposure_time.setText(QCoreApplication.translate("Form", u"100", None))
        self.time_multi.setItemText(0, QCoreApplication.translate("Form", u"s", None))
        self.time_multi.setItemText(1, QCoreApplication.translate("Form", u"ms", None))

        self.deinitialize_pushButton.setText(QCoreApplication.translate("Form", u"Initialize", None))
        self.initialize_pushButton.setText(QCoreApplication.translate("Form", u"Deinitialize", None))
    # retranslateUi

