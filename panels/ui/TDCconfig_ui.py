# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TDCconfig.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
        Form.resize(356, 247)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.label_18)

        self.filename_lineEdit = QLineEdit(self.groupBox)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")

        self.horizontalLayout_17.addWidget(self.filename_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.folderPath_lineEdit = QLineEdit(self.groupBox)
        self.folderPath_lineEdit.setObjectName(u"folderPath_lineEdit")

        self.horizontalLayout_4.addWidget(self.folderPath_lineEdit)

        self.openPath_pushButton = QPushButton(self.groupBox)
        self.openPath_pushButton.setObjectName(u"openPath_pushButton")

        self.horizontalLayout_4.addWidget(self.openPath_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.initialize_pushButton = QPushButton(self.groupBox)
        self.initialize_pushButton.setObjectName(u"initialize_pushButton")

        self.horizontalLayout.addWidget(self.initialize_pushButton)

        self.deinitialize_pushButton = QPushButton(self.groupBox)
        self.deinitialize_pushButton.setObjectName(u"deinitialize_pushButton")
        self.deinitialize_pushButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.deinitialize_pushButton)

        self.connectionStatus_label = QLabel(self.groupBox)
        self.connectionStatus_label.setObjectName(u"connectionStatus_label")
        self.connectionStatus_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.connectionStatus_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_3.addWidget(self.label_16)

        self.exposureTime_lineEdit = QLineEdit(self.groupBox)
        self.exposureTime_lineEdit.setObjectName(u"exposureTime_lineEdit")

        self.horizontalLayout_3.addWidget(self.exposureTime_lineEdit)

        self.time_multi = QComboBox(self.groupBox)
        self.time_multi.addItem("")
        self.time_multi.addItem("")
        self.time_multi.setObjectName(u"time_multi")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.time_multi.sizePolicy().hasHeightForWidth())
        self.time_multi.setSizePolicy(sizePolicy1)
        self.time_multi.setMaximumSize(QSize(70, 16777215))
        self.time_multi.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.time_multi)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.startThread_pushButton = QPushButton(self.groupBox)
        self.startThread_pushButton.setObjectName(u"startThread_pushButton")

        self.horizontalLayout_5.addWidget(self.startThread_pushButton)

        self.stopThread_pushButton = QPushButton(self.groupBox)
        self.stopThread_pushButton.setObjectName(u"stopThread_pushButton")

        self.horizontalLayout_5.addWidget(self.stopThread_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        self.time_multi.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"TDC Config", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Filename", None))
        self.filename_lineEdit.setInputMask("")
        self.filename_lineEdit.setText(QCoreApplication.translate("Form", u"tdc_gpx3.ini", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Path", None))
        self.folderPath_lineEdit.setText(QCoreApplication.translate("Form", u"C:\\\\Users\\\\attose1_VMI\\\\Documents\\\\Python_Scripts\\\\scTDC\\\\scTDC_Python_SDK_v1.3.0\\\\scTDC_Py\\\\Library\\\\", None))
        self.openPath_pushButton.setText(QCoreApplication.translate("Form", u"Open", None))
        self.initialize_pushButton.setText(QCoreApplication.translate("Form", u"Initialize", None))
        self.deinitialize_pushButton.setText(QCoreApplication.translate("Form", u"Deinitialize", None))
        self.connectionStatus_label.setText(QCoreApplication.translate("Form", u"OFF", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Exposure time", None))
        self.exposureTime_lineEdit.setInputMask("")
        self.exposureTime_lineEdit.setText(QCoreApplication.translate("Form", u"100", None))
        self.time_multi.setItemText(0, QCoreApplication.translate("Form", u"s", None))
        self.time_multi.setItemText(1, QCoreApplication.translate("Form", u"ms", None))

        self.startThread_pushButton.setText(QCoreApplication.translate("Form", u"Start", None))
        self.stopThread_pushButton.setText(QCoreApplication.translate("Form", u"Stop", None))
    # retranslateUi

