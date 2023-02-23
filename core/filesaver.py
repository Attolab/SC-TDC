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

from PySide6 import QtCore
# from pyqtgraph.Qt import QtCore, QtGui
from utils.storage import store_tof,open_output_file
import numpy as np
import logging

logger = logging.getLogger(__name__)


class FileSaver(QtCore.QThread):

    def __init__(self):
        QtCore.QThread.__init__(self)
        self._tof_file = None
        self._log_file= None
        self._index = 0


    def openFiles(self,filename,index,tof=1,log=1):
        self._index = index
        if tof: 
            self.openTof(filename)
        if log:
            self.openLog(filename)

    def openLog(self,filename):
        if self._log_file is not None:
            self._log_file.close()
        logger.info('Opening Log file :{}'.format(filename))
        file_format = '{}.{}'           
        self._log_file = open(file_format.format(filename,'log'),'a',newline = '')

    def openTof(self,filename):
        if self._tof_file is not None:
            self._tof_file.close()
        logger.info('Opening tof file :{}'.format(filename))
        self._tof_file = open_output_file(filename,'tof',index=self._index)
    
    def setIndex(self,index):
        self._index = index

    def onTof(self,data):
        if self._tof_file is not None:
            store_tof(self._tof_file,data)  

    def writeLog(self,filename,index,acq_time,pos,exposure_time,):
        import csv, os
        file_format = '{}.{}'           
        filename = file_format.format(filename,'log')
        print(filename)
        if self._log_file is not None and not self._log_file.closed:
            spamwriter = csv.writer(self._log_file,delimiter = '\t')
            if os.stat(filename).st_size == 0:
                print('file is empty')
                spamwriter.writerow(['Index',  'Acquisition Time (s)','Position','Exposure time (ms)',] )
        spamwriter.writerow([index,acq_time, pos,exposure_time,])

    def closeFiles(self):
        if self._tof_file is not None:
            logger.info('Closing tof file')
            self._tof_file.close()
            self._tof_file = None

    def closeLogFile(self):
        if self._log_file is not None:
            logger.info('Closing log file')
            self._log_file.close()
            self._log_file = None                

    # def find_index(self,filename,index,ext):
    #     file_format = '{}_{:06d}.{}'           
    #     raw_filename = file_format.format(filename,index,ext)
    #     while os.path.isfile(raw_filename):
    #         index+=1
    #         raw_filename = file_format.format(filename,index,ext) 
    #     return index
    # def check_index(self,filename,index):
    #     ext = ('raw','toa','tof','blob')
    #     for e in ext:
    #         index_temp = self.find_index(filename,0,e)
    #         index = max(index_temp,index)
    #     return index        