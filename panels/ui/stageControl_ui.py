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
    QLabel, QLayout, QLineEdit, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSplitter, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_stageControl(object):
    def setupUi(self, stageControl):
        if not stageControl.objectName():
            stageControl.setObjectName(u"stageControl")
        stageControl.resize(675, 659)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(stageControl.sizePolicy().hasHeightForWidth())
        stageControl.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(stageControl)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(stageControl)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.horizontalLayoutWidget = QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_delayScheme_3 = QLabel(self.horizontalLayoutWidget)
        self.label_delayScheme_3.setObjectName(u"label_delayScheme_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_delayScheme_3.sizePolicy().hasHeightForWidth())
        self.label_delayScheme_3.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.label_delayScheme_3)

        self.cBox_stageSelection = QComboBox(self.horizontalLayoutWidget)
        self.cBox_stageSelection.addItem("")
        self.cBox_stageSelection.addItem("")
        self.cBox_stageSelection.setObjectName(u"cBox_stageSelection")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cBox_stageSelection.sizePolicy().hasHeightForWidth())
        self.cBox_stageSelection.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.cBox_stageSelection)

        self.pushButton_stageSettings = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_stageSettings.setObjectName(u"pushButton_stageSettings")
        sizePolicy2.setHeightForWidth(self.pushButton_stageSettings.sizePolicy().hasHeightForWidth())
        self.pushButton_stageSettings.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.pushButton_stageSettings)

        self.verticalSpacer = QSpacerItem(120, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stage_position_status = QLineEdit(self.horizontalLayoutWidget)
        self.stage_position_status.setObjectName(u"stage_position_status")
        self.stage_position_status.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stage_position_status.sizePolicy().hasHeightForWidth())
        self.stage_position_status.setSizePolicy(sizePolicy3)
        self.stage_position_status.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.stage_position_status)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_t0_2 = QLabel(self.horizontalLayoutWidget)
        self.label_t0_2.setObjectName(u"label_t0_2")
        sizePolicy1.setHeightForWidth(self.label_t0_2.sizePolicy().hasHeightForWidth())
        self.label_t0_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label_t0_2)

        self.offset_spinBox_2 = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.offset_spinBox_2.setObjectName(u"offset_spinBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.offset_spinBox_2.sizePolicy().hasHeightForWidth())
        self.offset_spinBox_2.setSizePolicy(sizePolicy4)
        self.offset_spinBox_2.setWrapping(False)
        self.offset_spinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.offset_spinBox_2.setDecimals(7)

        self.horizontalLayout_5.addWidget(self.offset_spinBox_2)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.label)

        self.stage_position_status_2 = QLineEdit(self.horizontalLayoutWidget)
        self.stage_position_status_2.setObjectName(u"stage_position_status_2")
        self.stage_position_status_2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.stage_position_status_2.sizePolicy().hasHeightForWidth())
        self.stage_position_status_2.setSizePolicy(sizePolicy3)
        self.stage_position_status_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.stage_position_status_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.splitter.addWidget(self.horizontalLayoutWidget)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_stageMode = QLabel(self.widget)
        self.label_stageMode.setObjectName(u"label_stageMode")

        self.horizontalLayout.addWidget(self.label_stageMode)

        self.delayScheme_comboBox = QComboBox(self.widget)
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.addItem("")
        self.delayScheme_comboBox.setObjectName(u"delayScheme_comboBox")

        self.horizontalLayout.addWidget(self.delayScheme_comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.update_pushButton = QPushButton(self.widget)
        self.update_pushButton.setObjectName(u"update_pushButton")

        self.horizontalLayout.addWidget(self.update_pushButton)

        self.move_pushButton = QPushButton(self.widget)
        self.move_pushButton.setObjectName(u"move_pushButton")

        self.horizontalLayout.addWidget(self.move_pushButton)

        self.stop_pushButton = QPushButton(self.widget)
        self.stop_pushButton.setObjectName(u"stop_pushButton")

        self.horizontalLayout.addWidget(self.stop_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.textEdit_delayInput = QPlainTextEdit(self.widget)
        self.textEdit_delayInput.setObjectName(u"textEdit_delayInput")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.textEdit_delayInput.sizePolicy().hasHeightForWidth())
        self.textEdit_delayInput.setSizePolicy(sizePolicy6)

        self.verticalLayout_3.addWidget(self.textEdit_delayInput)

        self.label_delayScheme_4 = QLabel(self.widget)
        self.label_delayScheme_4.setObjectName(u"label_delayScheme_4")
        self.label_delayScheme_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_delayScheme_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_delayScheme = QLabel(self.widget)
        self.label_delayScheme.setObjectName(u"label_delayScheme")

        self.horizontalLayout_6.addWidget(self.label_delayScheme)

        self.cBox_stageMode = QComboBox(self.widget)
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.setObjectName(u"cBox_stageMode")

        self.horizontalLayout_6.addWidget(self.cBox_stageMode)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.absoluteMotion_radioButton = QRadioButton(self.widget)
        self.absoluteMotion_radioButton.setObjectName(u"absoluteMotion_radioButton")
        self.absoluteMotion_radioButton.setChecked(True)

        self.horizontalLayout_4.addWidget(self.absoluteMotion_radioButton)

        self.relativeMotion_radioButton = QRadioButton(self.widget)
        self.relativeMotion_radioButton.setObjectName(u"relativeMotion_radioButton")

        self.horizontalLayout_4.addWidget(self.relativeMotion_radioButton)

        self.label_t0 = QLabel(self.widget)
        self.label_t0.setObjectName(u"label_t0")
        sizePolicy1.setHeightForWidth(self.label_t0.sizePolicy().hasHeightForWidth())
        self.label_t0.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_t0)

        self.offset_spinBox = QDoubleSpinBox(self.widget)
        self.offset_spinBox.setObjectName(u"offset_spinBox")
        sizePolicy2.setHeightForWidth(self.offset_spinBox.sizePolicy().hasHeightForWidth())
        self.offset_spinBox.setSizePolicy(sizePolicy2)
        self.offset_spinBox.setWrapping(False)
        self.offset_spinBox.setDecimals(7)

        self.horizontalLayout_4.addWidget(self.offset_spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_delayPlot = QLabel(self.widget1)
        self.label_delayPlot.setObjectName(u"label_delayPlot")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_delayPlot.sizePolicy().hasHeightForWidth())
        self.label_delayPlot.setSizePolicy(sizePolicy7)

        self.verticalLayout_2.addWidget(self.label_delayPlot)

        self.plot_delays = PlotWidget(self.widget1)
        self.plot_delays.setObjectName(u"plot_delays")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.plot_delays.sizePolicy().hasHeightForWidth())
        self.plot_delays.setSizePolicy(sizePolicy8)

        self.verticalLayout_2.addWidget(self.plot_delays)

        self.splitter.addWidget(self.widget1)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(stageControl)

        QMetaObject.connectSlotsByName(stageControl)
    # setupUi

    def retranslateUi(self, stageControl):
        stageControl.setWindowTitle(QCoreApplication.translate("stageControl", u"Form", None))
        self.label_delayScheme_3.setText(QCoreApplication.translate("stageControl", u"Stage Selection", None))
        self.cBox_stageSelection.setItemText(0, QCoreApplication.translate("stageControl", u"Newport - Time Delay", None))
        self.cBox_stageSelection.setItemText(1, QCoreApplication.translate("stageControl", u"ThorLabs - Rotation", None))

        self.pushButton_stageSettings.setText(QCoreApplication.translate("stageControl", u"Stage Settings", None))
        self.stage_position_status.setText(QCoreApplication.translate("stageControl", u"STAGE IS FIXED", None))
        self.label_t0_2.setText(QCoreApplication.translate("stageControl", u"Target", None))
        self.offset_spinBox_2.setSuffix("")
        self.label.setText(QCoreApplication.translate("stageControl", u"Current", None))
        self.stage_position_status_2.setText("")
        self.label_stageMode.setText(QCoreApplication.translate("stageControl", u"Stage Mode", None))
        self.delayScheme_comboBox.setItemText(0, QCoreApplication.translate("stageControl", u"No Sorting", None))
        self.delayScheme_comboBox.setItemText(1, QCoreApplication.translate("stageControl", u"Sort Acending", None))
        self.delayScheme_comboBox.setItemText(2, QCoreApplication.translate("stageControl", u"Sort Decending", None))
        self.delayScheme_comboBox.setItemText(3, QCoreApplication.translate("stageControl", u"Staggered Acending", None))
        self.delayScheme_comboBox.setItemText(4, QCoreApplication.translate("stageControl", u"Staggered Decending", None))

        self.update_pushButton.setText(QCoreApplication.translate("stageControl", u"Update", None))
        self.move_pushButton.setText(QCoreApplication.translate("stageControl", u"Move", None))
        self.stop_pushButton.setText(QCoreApplication.translate("stageControl", u"Stop", None))
        self.label_delayScheme_4.setText(QCoreApplication.translate("stageControl", u"Scan panel", None))
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
        self.offset_spinBox.setSuffix("")
        self.label_delayPlot.setText(QCoreApplication.translate("stageControl", u"Delays Plot", None))
    # retranslateUi

