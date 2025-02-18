#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright 2021 Surface Concept GmbH

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

-------------------------------------------------------------------------------

Created on Wed Jun 16 17:15:00 2021

WARNING: This example can potentially create a very large text file.
Tune down the EXPOSURE_MS variable and the NR_OF_MEASUREMENTS, if you
run this example with hardware with a high rate of events.

Test of the buffered-data callbacks interface for *** TDC events ***
(suitable if you have a "stand-alone" TDC without delay-line detector
or if you operate a delay-line detector with "SD_Format=-1" setting
and you are interested in the TDC events on the individual channels).
Write event data to a text file (no matplotlib needed).
Similarly to example_buffered_data_callbacks3.py, the processing is
delegated to the main thread which is recommended over processing in the
'on_data' callback.
Here, we request data at the end of every measurement. This makes it
easier to include measurement separator lines in the output file.
The logic is still a bit tricky. When the 'end_of_meas' callback is
invoked, and we return True, the next 'on_data' callback will deliver
the remaining buffered data of the current measurement. The order of
last data chunk and end-of-measurement notification is sorted in the
BufDataCB4 class, so the main thread will receive them in a sensible
order.
Formatting the arrays to a textual form via the savetxt function
of numpy seems to take quite some computational time. For productive
use cases, other forms of data export are recommended that provide a
higher performance in speed and disk space.
(However for demo purposes, the text file export allows to view the
output with an ordinary editor).
"""

import Library.scTDC as scTDC
import time
import timeit
from dataBuffer import BufDataCB5
from DataToFile import DataToTextfile
from ast import Param
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,QFileInfo,QSettings,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal,QProcess)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QWindow,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QWidget,QDockWidget,QFileDialog,QTableWidgetItem,QHBoxLayout)
from panels.timeofflight import TimeOfFlightPanel
from panels.acquisitionpanel import AcquisitionPanel
from panels.viewerconfig import ViewerConfig
from panels.TDCconfig import TDCConfig
from panels.stageControl import StageControl
from SC_TDC import SC_TDC
import logging

# -----------------------------------------------------------------------------
# example 4 of deriving from buffered_data_callbacks_pipe

NR_OF_MEASUREMENTS = 2    # number of measurements
EXPOSURE_MS = 100         # exposure duration in milliseconds
OUTPUT_TEXTFILE_NAME = "tmp_textfile1357.txt" # this file will be overwritten!

# define some constants to distinguish the type of element placed in the queue
QUEUE_DATA = 0
QUEUE_ENDOFMEAS = 1

# def sortData(eventtype,data):
#     if eventtype == QUEUE_DATA:
#         return data
#     elif eventtype == QUEUE_ENDOFMEAS:
#         return 0
# def restore(settings):
#     finfo = QFileInfo(settings.fileName())
#     if finfo.exists() and finfo.isFile():
#         for w in QApplication.allWidgets():
#             mo = w.metaObject()
#             if w.objectName() != "":
#                 for i in range(mo.propertyCount()):
#                     name = mo.property(i).name()
#                     val = settings.value("{}/{}".format(w.objectName(), name), w.property(name))
#                     w.setProperty(name, val)

# def save(settings):
#     for w in QApplication.allWidgets():
#         mo = w.metaObject()
#         if w.objectName() != "":
#             for i in range(mo.propertyCount()):
#                 name = mo.property(i).name()
#                 settings.setValue("{}/{}".format(w.objectName(), name), w.property(name))
class SC_TDC_viewer(QMainWindow,):
    clearNow = Signal()
    displayNow = Signal()
    refreshNow = Signal()
    settingsChanged = Signal()
    onTof = Signal(object)
    resetTof = Signal()
    closeDevice_signal = Signal()
    settings = QSettings("gui.ini", QSettings.IniFormat)

    def __init__(self,parent=None,):
        super(SC_TDC_viewer, self).__init__(parent)
        # Initialize windows
        self.setupWindows()
        self.start_TDC()
        self.connectSignals()
        self._display_rate = 1/5
        self._last_update = 0
        self._last_frame = 0.0
        self._frame_time = -1.0
        self.readSettings()


    def readSettings(self,):        
        self.restoreGeometry(self.settings.value("geometry"));
        self.restoreState(self.settings.value("windowState"));
        # restore(self.settings)

        # self.geometry()
        # a = self.geometry().getRect()
        # self.resize(self.size().height(),self.size().width())


    def start_TDC(self):
        # Initialize device in a separate class
        self.TDC = SC_TDC(adress="C:\\Users\\attose1_VMI\\Documents\\Python_Scripts\\scTDC\\scTDC_Python_SDK_v1.3.0\\scTDC_Py\\Library\\",
        filename="tdc_gpx3.ini",exposureTime=100)
        self.TDC.dataCallback = self.onData


    for w in QApplication.allWidgets():
        try:
             if w.objectName() == 'Viewer configuration':
                print(1)
        except:
            pass
        
    def setupWindows(self):
        # TDC configuration
        self._TDC_config_panel = TDCConfig(self)
        self._dock_TDC_config = QDockWidget('TDC configuration',parent=self,objectName='dock_tdcConfig')
        # self._dock_TDC_config.setObjectName('TDC_Config')
        self._dock_TDC_config.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self._dock_TDC_config.setWidget(self._TDC_config_panel)
        self.addDockWidget(Qt.LeftDockWidgetArea,self._dock_TDC_config)         
        # Viewer configuration
        self._viewer_config_panel = ViewerConfig(self)
        self._dock_viewer_config = QDockWidget('Viewer configuration',parent=self,objectName='dock_viewerConfig')
        self._dock_viewer_config.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self._dock_viewer_config.setWidget(self._viewer_config_panel)
        self.addDockWidget(Qt.LeftDockWidgetArea,self._dock_viewer_config)         
        # Acquisition panel used for acquisition parameters
        self._acq_panel = AcquisitionPanel(self)
        self._dock_acq = QDockWidget('Acquisition',parent=self,objectName='dock_acquisitionConfig')
        self._dock_acq.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self._dock_acq.setWidget(self._acq_panel)
        self.addDockWidget(Qt.LeftDockWidgetArea,self._dock_acq) 
        # # Stage control panel used for acquisition parameters
        self._stage_panel = StageControl(self)
        self._dock_stage = QDockWidget('Stage control',parent=self,objectName='dock_stageControl')
        self._dock_stage.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self._dock_stage.setWidget(self._stage_panel)
        self.addDockWidget(Qt.LeftDockWidgetArea,self._dock_stage) 
        # Tof panel used for display
        self._tof_panel = TimeOfFlightPanel(self)
        self._dock_tof = QDockWidget('Time of Flight',parent=self,objectName='dock_ToFViewer')
        self._dock_tof.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self._dock_tof.setWidget(self._tof_panel)
        self.addDockWidget(Qt.RightDockWidgetArea,self._dock_tof)    
        self.tabifyDockWidget(self._dock_acq,self._dock_viewer_config)
        self.tabifyDockWidget(self._dock_viewer_config,self._dock_TDC_config)

        # self._stageControl_panel.setMaximumWidth(500)
        # self._acq_panel.setMaximumWidth(500)
        # self.showFullScreen()
        # self.setWindowFlags()
        self.setTabPosition(Qt.LeftDockWidgetArea,QTabWidget.TabPosition.North)
        # mainWindow->setWindowFlags(Qt::CustomizeWindowHint | Qt::FramelessWindowHint)
        # self.setTabPosition()
        self._tof_panel.showMaximized()
        # QMainWindow::tabifyDockWidget(QDockWidget *first, QDockWidget *second)
    def connectSignals(self,):
        self._TDC_config_panel.startThread_signal.connect(self.TDC.start_thread)
        self._TDC_config_panel.endThread_signal.connect(self.TDC.stop_thread)
        self._TDC_config_panel.connect_signal.connect(self.TDC.connectDevice)
        self._TDC_config_panel.disconnect_signal.connect(self.TDC.disconnectDevice)
        self._TDC_config_panel.updateExposureTimeChange.connect(self.onExposureTimeUpdate)
        self._TDC_config_panel.updateLibPathChange.connect(self.onLibPathChangeUpdate)

        self.TDC.isDeviceInitialized_Signal.connect(self._TDC_config_panel.isDeviceInitialized)


        self._viewer_config_panel.updateRateChange.connect(self.onDisplayUpdate)
        self._viewer_config_panel.frameTimeChange.connect(self.onFrameTimeUpdate)        
        self._viewer_config_panel.resetPlots.connect(self.clearNow.emit)


        self.clearNow.connect(self._tof_panel.clearTof)
        self.refreshNow.connect(self._tof_panel.refreshTof)

        self.onTof.connect(self._tof_panel.onEvent)
        self.onTof.connect(self._acq_panel.fileSaver.onTof)

        self.displayNow.connect(self._tof_panel.displayTof)

        self.closeDevice_signal.connect(self.TDC.closeDevice)

        # self._acq_panel.start_acq_pushButton.clicked.connect(self._stageControl_panel.parseDelayInput)

        self._stage_panel.signal_stagepositionfixed.connect(self._acq_panel.isStageReady)        

        # self._acq_panel.end_acq_pushButton.clicked.connect(self.TDC.stop_thread)
        # self._acq_panel.start_acq_pushButton.clicked.connect(self.TDC.start_thread)

        self._acq_panel.signal_goToPosition.connect(self._stage_panel.receivePositionCommand)


    def closeDevice(self):
        self.closeDevice_signal.emit()

    def onLibPathChangeUpdate(self,value):
        logging.info('Library path changed to {}'.format(value))
        self.TDC.libPath = value

    def onExposureTimeUpdate(self,value):
        logging.info('Exposure Time changed to {} ms'.format(value))
        self.TDC.exposureTime = value

    def onDisplayUpdate(self,value):
        logging.info('Display rate changed to {} s'.format(value))
        self._display_rate = value

    def onFrameTimeUpdate(self,value):
        logging.info('Frame time set to {} s'.format(value))
        self._frame_time = value

    def onData(self,event_type,data):
        # print(data)
        # print(timeit.default_timer())
        #Measure continously
        check_update = time.time()

        #Refresh rate
        if self._frame_time >=0 and (check_update-self._last_frame) > self._frame_time:
            self.refreshNow.emit()
            self._last_frame = time.time()
        if event_type == 0:
            # print('Data')            
            self.onTof.emit(data)

        # elif event_type == 1:
        #     print('Measurement')

        if (check_update-self._last_update) > self._display_rate:            
            self.displayNow.emit()
            self._last_update = time.time()      

    def closeEvent(self, event):
        
        # settings=QSettings("MyCompany", "MyApp");
        self.settings.setValue("geometry", self.saveGeometry());
        self.settings.setValue("windowState", self.saveState());
        QMainWindow.closeEvent(self,event);        
        # save(self.settings)
        # QWidget.closeEvent(self, event)
    # def exitGUI(self):
        # self.close()
            # time.sleep(1.0)
            # print(timeit.default_timer())            
    # # enter a scope where the text file is open
    # with DataToTextfile(OUTPUT_TEXTFILE_NAME) as data_to_textfile:
    #     # event loop
    #     meas_remaining = NR_OF_MEASUREMENTS
    #     while True:
    #         eventtype, data = bufdatacb.queue.get()  # waits until element available
    #         if eventtype == QUEUE_DATA:
    #             data_to_textfile.process_data(data)
    #         elif eventtype == QUEUE_ENDOFMEAS:
    #             data_to_textfile.write_measurement_separator()

def main():
    import sys
    import logging
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    app = QApplication([])    
    # screen_resolution = app.desktop().screenGeometry()
    # width, height = screen_resolution.width(), screen_resolution.height()
    config = SC_TDC_viewer()




    app.lastWindowClosed.connect(config.closeDevice)

    config.showMaximized()
    config._screen = app.primaryScreen()        
    rect = config._screen.geometry()
    config.setGeometry(QRect(0,rect.height()*0.025,rect.width()*0.5,rect.height()*.925))
    config.show()

    app.exec_()

if __name__=="__main__":
    main()