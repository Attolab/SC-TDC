# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewerconfig.ui'
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
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(330, 207)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.display_rate = QSlider(self.groupBox)
        self.display_rate.setObjectName(u"display_rate")
        self.display_rate.setMinimum(1)
        self.display_rate.setMaximum(50)
        self.display_rate.setValue(5)
        self.display_rate.setOrientation(Qt.Horizontal)
        self.display_rate.setInvertedAppearance(False)
        self.display_rate.setTickPosition(QSlider.TicksBothSides)
        self.display_rate.setTickInterval(5)

        self.horizontalLayout_2.addWidget(self.display_rate)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_3.addWidget(self.label_16)

        self.frame_time = QLineEdit(self.groupBox)
        self.frame_time.setObjectName(u"frame_time")

        self.horizontalLayout_3.addWidget(self.frame_time)

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

        self.reset_plots = QPushButton(self.groupBox)
        self.reset_plots.setObjectName(u"reset_plots")

        self.verticalLayout.addWidget(self.reset_plots)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Viewer Config", None))
        self.label.setText(QCoreApplication.translate("Form", u"Display Update (Hz)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"50", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Refresh time", None))
        self.frame_time.setInputMask("")
        self.frame_time.setText(QCoreApplication.translate("Form", u"-1", None))
        self.time_multi.setItemText(0, QCoreApplication.translate("Form", u"s", None))
        self.time_multi.setItemText(1, QCoreApplication.translate("Form", u"ms", None))

        self.reset_plots.setText(QCoreApplication.translate("Form", u"Reset Plots", None))
    # retranslateUi

