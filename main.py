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
#

# -----------------------------------------------------------------------------
# example 4 of deriving from buffered_data_callbacks_pipe

NR_OF_MEASUREMENTS = 2    # number of measurements
EXPOSURE_MS = 100         # exposure duration in milliseconds
OUTPUT_TEXTFILE_NAME = "tmp_textfile1357.txt" # this file will be overwritten!

# define some constants to distinguish the type of element placed in the queue
QUEUE_DATA = 0
QUEUE_ENDOFMEAS = 1


def initializeDevice(libpath=None):
    import os
    if libpath:
        folder_init = os.getcwd()
        os.chdir(libpath)
    else:
        print('No library path given')
        return -1
    device = scTDC.Device(autoinit=False)
    # initialize TDC --- and check for error!
    retcode, errmsg = device.initialize()
    if retcode < 0:
        print("error during init:", retcode, errmsg)
        return -1
    else:
        print("successfully initialized")
    os.chdir(folder_init)
    return device



def test5():

    device = initializeDevice("C:\\Users\\attose1_VMI\\Documents\\Python_Scripts\\scTDC\\scTDC_Python_SDK_v1.3.0\\scTDC_Py\\Library\\")    

    # open a BUFFERED_DATA_CALLBACKS pipe
    bufdatacb = BufDataCB5(device.lib, device.dev_desc)

    # define a closure that checks return codes for errors and does clean up
    def errorcheck(retcode):
        if retcode < 0:
            print(device.lib.sc_get_err_msg(retcode))
            bufdatacb.close()
            device.deinitialize()
            return -1
        else:
            return 0

    start = timeit.default_timer()

    # start a first measurement
    retcode = bufdatacb.start_measurement(EXPOSURE_MS)
    if errorcheck(retcode) < 0:
        return -1

    # enter a scope where the text file is open
    with DataToTextfile(OUTPUT_TEXTFILE_NAME) as data_to_textfile:
        # event loop
        meas_remaining = NR_OF_MEASUREMENTS
        while True:
            eventtype, data = bufdatacb.queue.get()  # waits until element available
            if eventtype == QUEUE_DATA:
                data_to_textfile.process_data(data)
            elif eventtype == QUEUE_ENDOFMEAS:
                data_to_textfile.write_measurement_separator()
                meas_remaining -= 1
                if meas_remaining > 0:
                    retcode = bufdatacb.start_measurement(EXPOSURE_MS)
                    if errorcheck(retcode) < 0:
                        return -1
                else:
                    break
            else: # unknown event
                break # break out of the event loop

    end = timeit.default_timer()
    print("\ntime elapsed : ", end-start, "s")

    time.sleep(0.1)
    # clean up
    bufdatacb.close() # closes the user callbacks pipe, method inherited from base class
    device.deinitialize()

    return 0

if __name__ == "__main__":
    test5()
