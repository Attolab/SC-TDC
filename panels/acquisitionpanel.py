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
from pyqtgraph.Qt import QtCore, QtGui
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,QTimer,QElapsedTimer,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal,QProcess)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QWindow,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QWidget,QDockWidget,QFileDialog,QTableWidgetItem,QHBoxLayout)
from .ui.acquisitionpanel_ui import Ui_Form
import numpy as np
import threading
from threading import Thread
import logging
import os
from datetime import date 

logger = logging.getLogger(__name__)


class RepeatFunction(Thread):
    """Call a function after a specified number of seconds:

            t = Timer(30.0, f, args=[], kwargs={})
            t.start()
            t.cancel()     # stop the timer's action if it's still waiting

    """

    def __init__(self, n_repeats, function, args=[], kwargs={}):
        Thread.__init__(self)
        self.repeats = n_repeats
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = threading.Event()
        # self.motion_stopped = threading.Condition()

    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.finished.set()

    def run(self):
        self._currentrepeat = 0
        while not self.finished.is_set() and self._currentrepeat < self.repeats:
            self.function(*self.args, **self.kwargs)
            self._currentrepeat +=1
        self.finished.set()


class AcquisitionPanel(QWidget,Ui_Form):
    # biasVoltageChange = QtCore.pyqtSignal(int)
    

    def __init__(self,parent=None):
        super(AcquisitionPanel, self).__init__(parent)

        # Set up the user interface from Designer.
        self.setupUi(self)  
        self._stageDelays = np.asarray([])
        self._convertDatathread = None
        self.connectSignals()
        self.initializeDate()
        self.folderPath_lineEdit.setText(self.initializeDate())

        self._in_acq = False
        self._repeating_thread = None
        self._stop_all_acquisitions = False

        # Timer thread
        # self._elapsed_time_thread = QtCore.QTimer()
        # self._elapsed_time = QtCore.QElapsedTimer()
        # self._elapsed_time_thread.timeout.connect(self.updateTimer)
        # self._elapsed_time_thread.start(1000)        

    def initializeDate(self):
        today = date.today()
        # year = datetime.year()
        folder_init = os.getcwd()
        current_directory = os.path.join(folder_init,today.strftime("%Y%m%d"))
        # current_directory = os.path.join(folder_init,today.strftime("%Y"),today.strftime("%Y%m%d"))
        if not(os.path.isdir(current_directory)):
            os.mkdir(current_directory)        
        return current_directory

    def connectSignals(self):
        # self.start_acq_pushButton.clicked.connect(self.startAcqClicked)
        # self.end_acq_pushButton.clicked.connect(self.endAcqClicked)
        self.openPath_pushButton.clicked.connect(self.openPath)
        
    def openPath(self):
        # current_dir = self.folderPath_lineEdit.text(directory)

        directory = QtGui.QFileDialog.getExistingDirectory(self, "Open Directory",
                                             "/home",
                                             QtGui.QFileDialog.ShowDirsOnly
                                             | QtGui.QFileDialog.DontResolveSymlinks)
        if directory is not None:
            self.folderPath_lineEdit.setText(directory)            
            # self.folderPath_lineEdit.setText(current_dir)


    
    
    def updatePosition(self,pos):
        self.status_position.setText(f'{pos}')


    def savePositionArray(self,position_array):
        self._stageDelays = position_array


    def updateIndexing(self,position_array,index,steps):
        self.status_position.setText(self.makeFormatOuput(position_array[0], position_array[-1]))
        self.status_image.setText(self.makeFormatOuput(index[0],index[-1]))
        self.status_steps.setText(self.makeFormatOuput(steps[0],steps[-1]))
        acq_time = float(self.acq_time.text())
        
        # Estimate the length of the scan:
        stageVelocity = 1.0 # mm/s
        totalStageMotion = np.sum(np.abs(np.diff(self._stageDelays)))
        scanLengthEstimate = acq_time*steps[-1] + totalStageMotion * 1.0/stageVelocity
        remainingStageMotion = np.sum(np.abs(np.diff(self._stageDelays[steps[0]:])))
        scanLengthRemaining = acq_time*(steps[-1] - steps[0]+1) + remainingStageMotion * 1.0/stageVelocity
        h_remaining,m_remaining,s_remaining = self.makeHoursMinutesSeconds(scanLengthRemaining)
        h_total,m_total,s_total = self.makeHoursMinutesSeconds(scanLengthEstimate)
        self.status_scanLength.setText(f"{h_remaining}h {m_remaining} m {s_remaining} s / {h_total}h {m_total} m {s_total} s")

    #Output for GUI
    def makeFormatOuput(self,input1,input2):
        return f'{input1}/{input2}'    
    def makeHoursMinutesSeconds(self,seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        s = int(round(s))
        m = int(round(m))
        h = int(round(h))
        return h,m,s
    def run_acquisition(self,):
        print(time.time())
    def startAcqClicked(self):
        self._stop_all_acquisitions = False

        # filename,index,raw,toa,tof,blob,acq_time,repeats,position_array = self._collectAcquisitionSettings()

        if self._repeating_thread is not None:
            self._repeating_thread.cancel()
            self._repeating_thread = None
        self._repeating_thread = RepeatFunction(5,self.run_acquisition,())        

        # self._repeating_thread = RepeatFunction(repeats,self.run_acquisition,(acq_time,filename,index,raw,toa,tof,blob,position_array))        
        self._repeating_thread.start()
        self._elapsed_time.restart()   
    def endAcqClicked(self):
        # self.acqtab.end_movingstage()
        self._stop_all_acquisitions = True
        self.endAcquisition()
        if self._repeating_thread is not None:
            self._repeating_thread.cancel()
            self._repeating_thread = None 

    def endAcquisition(self):
        self.text_status.setText('Live')
        self._in_acq = False
        self.closeFile.emit()
        self._elapsed_time.restart()


    def updateTimer(self):
        if self._in_acq:
            seconds = self._elapsed_time.elapsed()/1000
            h,m,s = self.makeHoursMinutesSeconds(seconds)
            self.elapsed_time_s.display(int(round(s)))
            self.elapsed_time_m.display(int(round(m)))
            self.elapsed_time_h.display(h)
    def makeHoursMinutesSeconds(self,seconds):
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            return h,m,s

def main():
    import sys
    import logging
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    app = QApplication([])

    
    config = AcquisitionPanel()
    # app.lastWindowClosed.connect(config.closeDevice)
    config.show()
    
    app.exec_()
if __name__=="__main__":
    main()