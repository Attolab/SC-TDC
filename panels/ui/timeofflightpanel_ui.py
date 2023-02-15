# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timeofflightpanel.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(787, 499)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tof_view = PlotWidget(self.groupBox_3)
        self.tof_view.setObjectName(u"tof_view")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tof_view.sizePolicy().hasHeightForWidth())
        self.tof_view.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.tof_view)

        self.yield_view = PlotWidget(self.groupBox_3)
        self.yield_view.setObjectName(u"yield_view")
        sizePolicy.setHeightForWidth(self.yield_view.sizePolicy().hasHeightForWidth())
        self.yield_view.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.yield_view)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label)

        self.event_start = QLineEdit(self.groupBox_2)
        self.event_start.setObjectName(u"event_start")
        self.event_start.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.event_start)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.event_end = QLineEdit(self.groupBox_2)
        self.event_end.setObjectName(u"event_end")

        self.horizontalLayout_2.addWidget(self.event_end)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.bin_size = QLineEdit(self.groupBox_2)
        self.bin_size.setObjectName(u"bin_size")

        self.horizontalLayout_3.addWidget(self.bin_size)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.bin_size_3 = QLineEdit(self.groupBox_2)
        self.bin_size_3.setObjectName(u"bin_size_3")

        self.horizontalLayout_7.addWidget(self.bin_size_3)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.label_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.update_config = QPushButton(Form)
        self.update_config.setObjectName(u"update_config")

        self.verticalLayout_4.addWidget(self.update_config)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Time of Flight", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Time of Flight Config", None))
        self.label.setText(QCoreApplication.translate("Form", u"Event Window:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"us", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Number of bins", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Refresh rate", None))
        self.bin_size_3.setText(QCoreApplication.translate("Form", u"1000", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"ms", None))
        self.update_config.setText(QCoreApplication.translate("Form", u"Update", None))
    # retranslateUi

