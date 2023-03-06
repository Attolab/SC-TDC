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

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import time
import pyqtgraph as pg
from PySide6 import QtCore,QtGui
from threading import Thread,Event
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
from .ui.activeStabilisation_ui import Ui_Form
import logging
import numpy as np
from collections import deque
from simple_pid import PID
logger = logging.getLogger(__name__)


class PIDModule(QWidget,Ui_Form):
    frameTimeChange = Signal(float)
    ouputPID_signal = Signal(float)

    def __init__(self,parent=None):
        super(PIDModule, self).__init__(parent)
        # Set up the user interface from Designer.
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setupWindows()
        #Phase queue
        self._maxqueue = 1000
        self.phase_trend = deque(maxlen=self._maxqueue) 
        #PID
        self.pid = PID()
        self.updatePID()
        self.connectSignals()


    def connectSignals(self,):
        self._fourierSel.sigPositionChangeFinished.connect(self.refreshQueue)
        self.ui.showFourierMag_checkBox.stateChanged.connect(self.updateGUI)
        self.ui.showFourierPhase_checkBox.stateChanged.connect(self.updateGUI)
        self.ui.showImageROI_checkBox.stateChanged.connect(self.updateGUI)
        self.ui.showImage_checkBox.stateChanged.connect(self.updateGUI)

        self.ui.P_PID_spinBox.valueChanged.connect(self.updatePID)
        self.ui.I_PID_spinBox.valueChanged.connect(self.updatePID)
        self.ui.D_PID_spinBox.valueChanged.connect(self.updatePID)
        self.ui.objective_PID_spinBox.valueChanged.connect(self.updatePID)

    def showHideWidget(self,items,show_bool = True):
        if show_bool:        
            [item.show() for item in items]
        else:
            [item.hide() for item in items]

    def updateGUI(self):
        self.showHideWidget([self.ui.fourierMag_plotWidget],self.ui.showFourierMag_checkBox.isChecked())
        self.showHideWidget([self.ui.fourierPhase_plotWidget],self.ui.showFourierPhase_checkBox.isChecked())
        self.showHideWidget([self.ui.camera_imageView],self.ui.showImage_checkBox.isChecked())

    def refreshQueue(self,):
        self.phase_trend.clear()

    def updatePID(self,):
        self.pid.tunings =(self.ui.P_PID_spinBox.value(),self.ui.I_PID_spinBox.value(),self.ui.D_PID_spinBox.value())
        self.pid.setpoint = self.ui.objective_PID_spinBox.value()
        self._phaseObj.setValue(self.pid.setpoint)
    def updateData(self,):
        self.data = np.random.rand(1)*np.cos(np.random.rand(1)*self.X)+np.random.rand(1)+np.sin(np.random.rand(1)+self.Y)        
        self.ui.camera_imageView.setImage(self.data, autoRange=False)
        self.ui.camera_imageView.roiClicked = self.roiClicked
        x,y = self.ui.camera_imageView.roiCurves[0].getData()
        Npad = 2**(len(x)-1).bit_length()
        Npad = 2048
        F = np.fft.fft(y,Npad)
        F = F[:int(Npad/2)]        
        idx = int(self._fourierSel.getXPos())
        mag = np.abs(F[idx])
        phaseMeasured = np.angle(F[idx])
        self._fourierMag.setData(np.abs(F),autoRange=False)    
        if mag >= self._fourierLim.getYPos():
            self.ui.phaseMeasured_lineEdit.setText(str(phaseMeasured))
            self.phase_trend.append(np.angle(F[idx]))
            self._fourierPhase.setData(self.phase_trend)
            self.label.setText(str(np.std(self.phase_trend)))

        # print(self.pid(phaseMeasured))
        self.ouputPID_signal.emit(self.convert_rad_to_nm(self.pid(phaseMeasured)))



    def convert_rad_to_nm(self,input):
        return 2.11146/(2*np.pi)*299.792458/2*input

    def start(self,):
        print('Go')
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateData)
        self.timer.start(100)        
    # def hideEvent(self,a):
    #     print('hidden')
    # def showEvent(self,a):
    #     print('Shown')

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.timer.stop()
        return super().closeEvent(event)
    def setupWindows(self,):
        self.ui.camera_imageView.ui.roiBtn.setChecked(True) #Activate ROI
        cameraSize = [256,256]
        x = np.arange(cameraSize[0])
        y = np.arange(cameraSize[1])
        self.X,self.Y = np.meshgrid(x,y)

        self._fourierMag = pg.PlotDataItem()
        self.ui.fourierMag_plotWidget.addItem(self._fourierMag)
        self.ui.fourierMag_plotWidget.setLabel('bottom',text='Frequency')
        self.ui.fourierMag_plotWidget.setLabel('left',text='Magnitude')
        self.ui.fourierMag_plotWidget.showGrid(True)        
        self._fourierSel = pg.InfiniteLine(movable=True)
        self.ui.fourierMag_plotWidget.addItem(self._fourierSel)
        self._fourierLim = pg.InfiniteLine(movable=True,angle=0)
        self.ui.fourierMag_plotWidget.addItem(self._fourierLim)

        self._fourierPhase = pg.PlotDataItem()
        self.ui.fourierPhase_plotWidget.addItem(self._fourierPhase)
        self.ui.fourierPhase_plotWidget.setLabel('bottom',text='Measurement')
        self.ui.fourierPhase_plotWidget.setLabel('left',text='Hits')
        self._phaseObj = pg.InfiniteLine(movable=False,angle=0)
        self.ui.fourierPhase_plotWidget.addItem(self._phaseObj)
        self.label = pg.LabelItem(justify = "left")
        self.ui.fourierPhase_plotWidget.addItem(self.label)


 
    def roiClicked(self):
        if self.ui.camera_imageView.ui.roiBtn.isChecked():
            self.ui.camera_imageView.ui.roiPlot.setMouseEnabled(True, True)
            self.ui.camera_imageView.ui.splitter.handle(1).setEnabled(True)
            self.ui.camera_imageView.roiChanged()
            for c in self.ui.camera_imageView.roiCurves:
                c.show()
            self.ui.camera_imageView.ui.roiPlot.showAxis('left')
        else:
            self.ui.camera_imageView.roi.hide()
            self.ui.camera_imageView.ui.roiPlot.setMouseEnabled(False, False)
            for c in self.ui.camera_imageView.roiCurves:
                c.hide()
            self.ui.camera_imageView.ui.roiPlot.hideAxis('left')
        self.ui.camera_imageView.ui.roiPlot.setVisible(self.ui.showImageROI_checkBox.isChecked())


        
def main():
    import sys
    import logging
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    app = QApplication([])    
    # screen_resolution = app.desktop().screenGeometry()
    # width, height = screen_resolution.width(), screen_resolution.height()
    config = PIDModule()

    # config.showMaximized()
    # config._screen = app.primaryScreen()        
    # rect = config._screen.geometry()
    # config.setGeometry(QRect(0,rect.height()*0.025,rect.width()*0.5,rect.height()*.925))
    config.show()

    app.exec_()

if __name__=="__main__":
    main()