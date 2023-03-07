# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stageControl.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_stageControl(object):
    def setupUi(self, stageControl):
        if not stageControl.objectName():
            stageControl.setObjectName(u"stageControl")
        stageControl.resize(597, 225)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(stageControl.sizePolicy().hasHeightForWidth())
        stageControl.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(stageControl)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox = QGroupBox(stageControl)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cBox_stageSelection = QComboBox(self.groupBox)
        self.cBox_stageSelection.addItem("")
        self.cBox_stageSelection.addItem("")
        self.cBox_stageSelection.setObjectName(u"cBox_stageSelection")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cBox_stageSelection.sizePolicy().hasHeightForWidth())
        self.cBox_stageSelection.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.cBox_stageSelection)

        self.pushButton_stageSettings = QPushButton(self.groupBox)
        self.pushButton_stageSettings.setObjectName(u"pushButton_stageSettings")
        sizePolicy1.setHeightForWidth(self.pushButton_stageSettings.sizePolicy().hasHeightForWidth())
        self.pushButton_stageSettings.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton_stageSettings)

        self.activeStab_pushButton = QPushButton(self.groupBox)
        self.activeStab_pushButton.setObjectName(u"activeStab_pushButton")
        sizePolicy1.setHeightForWidth(self.activeStab_pushButton.sizePolicy().hasHeightForWidth())
        self.activeStab_pushButton.setSizePolicy(sizePolicy1)
        self.activeStab_pushButton.setCheckable(True)

        self.verticalLayout.addWidget(self.activeStab_pushButton)

        self.verticalSpacer = QSpacerItem(120, 50, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(stageControl)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stop_pushButton = QPushButton(self.groupBox_2)
        self.stop_pushButton.setObjectName(u"stop_pushButton")
        self.stop_pushButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.stop_pushButton)

        self.offset_spinBox = QDoubleSpinBox(self.groupBox_2)
        self.offset_spinBox.setObjectName(u"offset_spinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.offset_spinBox.sizePolicy().hasHeightForWidth())
        self.offset_spinBox.setSizePolicy(sizePolicy2)
        self.offset_spinBox.setWrapping(False)
        self.offset_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.offset_spinBox.setDecimals(3)
        self.offset_spinBox.setMinimum(-1000000.000000000000000)
        self.offset_spinBox.setMaximum(1000000.000000000000000)
        self.offset_spinBox.setValue(0.000000000000000)

        self.horizontalLayout.addWidget(self.offset_spinBox)

        self.label_t0 = QLabel(self.groupBox_2)
        self.label_t0.setObjectName(u"label_t0")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_t0.sizePolicy().hasHeightForWidth())
        self.label_t0.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.label_t0)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.conversionFactor_lineEdit = QLineEdit(self.groupBox_2)
        self.conversionFactor_lineEdit.setObjectName(u"conversionFactor_lineEdit")
        self.conversionFactor_lineEdit.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.conversionFactor_lineEdit.sizePolicy().hasHeightForWidth())
        self.conversionFactor_lineEdit.setSizePolicy(sizePolicy4)
        self.conversionFactor_lineEdit.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.conversionFactor_lineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.conversionFactor_lineEdit)

        self.cBox_stageMode = QComboBox(self.groupBox_2)
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.addItem("")
        self.cBox_stageMode.setObjectName(u"cBox_stageMode")

        self.horizontalLayout_2.addWidget(self.cBox_stageMode)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_t0_3 = QLabel(self.groupBox_3)
        self.label_t0_3.setObjectName(u"label_t0_3")
        sizePolicy3.setHeightForWidth(self.label_t0_3.sizePolicy().hasHeightForWidth())
        self.label_t0_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.label_t0_3)

        self.targetAbsolute_spinBox = QDoubleSpinBox(self.groupBox_3)
        self.targetAbsolute_spinBox.setObjectName(u"targetAbsolute_spinBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.targetAbsolute_spinBox.sizePolicy().hasHeightForWidth())
        self.targetAbsolute_spinBox.setSizePolicy(sizePolicy5)
        self.targetAbsolute_spinBox.setWrapping(False)
        self.targetAbsolute_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.targetAbsolute_spinBox.setKeyboardTracking(False)
        self.targetAbsolute_spinBox.setDecimals(3)
        self.targetAbsolute_spinBox.setMinimum(-1000000.000000000000000)
        self.targetAbsolute_spinBox.setMaximum(10000000.000000000000000)

        self.horizontalLayout_3.addWidget(self.targetAbsolute_spinBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.currentAbsolute_lineEdit = QLineEdit(self.groupBox_3)
        self.currentAbsolute_lineEdit.setObjectName(u"currentAbsolute_lineEdit")
        self.currentAbsolute_lineEdit.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.currentAbsolute_lineEdit.sizePolicy().hasHeightForWidth())
        self.currentAbsolute_lineEdit.setSizePolicy(sizePolicy6)
        self.currentAbsolute_lineEdit.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.currentAbsolute_lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_t0_4 = QLabel(self.groupBox_4)
        self.label_t0_4.setObjectName(u"label_t0_4")
        sizePolicy3.setHeightForWidth(self.label_t0_4.sizePolicy().hasHeightForWidth())
        self.label_t0_4.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.label_t0_4)

        self.targetRelative_spinBox = QDoubleSpinBox(self.groupBox_4)
        self.targetRelative_spinBox.setObjectName(u"targetRelative_spinBox")
        sizePolicy5.setHeightForWidth(self.targetRelative_spinBox.sizePolicy().hasHeightForWidth())
        self.targetRelative_spinBox.setSizePolicy(sizePolicy5)
        self.targetRelative_spinBox.setWrapping(False)
        self.targetRelative_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.targetRelative_spinBox.setKeyboardTracking(False)
        self.targetRelative_spinBox.setProperty("showGroupSeparator", False)
        self.targetRelative_spinBox.setDecimals(4)
        self.targetRelative_spinBox.setMinimum(-10000000000.000000000000000)
        self.targetRelative_spinBox.setMaximum(100000000000.000000000000000)

        self.horizontalLayout_8.addWidget(self.targetRelative_spinBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.label_3)

        self.currentRelative_lineEdit = QLineEdit(self.groupBox_4)
        self.currentRelative_lineEdit.setObjectName(u"currentRelative_lineEdit")
        self.currentRelative_lineEdit.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.currentRelative_lineEdit.sizePolicy().hasHeightForWidth())
        self.currentRelative_lineEdit.setSizePolicy(sizePolicy6)
        self.currentRelative_lineEdit.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_9.addWidget(self.currentRelative_lineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_4.addWidget(self.groupBox_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addWidget(self.groupBox_2)


        self.retranslateUi(stageControl)

        self.cBox_stageMode.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(stageControl)
    # setupUi

    def retranslateUi(self, stageControl):
        stageControl.setWindowTitle(QCoreApplication.translate("stageControl", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("stageControl", u"Stage selection", None))
        self.cBox_stageSelection.setItemText(0, QCoreApplication.translate("stageControl", u"Newport - Time Delay", None))
        self.cBox_stageSelection.setItemText(1, QCoreApplication.translate("stageControl", u"ThorLabs - Rotation", None))

        self.pushButton_stageSettings.setText(QCoreApplication.translate("stageControl", u"Stage Settings", None))
        self.activeStab_pushButton.setText(QCoreApplication.translate("stageControl", u"Active Stabilization", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("stageControl", u"Stage position", None))
        self.stop_pushButton.setText(QCoreApplication.translate("stageControl", u"FIXED", None))
        self.offset_spinBox.setSuffix("")
        self.label_t0.setText(QCoreApplication.translate("stageControl", u"Offset", None))
        self.label_4.setText(QCoreApplication.translate("stageControl", u"Units", None))
        self.conversionFactor_lineEdit.setText("")
        self.cBox_stageMode.setItemText(0, QCoreApplication.translate("stageControl", u"Custom", None))
        self.cBox_stageMode.setItemText(1, QCoreApplication.translate("stageControl", u"Position [mm]", None))
        self.cBox_stageMode.setItemText(2, QCoreApplication.translate("stageControl", u"Time - Single Pass [ps]", None))
        self.cBox_stageMode.setItemText(3, QCoreApplication.translate("stageControl", u"Time - Single Pass [fs]", None))
        self.cBox_stageMode.setItemText(4, QCoreApplication.translate("stageControl", u"Index [no units]", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("stageControl", u"Absolute", None))
        self.label_t0_3.setText(QCoreApplication.translate("stageControl", u"Target", None))
        self.targetAbsolute_spinBox.setSuffix("")
        self.label_2.setText(QCoreApplication.translate("stageControl", u"Current", None))
        self.currentAbsolute_lineEdit.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("stageControl", u"Relative", None))
        self.label_t0_4.setText(QCoreApplication.translate("stageControl", u"Target", None))
        self.targetRelative_spinBox.setSuffix("")
        self.label_3.setText(QCoreApplication.translate("stageControl", u"Current", None))
        self.currentRelative_lineEdit.setText("")
    # retranslateUi

