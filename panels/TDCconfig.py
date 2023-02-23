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
    startThreadSignal = QtCore.Signal()
    endThreadSignal = QtCore.Signal()
    connectSignal = QtCore.Signal()
    disconnectSignal = QtCore.Signal()
    def __init__(self,parent=None):
        super(TDCConfig, self).__init__(parent)

        # Set up the user interface from Designer.
        self.setupUi(self)  
        self.connectSignals()
        
    def connectSignals(self):
        self.openPath_pushButton.clicked.connect(self.openPath)
        self.exposureTime_lineEdit.returnPressed.connect(self.exposureTimeChange)
        self.startThread_pushButton.clicked.connect(self.startThreadSignal.emit)
        self.stopThread_pushButton.clicked.connect(self.endThreadSignal.emit)
        self.initialize_pushButton.clicked.connect(self.connectSignal.emit)
        self.deinitialize_pushButton.clicked.connect(self.disconnectSignal.emit)
        self.folderPath_lineEdit.returnPressed.connect(self.configurationFileChange)
        self.filename_lineEdit.returnPressed.connect(self.configurationFileChange)
    def openPath(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Directory",
                                             "/home",
                                             QtWidgets.QFileDialog.ShowDirsOnly
                                             | QtWidgets.QFileDialog.DontResolveSymlinks)

        self.folderPath_lineEdit.setText(directory)


    def isDeviceInitialized(self,isInitialized):
        if isInitialized:
            self.connectionStatus_label.setText('ON')
            self.initialize_pushButton.setEnabled(False)
            self.deinitialize_pushButton.setEnabled(True)
            self.folderPath_lineEdit.setEnabled(False)
            self.filename_lineEdit.setEnabled(False)            
        else:
            self.connectionStatus_label.setText('OFF')
            self.deinitialize_pushButton.setEnabled(False)
            self.initialize_pushButton.setEnabled(True)
            self.folderPath_lineEdit.setEnabled(True)
            self.filename_lineEdit.setEnabled(True)
            
    def exposureTimeChange(self,):
        exposureTime = int(self.exposureTime_lineEdit.text())
        self.updateExposureTimeChange.emit(exposureTime)

    def configurationFileChange(self,):
        import os
        libpath = os.path.join(self.folderPath_lineEdit.text(),self.filename_lineEdit.text())
        self.updateLibPathChange.emit(libpath)