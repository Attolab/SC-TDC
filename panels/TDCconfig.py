##############################################################################
##
# This file is part of pymepixviewer
#
# https://arxiv.org/abs/1905.07999
#
#
# pymepixviewer is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pymepixviewer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pymepixviewer.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import time
import pyqtgraph as pg
from PySide6 import QtWidgets,QtCore,QtGui
# from pyqtgraph.Qt import QtCore, QtGui
from .ui.TDCconfig_ui import Ui_Form
import numpy as np
import threading
from threading import Thread
import logging
import os
from datetime import date 

logger = logging.getLogger(__name__)


class TDCConfig(QtWidgets.QWidget,Ui_Form):
    updateExposureTimeChange = QtCore.Signal(int)
    updateLibPathChange = QtCore.Signal(str) 
    startThread_signal = QtCore.Signal()
    endThread_signal = QtCore.Signal()
    connect_signal = QtCore.Signal()
    disconnect_signal = QtCore.Signal()
    def __init__(self,parent=None):
        super(TDCConfig, self).__init__(parent)

        # Set up the user interface from Designer.
        # self.setupUi(self)  
        self.ui = Ui_Form()
        self.ui.setupUi(self)  
        self.setupWindows()
        self.connectSignals()

    def setupWindows(self):
        self.ui.startThread_pushButton.setEnabled(True)
        self.ui.stopThread_pushButton.setEnabled(False)


    def connectSignals(self):
        self.ui.openPath_pushButton.clicked.connect(self.openPath)
        self.ui.exposureTime_lineEdit.returnPressed.connect(self.exposureTimeChange)
        self.ui.startThread_pushButton.clicked.connect(self.startThread)
        self.ui.stopThread_pushButton.clicked.connect(self.endThread)
        # self.startThread_pushButton.clicked.connect(self.startThreadSignal.emit)
        # self.stopThread_pushButton.clicked.connect(self.endThreadSignal.emit)        
        self.ui.initialize_pushButton.clicked.connect(self.connect_signal.emit)
        self.ui.deinitialize_pushButton.clicked.connect(self.disconnect_signal.emit)
        self.ui.folderPath_lineEdit.returnPressed.connect(self.configurationFileChange)
        self.ui.filename_lineEdit.returnPressed.connect(self.configurationFileChange)
    def openPath(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Directory",
                                             "/home",
                                             QtWidgets.QFileDialog.ShowDirsOnly
                                             | QtWidgets.QFileDialog.DontResolveSymlinks)

        self.ui.folderPath_lineEdit.setText(directory)


    def startThread(self):
        self.startThread_signal.emit()
        self.ui.startThread_pushButton.setEnabled(False)
        self.ui.stopThread_pushButton.setEnabled(True)
    def endThread(self):
        self.endThread_signal.emit()
        self.ui.startThread_pushButton.setEnabled(True)
        self.ui.stopThread_pushButton.setEnabled(False)

    def isDeviceInitialized(self,isInitialized):
        if isInitialized:
            self.ui.connectionStatus_label.setText('ON')
            self.ui.initialize_pushButton.setEnabled(False)
            self.ui.deinitialize_pushButton.setEnabled(True)
            self.ui.folderPath_lineEdit.setEnabled(False)
            self.ui.filename_lineEdit.setEnabled(False)            
        else:
            self.ui.connectionStatus_label.setText('OFF')
            self.ui.deinitialize_pushButton.setEnabled(False)
            self.ui.initialize_pushButton.setEnabled(True)
            self.ui.folderPath_lineEdit.setEnabled(True)
            self.ui.filename_lineEdit.setEnabled(True)
            
    def exposureTimeChange(self,):
        exposureTime = int(self.ui.exposureTime_lineEdit.text())
        self.updateExposureTimeChange.emit(exposureTime)

    def configurationFileChange(self,):
        import os
        libpath = os.path.join(self.folderPath_lineEdit.text(),self.filename_lineEdit.text())
        self.updateLibPathChange.emit(libpath)