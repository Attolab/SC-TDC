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
import threading
from PySide6.QtCore import Signal
import numpy as np
#

# -----------------------------------------------------------------------------
# example 4 of deriving from buffered_data_callbacks_pipe

NR_OF_MEASUREMENTS = 2    # number of measurements
EXPOSURE_MS = 100         # exposure duration in milliseconds
OUTPUT_TEXTFILE_NAME = "tmp_textfile1357.txt" # this file will be overwritten!
# define some constants to distinguish the type of element placed in the queue
QUEUE_DATA = 0
QUEUE_ENDOFMEAS = 1

class AcquisitionThread(threading.Thread):
    """Call a function after a specified number of seconds:

            t = Timer(30.0, f, args=[], kwargs={})
            t.start()
            t.cancel()     # stop the timer's action if it's still waiting

    """
    def __init__(self, function, args=[], kwargs={}):
        threading.Thread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = threading.Event()
    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.finished.set()

    def run(self):
        repeats = 0
        while not self.finished.is_set():
            print(repeats)
            repeats += 1
            # print('launching acq')
            self.function(*self.args, **self.kwargs)
            # print('finishing acq')
        # self.finished.set()


class SC_TDC(object,):
    # clearNow = Signal()
    # _dataSignal = Signal(object)

    def __init__(self,parent=None,adress="C:\\Users\\attose1_VMI\\Documents\\Python_Scripts\\scTDC\\scTDC_Python_SDK_v1.3.0\\scTDC_Py\\Library\\"
                ,exposureTime=100):
        # super(SC_TDC, self).__init__(parent)
        # self.setupUi(self)    
        self.libpath = adress+"tdc_gpx3.ini"
        # Initialize device
        try:
            self.device = self.initializeDevice()        
            # open a BUFFERED_DATA_CALLBACKS pipe
            self.bufdatacb = BufDataCB5(self.device.lib, self.device.dev_desc)
        except:
            self.device = None
            self.bufdatacb = None
        self._event_callback=None
        self.exposureTime = exposureTime
        self._data_thread = None
        # self.start_thread(exposureTime=self.exposureTime)
        
        # self._data_thread = threading.Thread(target=self.data_thread)
        # self._data_thread.start()
        # self.bufdatacb.dataCallback = self.onData


    def getData(self,exposureTime):
        if self.device is not None:
            retcode = self.bufdatacb.start_measurement(exposureTime) # Starting measurements
            self.errorcheck(retcode) # Checking error
            while True:
                eventtype, data = self.bufdatacb.queue.get()  # waits until element available
                # print(f'eventtype = {eventtype}')
                # print(f'data = {data}')
                if data is None:
                    break       
        else:
            time.sleep(exposureTime*1e-3)
            L = 1000
            eventtype,data = (0,(np.arange(L),np.random.rand(L)))
            # self._dataSignal.emit()     
        # data_type,data = value
        self._event_callback(eventtype,data)

    def stop_thread(self,):    
        print('Stopping thread:')
        if self._data_thread is not None:
            self._data_thread.cancel()
            self._data_thread = None
            print('Thread is stopped')
        else:
            print('No active thread to be stopped')
    def start_thread(self,):  
        print('Starting thread:')  
        if self._data_thread is not None:
            self._data_thread.cancel()
            self._data_thread = None
        self._data_thread = AcquisitionThread(self.getData,(self.exposureTime,))
        self._data_thread.start()
        print('Thread is started')  


    def initializeDevice(self,):        
        import os
        folder,filename_withext = os.path.split(self.libpath)
        if self.libpath:
            folder_init = os.getcwd()
            os.chdir(folder)
        else:
            print('No library path given')
            return -1
        device = scTDC.Device(inifilepath=self.libpath,autoinit=False)
        # initialize TDC --- and check for error!
        retcode, errmsg = device.initialize()
        if retcode < 0:
            print("error during init:", retcode, errmsg)
            return -1
        else:
            print("successfully initialized")
        os.chdir(folder_init)
        return device     

    @property
    def exposureTime(self):
        """Exposure time in volts"""
        return self._exposure_time
    
    @exposureTime.setter
    def exposureTime(self,value):
        self._exposure_time = value


    @property
    def dataCallback(self):
        """Function to call when data is recieved from a timepix device
        This has the effect of disabling polling. 
        """
        return self._event_callback
    @dataCallback.setter
    def dataCallback(self,value):
        self._event_callback = value

    # define a closure that checks return codes for errors and does clean up
    def errorcheck(self,retcode):
        if retcode < 0:
            print(self.device.lib.sc_get_err_msg(retcode))
            self.closeDevice()
            return -1
        else:
            return 0        
    def closePipe(self):
        if self._data_thread is not None:
            self.stop_thread()
        if self.bufdatacb is not None:
            self.bufdatacb.close() # closes the user callbacks pipe, method inherited from base class
        self.bufdatacb = None           
        print('Pipe is closed')        

    def openPipe(self,):
        if self.device is not None:
            self.bufdatacb = BufDataCB5(self.device.lib, self.device.dev_desc)
            print('Pipe is created')
        else:
            self.bufdatacb = None
            print('Pipe is not created')
    def closeDevice(self):
        # clean up
        self.closePipe() # Closing pipe        
        self.device.deinitialize() # Deinitialize device

    def resetDevice(self):
        self.closeDevice()
        self.initializeDevice()
        self.openPipe()
        # clean up

def main():
    import sys
    import logging
    import numpy as np
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    config = SC_TDC()
if __name__=="__main__":
    main()