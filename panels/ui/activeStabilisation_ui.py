# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'activeStabilisation.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSplitter, QVBoxLayout, QWidget)

from pyqtgraph import (ImageView, PlotWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(410, 581)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.camera_imageView = ImageView(self.splitter)
        self.camera_imageView.setObjectName(u"camera_imageView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(80)
        sizePolicy.setHeightForWidth(self.camera_imageView.sizePolicy().hasHeightForWidth())
        self.camera_imageView.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.camera_imageView)
        self.fourierMag_plotWidget = PlotWidget(self.splitter)
        self.fourierMag_plotWidget.setObjectName(u"fourierMag_plotWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(30)
        sizePolicy1.setHeightForWidth(self.fourierMag_plotWidget.sizePolicy().hasHeightForWidth())
        self.fourierMag_plotWidget.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.fourierMag_plotWidget)
        self.fourierPhase_plotWidget = PlotWidget(self.splitter)
        self.fourierPhase_plotWidget.setObjectName(u"fourierPhase_plotWidget")
        sizePolicy1.setHeightForWidth(self.fourierPhase_plotWidget.sizePolicy().hasHeightForWidth())
        self.fourierPhase_plotWidget.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.fourierPhase_plotWidget)

        self.verticalLayout_2.addWidget(self.splitter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.showImage_checkBox = QCheckBox(self.groupBox)
        self.showImage_checkBox.setObjectName(u"showImage_checkBox")
        self.showImage_checkBox.setChecked(True)

        self.verticalLayout_5.addWidget(self.showImage_checkBox)

        self.showImageROI_checkBox = QCheckBox(self.groupBox)
        self.showImageROI_checkBox.setObjectName(u"showImageROI_checkBox")
        self.showImageROI_checkBox.setChecked(True)

        self.verticalLayout_5.addWidget(self.showImageROI_checkBox)

        self.showFourierMag_checkBox = QCheckBox(self.groupBox)
        self.showFourierMag_checkBox.setObjectName(u"showFourierMag_checkBox")
        self.showFourierMag_checkBox.setChecked(True)

        self.verticalLayout_5.addWidget(self.showFourierMag_checkBox)

        self.showFourierPhase_checkBox = QCheckBox(self.groupBox)
        self.showFourierPhase_checkBox.setObjectName(u"showFourierPhase_checkBox")
        self.showFourierPhase_checkBox.setChecked(True)

        self.verticalLayout_5.addWidget(self.showFourierPhase_checkBox)


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_t0_3 = QLabel(self.groupBox_2)
        self.label_t0_3.setObjectName(u"label_t0_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_t0_3.sizePolicy().hasHeightForWidth())
        self.label_t0_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label_t0_3)

        self.P_PID_spinBox = QDoubleSpinBox(self.groupBox_2)
        self.P_PID_spinBox.setObjectName(u"P_PID_spinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.P_PID_spinBox.sizePolicy().hasHeightForWidth())
        self.P_PID_spinBox.setSizePolicy(sizePolicy3)
        self.P_PID_spinBox.setWrapping(False)
        self.P_PID_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.P_PID_spinBox.setKeyboardTracking(False)
        self.P_PID_spinBox.setDecimals(3)
        self.P_PID_spinBox.setMinimum(-1000000.000000000000000)
        self.P_PID_spinBox.setMaximum(1000000.000000000000000)

        self.horizontalLayout.addWidget(self.P_PID_spinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_t0_4 = QLabel(self.groupBox_2)
        self.label_t0_4.setObjectName(u"label_t0_4")
        sizePolicy2.setHeightForWidth(self.label_t0_4.sizePolicy().hasHeightForWidth())
        self.label_t0_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.label_t0_4)

        self.I_PID_spinBox = QDoubleSpinBox(self.groupBox_2)
        self.I_PID_spinBox.setObjectName(u"I_PID_spinBox")
        sizePolicy3.setHeightForWidth(self.I_PID_spinBox.sizePolicy().hasHeightForWidth())
        self.I_PID_spinBox.setSizePolicy(sizePolicy3)
        self.I_PID_spinBox.setWrapping(False)
        self.I_PID_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.I_PID_spinBox.setKeyboardTracking(False)
        self.I_PID_spinBox.setDecimals(3)
        self.I_PID_spinBox.setMinimum(-1000000.000000000000000)
        self.I_PID_spinBox.setMaximum(1000000.000000000000000)

        self.horizontalLayout_2.addWidget(self.I_PID_spinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_t0_5 = QLabel(self.groupBox_2)
        self.label_t0_5.setObjectName(u"label_t0_5")
        sizePolicy2.setHeightForWidth(self.label_t0_5.sizePolicy().hasHeightForWidth())
        self.label_t0_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label_t0_5)

        self.D_PID_spinBox = QDoubleSpinBox(self.groupBox_2)
        self.D_PID_spinBox.setObjectName(u"D_PID_spinBox")
        sizePolicy3.setHeightForWidth(self.D_PID_spinBox.sizePolicy().hasHeightForWidth())
        self.D_PID_spinBox.setSizePolicy(sizePolicy3)
        self.D_PID_spinBox.setWrapping(False)
        self.D_PID_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.D_PID_spinBox.setKeyboardTracking(False)
        self.D_PID_spinBox.setDecimals(3)
        self.D_PID_spinBox.setMinimum(-1000000.000000000000000)
        self.D_PID_spinBox.setMaximum(1000000.000000000000000)

        self.horizontalLayout_3.addWidget(self.D_PID_spinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.stabilize_pushButton = QPushButton(self.groupBox_3)
        self.stabilize_pushButton.setObjectName(u"stabilize_pushButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stabilize_pushButton.sizePolicy().hasHeightForWidth())
        self.stabilize_pushButton.setSizePolicy(sizePolicy4)
        self.stabilize_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.stabilize_pushButton.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.stabilize_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.phaseMeasured_lineEdit = QLineEdit(self.groupBox_3)
        self.phaseMeasured_lineEdit.setObjectName(u"phaseMeasured_lineEdit")
        self.phaseMeasured_lineEdit.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.phaseMeasured_lineEdit.sizePolicy().hasHeightForWidth())
        self.phaseMeasured_lineEdit.setSizePolicy(sizePolicy6)
        self.phaseMeasured_lineEdit.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_4.addWidget(self.phaseMeasured_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy5.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.objective_PID_spinBox = QDoubleSpinBox(self.groupBox_3)
        self.objective_PID_spinBox.setObjectName(u"objective_PID_spinBox")
        sizePolicy3.setHeightForWidth(self.objective_PID_spinBox.sizePolicy().hasHeightForWidth())
        self.objective_PID_spinBox.setSizePolicy(sizePolicy3)
        self.objective_PID_spinBox.setWrapping(False)
        self.objective_PID_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.objective_PID_spinBox.setKeyboardTracking(False)
        self.objective_PID_spinBox.setDecimals(3)
        self.objective_PID_spinBox.setMinimum(-1000000.000000000000000)
        self.objective_PID_spinBox.setMaximum(1000000.000000000000000)

        self.horizontalLayout_6.addWidget(self.objective_PID_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_5.addWidget(self.groupBox_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Display", None))
        self.showImage_checkBox.setText(QCoreApplication.translate("Form", u"Image", None))
        self.showImageROI_checkBox.setText(QCoreApplication.translate("Form", u"ROI", None))
        self.showFourierMag_checkBox.setText(QCoreApplication.translate("Form", u"Magnitude", None))
        self.showFourierPhase_checkBox.setText(QCoreApplication.translate("Form", u"Phase", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"PID", None))
        self.label_t0_3.setText(QCoreApplication.translate("Form", u"P", None))
        self.P_PID_spinBox.setSuffix("")
        self.label_t0_4.setText(QCoreApplication.translate("Form", u"I", None))
        self.I_PID_spinBox.setSuffix("")
        self.label_t0_5.setText(QCoreApplication.translate("Form", u"D", None))
        self.D_PID_spinBox.setSuffix("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Status", None))
        self.stabilize_pushButton.setText(QCoreApplication.translate("Form", u"Stabilize", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Measured", None))
        self.phaseMeasured_lineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Objective", None))
        self.objective_PID_spinBox.setSuffix("")
    # retranslateUi

