# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acquisitionpanel.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(448, 419)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.folderPath_lineEdit = QLineEdit(Form)
        self.folderPath_lineEdit.setObjectName(u"folderPath_lineEdit")

        self.horizontalLayout_4.addWidget(self.folderPath_lineEdit)

        self.openPath_pushButton = QPushButton(Form)
        self.openPath_pushButton.setObjectName(u"openPath_pushButton")

        self.horizontalLayout_4.addWidget(self.openPath_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.filePrefix_lineEdit = QLineEdit(Form)
        self.filePrefix_lineEdit.setObjectName(u"filePrefix_lineEdit")

        self.horizontalLayout_5.addWidget(self.filePrefix_lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.acquisitionTime_lineEdit = QLineEdit(Form)
        self.acquisitionTime_lineEdit.setObjectName(u"acquisitionTime_lineEdit")

        self.horizontalLayout_6.addWidget(self.acquisitionTime_lineEdit)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 114, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_stageMode = QLabel(self.layoutWidget)
        self.label_stageMode.setObjectName(u"label_stageMode")

        self.horizontalLayout_9.addWidget(self.label_stageMode)

        self.delayScheme_comboBox = QComboBox(self.layoutWidget)
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.setObjectName(u"delayScheme_comboBox")

        self.horizontalLayout_9.addWidget(self.delayScheme_comboBox)


        self.horizontalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.update_pushButton = QPushButton(self.layoutWidget)
        self.update_pushButton.setObjectName(u"update_pushButton")

        self.horizontalLayout.addWidget(self.update_pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.textEdit_delayInput = QPlainTextEdit(self.layoutWidget)
        self.textEdit_delayInput.setObjectName(u"textEdit_delayInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit_delayInput.sizePolicy().hasHeightForWidth())
        self.textEdit_delayInput.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.textEdit_delayInput)

        self.splitter.addWidget(self.layoutWidget)
        self.plot_delays = PlotWidget(self.splitter)
        self.plot_delays.setObjectName(u"plot_delays")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(30)
        sizePolicy3.setHeightForWidth(self.plot_delays.sizePolicy().hasHeightForWidth())
        self.plot_delays.setSizePolicy(sizePolicy3)
        self.splitter.addWidget(self.plot_delays)

        self.verticalLayout_2.addWidget(self.splitter)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_7 = QLineEdit(Form)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy4)

        self.verticalLayout_9.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(Form)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy4)

        self.verticalLayout_9.addWidget(self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(Form)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy4)

        self.verticalLayout_9.addWidget(self.lineEdit_9)

        self.lineEdit_10 = QLineEdit(Form)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy4)

        self.verticalLayout_9.addWidget(self.lineEdit_10)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.status_position = QLineEdit(Form)
        self.status_position.setObjectName(u"status_position")
        self.status_position.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.status_position.sizePolicy().hasHeightForWidth())
        self.status_position.setSizePolicy(sizePolicy5)

        self.verticalLayout_10.addWidget(self.status_position)

        self.status_image = QLineEdit(Form)
        self.status_image.setObjectName(u"status_image")
        self.status_image.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.status_image.sizePolicy().hasHeightForWidth())
        self.status_image.setSizePolicy(sizePolicy5)

        self.verticalLayout_10.addWidget(self.status_image)

        self.status_steps = QLineEdit(Form)
        self.status_steps.setObjectName(u"status_steps")
        self.status_steps.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.status_steps.sizePolicy().hasHeightForWidth())
        self.status_steps.setSizePolicy(sizePolicy5)

        self.verticalLayout_10.addWidget(self.status_steps)

        self.status_scanLength = QLineEdit(Form)
        self.status_scanLength.setObjectName(u"status_scanLength")
        self.status_scanLength.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.status_scanLength.sizePolicy().hasHeightForWidth())
        self.status_scanLength.setSizePolicy(sizePolicy5)

        self.verticalLayout_10.addWidget(self.status_scanLength)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label)

        self.elapsed_time_h = QLCDNumber(Form)
        self.elapsed_time_h.setObjectName(u"elapsed_time_h")
        self.elapsed_time_h.setLineWidth(1)
        self.elapsed_time_h.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_7.addWidget(self.elapsed_time_h)

        self.elapsed_time_m = QLCDNumber(Form)
        self.elapsed_time_m.setObjectName(u"elapsed_time_m")
        self.elapsed_time_m.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_7.addWidget(self.elapsed_time_m)

        self.elapsed_time_s = QLCDNumber(Form)
        self.elapsed_time_s.setObjectName(u"elapsed_time_s")
        self.elapsed_time_s.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_7.addWidget(self.elapsed_time_s)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.start_acq_pushButton = QPushButton(Form)
        self.start_acq_pushButton.setObjectName(u"start_acq_pushButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.start_acq_pushButton.sizePolicy().hasHeightForWidth())
        self.start_acq_pushButton.setSizePolicy(sizePolicy6)
        font = QFont()
        font.setPointSize(16)
        self.start_acq_pushButton.setFont(font)

        self.verticalLayout.addWidget(self.start_acq_pushButton)

        self.end_acq_pushButton = QPushButton(Form)
        self.end_acq_pushButton.setObjectName(u"end_acq_pushButton")
        sizePolicy6.setHeightForWidth(self.end_acq_pushButton.sizePolicy().hasHeightForWidth())
        self.end_acq_pushButton.setSizePolicy(sizePolicy6)
        self.end_acq_pushButton.setFont(font)

        self.verticalLayout.addWidget(self.end_acq_pushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_12.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_12)

        self.status_label = QLabel(Form)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.status_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Path", None))
        self.openPath_pushButton.setText(QCoreApplication.translate("Form", u"Open", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Prefix:", None))
        self.filePrefix_lineEdit.setText(QCoreApplication.translate("Form", u"test_", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Acquisition Time:", None))
        self.acquisitionTime_lineEdit.setText(QCoreApplication.translate("Form", u"10", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"ms", None))
        self.label_stageMode.setText(QCoreApplication.translate("Form", u"Stage Mode", None))
        self.delayScheme_comboBox.setItemText(0, QCoreApplication.translate("Form", u"No Sorting", None))
        self.delayScheme_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Sort Acending", None))
        self.delayScheme_comboBox.setItemText(2, QCoreApplication.translate("Form", u"Sort Decending", None))
        self.delayScheme_comboBox.setItemText(3, QCoreApplication.translate("Form", u"Staggered Acending", None))
        self.delayScheme_comboBox.setItemText(4, QCoreApplication.translate("Form", u"Staggered Decending", None))

        self.update_pushButton.setText(QCoreApplication.translate("Form", u"Refresh", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Form", u"Position", None))
        self.lineEdit_8.setText(QCoreApplication.translate("Form", u"Image number", None))
        self.lineEdit_9.setText(QCoreApplication.translate("Form", u"Steps", None))
        self.lineEdit_10.setText(QCoreApplication.translate("Form", u"Scan Time Remaining / Total", None))
        self.label.setText(QCoreApplication.translate("Form", u"Acq Time:", None))
        self.start_acq_pushButton.setText(QCoreApplication.translate("Form", u"Start Acquisition", None))
        self.end_acq_pushButton.setText(QCoreApplication.translate("Form", u"Stop Acquisition", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Status:", None))
        self.status_label.setText(QCoreApplication.translate("Form", u"Live", None))
    # retranslateUi

