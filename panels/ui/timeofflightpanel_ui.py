# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timeofflightpanel.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(772, 508)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tof_view = PlotWidget(self.groupBox_3)
        self.tof_view.setObjectName(u"tof_view")
        sizePolicy.setHeightForWidth(self.tof_view.sizePolicy().hasHeightForWidth())
        self.tof_view.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.tof_view)

        self.yield_view = PlotWidget(self.groupBox_3)
        self.yield_view.setObjectName(u"yield_view")
        sizePolicy.setHeightForWidth(self.yield_view.sizePolicy().hasHeightForWidth())
        self.yield_view.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.yield_view)

        self.settings_checkBox = QCheckBox(self.groupBox_3)
        self.settings_checkBox.setObjectName(u"settings_checkBox")

        self.verticalLayout.addWidget(self.settings_checkBox)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settings_groupBox = QGroupBox(self.groupBox_3)
        self.settings_groupBox.setObjectName(u"settings_groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.settings_groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.settings_groupBox)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label)

        self.event_start = QLineEdit(self.settings_groupBox)
        self.event_start.setObjectName(u"event_start")
        self.event_start.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.event_start)

        self.label_2 = QLabel(self.settings_groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.event_end = QLineEdit(self.settings_groupBox)
        self.event_end.setObjectName(u"event_end")

        self.horizontalLayout_2.addWidget(self.event_end)

        self.label_4 = QLabel(self.settings_groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.settings_groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.bin_size = QLineEdit(self.settings_groupBox)
        self.bin_size.setObjectName(u"bin_size")

        self.horizontalLayout_3.addWidget(self.bin_size)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.settings_groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.max_queue = QLineEdit(self.settings_groupBox)
        self.max_queue.setObjectName(u"max_queue")

        self.horizontalLayout_4.addWidget(self.max_queue)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.settings_groupBox)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.update_config = QPushButton(self.groupBox_3)
        self.update_config.setObjectName(u"update_config")

        self.verticalLayout.addWidget(self.update_config)


        self.verticalLayout_5.addWidget(self.groupBox_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Time of Flight", None))
        self.settings_checkBox.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.settings_groupBox.setTitle(QCoreApplication.translate("Form", u"Time of Flight Config", None))
        self.label.setText(QCoreApplication.translate("Form", u"Event Window:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"us", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Number of bins", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Max queue", None))
        self.max_queue.setText("")
        self.update_config.setText(QCoreApplication.translate("Form", u"Update", None))
    # retranslateUi

