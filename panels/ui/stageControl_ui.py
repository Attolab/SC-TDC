# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stageControl.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSplitter,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_stageControl(object):
    def setupUi(self, stageControl):
        if not stageControl.objectName():
            stageControl.setObjectName(u"stageControl")
        stageControl.resize(1030, 531)
        self.horizontalLayout_4 = QHBoxLayout(stageControl)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.splitter = QSplitter(stageControl)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(10)
        self.horizontalLayoutWidget = QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_delayScheme_3 = QLabel(self.horizontalLayoutWidget)
        self.label_delayScheme_3.setObjectName(u"label_delayScheme_3")

        self.verticalLayout_4.addWidget(self.label_delayScheme_3)

        self.cBox_stageSelection = QComboBox(self.horizontalLayoutWidget)
        self.cBox_stageSelection.addItem("")
        self.cBox_stageSelection.addItem("")
        self.cBox_stageSelection.setObjectName(u"cBox_stageSelection")

        self.verticalLayout_4.addWidget(self.cBox_stageSelection)

        self.pushButton_stageSettings = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_stageSettings.setObjectName(u"pushButton_stageSettings")

        self.verticalLayout_4.addWidget(self.pushButton_stageSettings)

        self.label_delayScheme = QLabel(self.horizontalLayoutWidget)
        self.label_delayScheme.setObjectName(u"label_delayScheme")

        self.verticalLayout_4.addWidget(self.label_delayScheme)

        self.cBox_stageMode = QComboBox(self.horizontalLayoutWidget)
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.setObjectName(u"cBox_stageMode")

        self.verticalLayout_4.addWidget(self.cBox_stageMode)

        self.absoluteMotion_radioButton = QRadioButton(self.horizontalLayoutWidget)
        self.absoluteMotion_radioButton.setObjectName(u"absoluteMotion_radioButton")
        self.absoluteMotion_radioButton.setChecked(True)

        self.verticalLayout_4.addWidget(self.absoluteMotion_radioButton)

        self.relativeMotion_radioButton = QRadioButton(self.horizontalLayoutWidget)
        self.relativeMotion_radioButton.setObjectName(u"relativeMotion_radioButton")

        self.verticalLayout_4.addWidget(self.relativeMotion_radioButton)

        self.label_t0 = QLabel(self.horizontalLayoutWidget)
        self.label_t0.setObjectName(u"label_t0")

        self.verticalLayout_4.addWidget(self.label_t0)

        self.offset_spinBox = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.offset_spinBox.setObjectName(u"offset_spinBox")
        self.offset_spinBox.setDecimals(7)

        self.verticalLayout_4.addWidget(self.offset_spinBox)

        self.verticalSpacer = QSpacerItem(120, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(292, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.update_pushButton = QPushButton(self.horizontalLayoutWidget)
        self.update_pushButton.setObjectName(u"update_pushButton")

        self.horizontalLayout_2.addWidget(self.update_pushButton)

        self.label_stageMode = QLabel(self.horizontalLayoutWidget)
        self.label_stageMode.setObjectName(u"label_stageMode")

        self.horizontalLayout_2.addWidget(self.label_stageMode)

        self.delayScheme_comboBox = QComboBox(self.horizontalLayoutWidget)
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.setObjectName(u"delayScheme_comboBox")

        self.horizontalLayout_2.addWidget(self.delayScheme_comboBox)

        self.horizontalSpacer_3 = QSpacerItem(292, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.textEdit_delayInput = QPlainTextEdit(self.horizontalLayoutWidget)
        self.textEdit_delayInput.setObjectName(u"textEdit_delayInput")

        self.verticalLayout_5.addWidget(self.textEdit_delayInput)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.move_pushButton = QPushButton(self.horizontalLayoutWidget)
        self.move_pushButton.setObjectName(u"move_pushButton")

        self.horizontalLayout.addWidget(self.move_pushButton)

        self.stop_pushButton = QPushButton(self.horizontalLayoutWidget)
        self.stop_pushButton.setObjectName(u"stop_pushButton")

        self.horizontalLayout.addWidget(self.stop_pushButton)

        self.stage_position_status = QLineEdit(self.horizontalLayoutWidget)
        self.stage_position_status.setObjectName(u"stage_position_status")
        self.stage_position_status.setEnabled(False)
        self.stage_position_status.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.stage_position_status)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.splitter.addWidget(self.horizontalLayoutWidget)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_delayPlot = QLabel(self.verticalLayoutWidget)
        self.label_delayPlot.setObjectName(u"label_delayPlot")

        self.verticalLayout_3.addWidget(self.label_delayPlot)

        self.plot_delays = PlotWidget(self.verticalLayoutWidget)
        self.plot_delays.setObjectName(u"plot_delays")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_delays.sizePolicy().hasHeightForWidth())
        self.plot_delays.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.plot_delays)

        self.splitter.addWidget(self.verticalLayoutWidget)

        self.horizontalLayout_4.addWidget(self.splitter)


        self.retranslateUi(stageControl)

        QMetaObject.connectSlotsByName(stageControl)
    # setupUi

    def retranslateUi(self, stageControl):
        stageControl.setWindowTitle(QCoreApplication.translate("stageControl", u"Form", None))
        self.label_delayScheme_3.setText(QCoreApplication.translate("stageControl", u"Stage Selection", None))
        self.cBox_stageSelection.setItemText(0, QCoreApplication.translate("stageControl", u"Newport - Time Delay", None))
        self.cBox_stageSelection.setItemText(1, QCoreApplication.translate("stageControl", u"ThorLabs - Rotation", None))

        self.pushButton_stageSettings.setText(QCoreApplication.translate("stageControl", u"Stage Settings", None))
        self.label_delayScheme.setText(QCoreApplication.translate("stageControl", u"Delay Scheme", None))
        self.cBox_stageMode.setItemText(0, QCoreApplication.translate("stageControl", u"Position [mm]", None))
        self.cBox_stageMode.setItemText(1, QCoreApplication.translate("stageControl", u"Time - Single Pass [ps]", None))
        self.cBox_stageMode.setItemText(2, QCoreApplication.translate("stageControl", u"Time - Double Pass [ps]", None))
        self.cBox_stageMode.setItemText(3, QCoreApplication.translate("stageControl", u"Time - Single Pass [fs]", None))
        self.cBox_stageMode.setItemText(4, QCoreApplication.translate("stageControl", u"Time - Double Pass [fs]", None))
        self.cBox_stageMode.setItemText(5, QCoreApplication.translate("stageControl", u"Index [no units]", None))

        self.absoluteMotion_radioButton.setText(QCoreApplication.translate("stageControl", u"Absolute", None))
        self.relativeMotion_radioButton.setText(QCoreApplication.translate("stageControl", u"Relative", None))
        self.label_t0.setText(QCoreApplication.translate("stageControl", u"Offset", None))
        self.update_pushButton.setText(QCoreApplication.translate("stageControl", u"Update", None))
        self.label_stageMode.setText(QCoreApplication.translate("stageControl", u"Stage Mode", None))
        self.delayScheme_comboBox.setItemText(0, QCoreApplication.translate("stageControl", u"No Sorting", None))
        self.delayScheme_comboBox.setItemText(1, QCoreApplication.translate("stageControl", u"Sort Acending", None))
        self.delayScheme_comboBox.setItemText(2, QCoreApplication.translate("stageControl", u"Sort Decending", None))
        self.delayScheme_comboBox.setItemText(3, QCoreApplication.translate("stageControl", u"Staggered Acending", None))
        self.delayScheme_comboBox.setItemText(4, QCoreApplication.translate("stageControl", u"Staggered Decending", None))

        self.move_pushButton.setText(QCoreApplication.translate("stageControl", u"Move", None))
        self.stop_pushButton.setText(QCoreApplication.translate("stageControl", u"Stop", None))
        self.stage_position_status.setText(QCoreApplication.translate("stageControl", u"STAGE IS FIXED", None))
        self.label_delayPlot.setText(QCoreApplication.translate("stageControl", u"Delays Plot", None))
    # retranslateUi

