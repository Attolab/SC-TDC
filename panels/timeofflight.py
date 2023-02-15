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
        self._yield = None
        self._tof_data = pg.PlotDataItem()
        self.tof_view.addItem(self._tof_data)
        self.tof_view.setLabel('bottom',text='Time of Flight',units='s')
        self.tof_view.setLabel('left',text='Hits')        
        self._yield_data = pg.PlotDataItem()
        self.yield_view.addItem(self._yield_data)
        self.yield_view.setLabel('bottom',text='Measurement')
        self.yield_view.setLabel('left',text='Hits')
        self._blob_tof_mode = False

        maxlength=1000
        self._counts_trend_y = deque(maxlen=maxlength)#np.ndarray(shape=(400,),dtype=np.float)
        self._counts_trend_x = deque(maxlen=maxlength)        
        self.setupTofConfig()
        self.connectSignals()

        
    def connectSignals(self):
        self.update_config.clicked.connect(self.onUpdateTofConfig)
    def clearTof(self):
        self._histo_x = None
        self._histo_y = None
        self._counts_trend_x = None
        self._counts_trend_y = None
    def resetTof(self):
        self._histo_x = None
        self._histo_y = None


    def onUpdateTofConfig(self):
        try:
            start = float(self.event_start.text())*1e-6
            end = float(self.event_end.text())*1E-6
            binning = int(self.bin_size.text())
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
        self.clearTof()

                   
    def _updateTof(self,tof):
        y,x = np.histogram(tof,np.linspace(self._tof_start,self._tof_end,self._tof_bin,dtype=np.float))
        if self._histo_x is None:
            self._histo_x = x
            self._histo_y = y
            self._counts_trend_y = np.sum(y)
        else:
            self._histo_y += y
            self._yield_data.appendData(np.sum(y))


    def updateTrend(self,trigger,avg_blobs):
        self._counts_trend_x.append(trigger)
        self._counts_trend_y.append(avg_blobs)
            # self._yield_data.appendData(np.sum(y))

    def displayTof(self):
        self._tof_data.setData(x=self._histo_x,y=self._histo_y, stepMode=True, fillLevel=0, brush=(0,0,255,150))
        self._yield_data.setData(x=self._counts_trend_x,y=self._counts_trend_y, stepMode=True, fillLevel=0, brush=(0,0,255,150))



    def onEvent(self,event):
        tof = event[3]
        self._updateTof(tof)

    def setupTofConfig(self):
        self.event_start.setValidator(QtGui.QDoubleValidator(self))
        self.event_end.setValidator(QtGui.QDoubleValidator(self))
        self.bin_size.setValidator(QtGui.QIntValidator(self))
        self.event_start.setText(str(0.0))
        self.event_end.setText(str(100.0))
        self.bin_size.setText(str(1000))

        self._tof_start = 0.0
        self._tof_end = 100.0
        self._tof_bin = 1000

def main():
    import sys
    app = QApplication([])
    tof = TimeOfFlightPanel()
    tof.show()

    app.exec_()
if __name__=="__main__":
    main()