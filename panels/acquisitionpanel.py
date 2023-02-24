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
from PySide6 import QtCore,QtGui,QtWidgets
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
from core.threading import BasicThread,RepeatThread
from core.filesaver import FileSaver
import logging
import os
from datetime import date 

logger = logging.getLogger(__name__)


class AcquisitionPanel(QWidget,Ui_Form):
    closeFile = Signal()
    signal_UpdateIndexing = Signal(object)

    def __init__(self,parent=None):
        super(AcquisitionPanel, self).__init__(parent)

        # Set up the user interface from Designer.
        self.setupUi(self)  
        self._stageDelays = np.asarray([])
        self._convertDatathread = None
        self.connectSignals()
        self.initializeDate()
        self.folderPath_lineEdit.setText(self.initializeDate())

        # Acquisition status
        self._in_acq = False
        self._stop_all_acquisitions = False

        # FileSaver class
        self._filesaver = FileSaver()
        self.closeFile.connect(self._filesaver.closeFiles)
        self._filesaver.start()
        # Timer thread
        self._elapsed_time_thread = QtCore.QTimer()
        self._elapsed_time = QtCore.QElapsedTimer()
        self._elapsed_time_thread.timeout.connect(self.updateTimer)
        self._elapsed_time_thread.start(1000)        

        # Repeating thread
        self._repeating_thread = None

    @property
    def fileSaver(self):
        return self._filesaver

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
        self.start_acq_pushButton.clicked.connect(self.startAcqClicked)
        self.end_acq_pushButton.clicked.connect(self.endAcqClicked)
        self.openPath_pushButton.clicked.connect(self.openPath)
        self.signal_UpdateIndexing.connect(self.updateIndexing)
        
    def openPath(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Directory",
                                             "/home",
                                             QtWidgets.QFileDialog.ShowDirsOnly
                                             | QtWidgets.QFileDialog.DontResolveSymlinks)
        if bool(directory):
            self.folderPath_lineEdit.setText(directory)            
    
    
    def updatePosition(self,pos):
        self.status_position.setText(f'{pos}')

    def savePositionArray(self,position_array):
        self._stageDelays = position_array

    def updateIndexing(self,event):
        position_array,index,steps = event
        self.status_position.setText(self.makeFormatOuput(position_array[0], position_array[-1]))
        self.status_image.setText(self.makeFormatOuput(index[0],index[-1]))
        self.status_steps.setText(self.makeFormatOuput(steps[0],steps[-1]))
        acq_time = float(self.acquisitionTime_lineEdit.text())        
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

    def _collectAcquisitionSettings(self):
        # Position array
        # position_array = acq._stageDelays
        position_array = np.zeros((5,))
        # Filename
        filename = os.path.join(self.folderPath_lineEdit.text(),self.filePrefix_lineEdit.text())
        logger.info('Filename to store to: {}'.format(filename))
        # # Index
        index = 0
        # index = acq.startindex.value()
        # # Check for valid index
        # index = self.check_index(filename,0)
        # Updated index value
        # logger.info('Start index is {}'.format(index))
        # acq.startindex.setValue(index)        
        acq_time = float(self.acquisitionTime_lineEdit.text())
        logger.info('Acq time is {} s'.format(acq_time))
        # logger.info(f'Number of steps is {len(position_array)}')
        # logger.info('Will repeat this {} times'.format(repeats))        
        return filename,index,acq_time,position_array

    def run_acquisition(self,acq_time,filename,index,position_array):
        numberofsteps = len(position_array) 
        final_index = index+numberofsteps-1
        currentstep = 0  
        print(position_array)          
        for pos in position_array:
            if not self._stop_all_acquisitions:
                self._in_acq = True
                currentstep += 1
                # Move the stage
                # self.signal_LaunchStageMotion.emit(pos)
                # Initialize the variable such that the following while wait for the variable to change before pursuing
                self._stage_ismoving = False
                # Update current position / index and step number
                self.signal_UpdateIndexing.emit(([pos, position_array[-1]], [index , final_index],[currentstep , numberofsteps]))
                # Wait for the stage to reach its final position
                while self._stage_ismoving:
                            time.sleep(0.1)                            
                try:
                    if self._in_acq:
                        #Open selected files except log
                        self._filesaver.openFiles(filename,index,tof=1,log=0)
                        self.status_label.setText('Acquiring...')        
                        logger.info('Starting Acquisition')
                        start = time.time()
                        time_val = 10*acq_time
                        if acq_time != -1:
                            start = time.time()
                            timeSpent = time.time() - start

                            while timeSpent < acq_time and self._in_acq and not(self._stop_all_acquisitions):
                                # pPB(round(timeSpent,1)*10, time_val, prefix = 'Progress:', suffix = 'Complete', length = 50)
                                time.sleep(0.05)
                                timeSpent = time.time() - start

                        self.endAcquisition()
                        tot_time = time.time()-start
                        logger.info('ENDING, time taken {}s or {} minutes'.format(tot_time,tot_time/60.0))                    
                        # # Saving parameters
                        # voltage = self.acqtab.bias_voltage.value()
                        # finethreshold = self.acqtab.fine_threshold.value()
                        # coarsethreshold = self.acqtab.coarse_threshold.value()
                        # #Open only log
                        # self._filesaver.openFiles(filename,index,0,0,0,0,1)                    
                        # # Saving image number, acquisition time, stage position, voltage, fine threshold, coarse threshold                    
                        # self._filesaver.writeLog(filename,index,round(tot_time),pos,voltage,finethreshold,coarsethreshold)
                        # self._filesaver.closeLogFile()
                        index += 1


                except Exception as e:
                    logger.error(str(e))
                    return
    def startAcqClicked(self):
        self._stop_all_acquisitions = False
        filename,index,acq_time,position_array = self._collectAcquisitionSettings()
        if self._repeating_thread is not None:
            self._repeating_thread.cancel()
            self._repeating_thread = None
        self.start_acq_pushButton.setEnabled(False)
        self.end_acq_pushButton.setEnabled(True)            
        self._repeating_thread = RepeatThread(1,self.run_acquisition,(acq_time,filename,index,position_array))
        self._repeating_thread.start()
        self._elapsed_time.restart()          

    def endAcqClicked(self):
        # self.acqtab.end_movingstage()
        self._stop_all_acquisitions = True
        self.endAcquisition()
        if self._repeating_thread is not None:
            self.start_acq_pushButton.setEnabled(True)
            self.end_acq_pushButton.setEnabled(False)            
            self._repeating_thread.cancel()
            self._repeating_thread = None 

    def endAcquisition(self):
        self.closeFile.emit()    
        self._in_acq = False
        self.status_label.setText('Live')
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
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self._elapsed_time_thread.stop()
        return super().closeEvent(event)

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