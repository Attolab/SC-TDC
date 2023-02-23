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
from PySide6.QtWidgets import QWidget
# from PySide6.Qt import QWidget
import numpy as np
# from .ui.timeofflightpanelui import Ui_Form
from .ui.timeofflightpanel_ui import Ui_Form
import traceback
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal,QProcess)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QWindow,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QWidget,QDockWidget,QFileDialog,QTableWidgetItem,QHBoxLayout)    
from collections import deque
class TimeOfFlightPanel(QWidget,Ui_Form):

    def __init__(self,parent=None):
        super(TimeOfFlightPanel, self).__init__(parent)

        # Set up the user interface from Designer.
        self.setupUi(self)
        self._histo_x = None
        self._histo_y = None
        self._tof_data = pg.PlotDataItem()
        self.tof_view.addItem(self._tof_data)
        self.tof_view.setLabel('bottom',text='Time of Flight',units='s')
        self.tof_view.setLabel('left',text='Hits')        
        self._yield_data = pg.PlotDataItem()
        self.yield_view.addItem(self._yield_data)
        self.yield_view.setLabel('bottom',text='Measurement')
        self.yield_view.setLabel('left',text='Hits')

        self._tof_start = 0.0
        self._tof_end = 1000.0
        self._tof_bin = 10000
        self._maxqueue = 1000
        self.makeBlobTrendQueue()
        self.setupTofConfig()
        self.connectSignals()

    def makeBlobTrendQueue(self,):
        self._counts_trend = deque(maxlen=self._maxqueue) 
        self._counts_trend_trigger = deque(maxlen=self._maxqueue)        

    def connectSignals(self):
        self.update_config.clicked.connect(self.onUpdateTofConfig)
        self.event_start.returnPressed.connect(self.onUpdateTofConfig)
        self.event_end.returnPressed.connect(self.onUpdateTofConfig)
        self.bin_size.returnPressed.connect(self.onUpdateTofConfig)
        self.max_queue.returnPressed.connect(self.onUpdateTofConfig)

    def clearTof(self):
        # Reset both Tof and Blobs
        self.refreshTof()
        self.makeBlobTrendQueue()

    def refreshTof(self):
        # Reset Tof only
        self._histo_x = None
        self._histo_y = None

    def onUpdateTofConfig(self):
        try:
            start = float(self.event_start.text())*1e-6
            end = float(self.event_end.text())*1e-6
            binning = int(self.bin_size.text())
            maxqueue = int(self.max_queue.text())
        except Exception as e:
            print(str(e))
            traceback.print_exc()
            return
        if start > end:
            self._tof_start = end
            self._tof_end = start
            self.event_start.setText(str(end))
            self.event_end.setText(str(start))
        else:
            self._tof_start = start
            self._tof_end = end

        self._tof_bin = binning
        self._maxqueue = maxqueue
        self.clearTof()

                   
    def _updateTof(self,trigger,tof):
        y,x = np.histogram(tof,np.linspace(self._tof_start,self._tof_end,self._tof_bin,dtype=np.float))        
        mean = np.sum(y)/len(trigger)
        if self._histo_x is None:
            self._histo_x = x
            self._histo_y = y
        else:
            self._histo_y += y
        if self._counts_trend_trigger:        
            next_index = self._counts_trend_trigger[-1]+1
        else:
            next_index = 0
        self.updateTrend(next_index,mean)

    def updateTrend(self,trigger,avg_blobs):
        self._counts_trend.append(avg_blobs)
        self._counts_trend_trigger.append(trigger)


    def displayTof(self):       
        self._tof_data.setData(x=self._histo_x,y=self._histo_y, stepMode="center", fillLevel=0, brush=(0,0,255,150))
        self._yield_data.setData(x=self._counts_trend_trigger,y=self._counts_trend, fillLevel=None, brush=(0,0,255,150))

    def onEvent(self,event):
        tof = event['time']*1e-9
        counter = event['ms_indices']-event['ms_indices'][0]
        self._updateTof(counter,tof)

    def setupTofConfig(self):
        self.event_start.setValidator(QtGui.QDoubleValidator(self))
        self.event_end.setValidator(QtGui.QDoubleValidator(self))
        self.bin_size.setValidator(QtGui.QIntValidator(self))
        self.max_queue.setValidator(QtGui.QIntValidator(self))        
        self.event_start.setText(str(self._tof_start))
        self.event_end.setText(str(self._tof_end))
        self.max_queue.setText(str(self._maxqueue ))
        self.bin_size.setText(str(self._tof_bin))
        self.onUpdateTofConfig()

def main():
    import sys
    app = QApplication([])
    tof = TimeOfFlightPanel()
    tof.show()

    app.exec_()
if __name__=="__main__":
    main()