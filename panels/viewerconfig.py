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
from .ui.viewerconfig_ui import Ui_Form
import logging

logger = logging.getLogger(__name__)


class ViewerConfig(QWidget,Ui_Form):
    resetPlots = Signal()
    updateRateChange = Signal(float)
    frameTimeChange = Signal(float)
    
    def __init__(self,parent=None):
        super(ViewerConfig, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setupUi(self)  
        self.setupLines()
        self.connectSignals()

    def setupLines(self):
        self.frame_time.setValidator(QtGui.QDoubleValidator(self))

    def connectSignals(self):
        self.display_rate.valueChanged.connect(self.displayRateChange)
        self.frame_time.returnPressed.connect(self.frameTimeChanged)
        self.reset_plots.clicked.connect(self.resetPlots.emit)

    def displayRateChange(self,value):
        seconds = 1.0/value
        self.updateRateChange.emit(seconds)
    
    # def eventCountChanged(self):
    #     self.eventCountChange.emit(int(self.event_count.text()))
    
    def frameTimeChanged(self):
        frame_time = float(self.frame_time.text())
        if self.time_multi.currentText() == "s":
            frame_time*=1
        elif self.time_multi.currentText()=="ms":
            frame_time*=1E-3        
        logger.info('Frame time changed to {} s'.format(frame_time))
        self.frameTimeChange.emit(frame_time)    