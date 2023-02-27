import sys
import re
import numpy as np
from PySide6 import QtWidgets,QtCore,QtGui

# Import to make the panel work in the pymepixviwer package.
# from .Stage import Stage
# from .ThorlabsAPTStage import ThorlabsAPTStage
# from .ui.delays_ui import Ui_stageControl
# from .ui.settingsDialogUI import Ui_SettingsDialog
from .ui.stageControl_ui import Ui_stageControl
from utils.Stage.Smaract.smaract import SmarAct
# from ui.stageControl_ui import Ui_stageControl
# from ui.settingsDialogUI import Ui_SettingsDialog
# from .settingsDialog import SettingsDialog
import logging
import threading
from threading import Thread
import time
# from .core.threading import BasicThread
class BasicThread(Thread):
    """Call a function after a specified number of seconds:

            t = Timer(30.0, f, args=[], kwargs={})
            t.start()
            t.cancel()     # stop the timer's action if it's still waiting
    """
    def __init__(self, function, args=[], kwargs={}):
        Thread.__init__(self)        
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = threading.Event()

    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.finished.set()

    def run(self):        
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
        self.finished.set()
# This class defines the functionality of the stage control widget. The UI is defined in the class Ui_stageControl,
# in the file delaysUI.py.s
# The delaysUI.py, is directly generated from the DelaysUI.ui file, which is the output of the QT-designer tool, and can
# be edited in that tool. Running pyqtc DelaysUI.ui -o delaysUI.py will generate the python code from the UI file.
# The stagecontrol class is a subclass of QWidget

class StageControl(QtWidgets.QWidget):
    #Signal for updating GUI
    signal_stagepositionupdated = QtCore.Signal(float)
    #Send true if stage is moving
    signal_stagepositionfixed = QtCore.Signal(bool)
    #Send position array
    signal_stagepositionarray = QtCore.Signal(object)

    # Initialize the widget. It won't show up on screen after this.
    def __init__(self,parent):
        ## Initialization ##
        # First class the parent class (QWidget) constructor.
        QtWidgets.QWidget.__init__(self)
        # Set the ui to be the one defined in the Ui_stageControl class
        self.ui = Ui_stageControl()
        # Call the setupUi method to add the right Ui elements.
        self.ui.setupUi(self)
        self._moving_stage_thread = None
        self.connectSignals()
        # Initialize the abstract stage that does nothing:
        # self._stage = Stage()
        self._stage = SmarAct()
        self._stage.enable()

        # Array to contain the positions to run though
        self._stagePositions = np.asarray([])
        # The index of currently set stage delay
        self.currentDelayIdx = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.blink)
        self.setupPlotWindows()

    def setupPlotWindows(self):
            # Initialize the plot of the stage delays:
        self.ui.plot_delays.setLabel('left','Postion')
        self.ui.plot_delays.setLabel('bottom','Steps ')#   
        self.ui.plot_delays.showGrid(x=True,y=True)
        # Initialize the done/undone plot that will show current progress:
        self.delaysPlot = self.ui.plot_delays.plot(self._stagePositions)        
        self.delaysPlot_done = self.ui.plot_delays.plot(self._stagePositions, fillLevel=0.0, brush=(50,50,200,200))

    def initializeStage(self):
        if self._stage is None:
            print("Initializing chosen stage")
        else:
            print("Deinitialize previously chosen stage first")
    def deinitializeStage(self):
        if self._stage is not None:
            print("Deinitializing chosen stage")
        else:
            print("No stage initialized")    

    #Launch function when buttons are pressed
    def connectSignals(self):
        self.ui.move_pushButton.clicked.connect(self.moveStage_button)
        self.ui.stop_pushButton.clicked.connect(self.stopStage_button)
        # You can also pass paramaters from signals to slots. This will be evident later in the code.
        # self.ui.pushButton_stageSettings.clicked.connect(self.openSettingsDialog)
        # Connect the stageMode combobox to the stageMeode_changed() method.
        self.ui.cBox_stageMode.currentIndexChanged.connect(self.stageMode_changed)
        # Connect the delayInput button being clicked to the parseDelayInput method.
        self.ui.update_pushButton.clicked.connect(self.parseDelayInput)        
        # Connect the stage selection combobox to the 
        self.ui.cBox_stageSelection.currentIndexChanged.connect(self.stageSelection_changed)
        self.ui.textEdit_delayInput.blockCountChanged.connect(self.parseDelayInput)
        self.ui.delayScheme_comboBox.currentIndexChanged.connect(self.parseDelayInput)
        self.ui.absoluteMotion_radioButton.toggled.connect(self.parseDelayInput)




    @QtCore.Slot()
    def stageSelection_changed(self):
        if self.ui.cBox_stageSelection.currentIndex() == 0:

            self._stage = self._NewportStage
        elif self.ui.cBox_stageSelection.currentIndex() == 1:
            self._stage = self._thorlabsStage
        else:
            print(f"current index of cBox_stageSelection: {self.ui.cBox_stageSelection.currentIndex} not recongnized")


    # Slot that is called when the stageMode combobox is changed. Doesn't really do anything yet, other than update some
    # text, and update the delays in a way that is for now completely unused.
    # (This @QtCore.pyqtSlot() declaration is not necessary, but nice to have to remember what it is, and will help the
    # IDE to catch some errors you might program.)
    @QtCore.Slot()
    def stage_in_motion(self):
        if self._in_motion:
            self.ui.stage_position_status.setText(f'MOVING')  
            self.timer.start(500)
        else:
            self.timer.stop()
            self.ui.stage_position_status.setText(f'FIXED')     
    def blink(self):
        print('Blinking')
    @QtCore.Slot()
    def stageMode_changed(self):
        # The options in the combobox is for now hard coded. This is not the best practice, but is pretty easy
        # to implement
        currentIndex = self.ui.cBox_stageMode.currentIndex()
        # if currentIndex == 0:
        #     self.ui.label_delayInput.setText("Delay Input [mm]")
        # elif currentIndex == 1 or currentIndex == 2:
        #     self.ui.label_delayInput.setText("Delay Input [ps]")
        # elif currentIndex == 3 or currentIndex == 4:
        #     self.ui.label_delayInput.setText("Delay Input [fs]")
        self.updateDelaysPlot()
        self.parseDelayInput()

    # This will take a signal from the daq config that gives 3 arrays as parameters, this is the reason for the wierd
    # signature:
    @QtCore.Slot(object, object, object)
    def update_currentDelayIndex(self, positions, indexes, steps):
        if(steps[0] != self.currentDelayIdx):
            self.currentDelayIdx = steps[0]
            self.updateDelaysPlot()
        return

    # Method to updagte the delays plot
    def updateDelaysPlot(self):
        stageDelay_indices = np.arange(0, np.size(self._stagePositions))
        # Plot with fill until the current index:
        self.delaysPlot_done.setData(stageDelay_indices[:self.currentDelayIdx], self._stagePositions[:self.currentDelayIdx])
        # Plot without fill after the current delay index:
        self.delaysPlot.setData(stageDelay_indices[self.currentDelayIdx:], self._stagePositions[self.currentDelayIdx:])
        return


    # def openSettingsDialog(self):
    #     dialog = SettingsDialog()
    #     dialog.signal_applyStageSerialPort.connect(self.set_stageCOMPort)
    #     return


    # This slot takes a parameter! Specifically here declared to be a string.
    # A signal that is emitted to it must then contain a string as a parameter.

    # Parses the delay input to an numpy array that contains all the stage delay values.
    # The syntax goes like this, expanding a little bit on what is used in the "frame_ultimate.vi" program:
    # A range: "start:step:stop" gives an array that goes from start to stop in steps of step.
    # A series: "range_a, range_b" (or "x:y:z, a:b:c") gives two ranges that are concatenated together to one array.
    #           Any number of ranges sperated by commas and/or whitespace (including return) is a series.
    #           Everything is a series will be sorted together, if sorting is used.
    # All_delays: "series_a;series_b" is multiple series seperated by a semicolon.
    #           Different series are NOT sorted together.
    # Note that this method is too long for good coding practice and should probably be put into it's own class.
    def parseDelayInput(self):
        class DelayParseException(Exception):
            def __init__(self, message):
                Exception.__init__(self, message)

        # Take the delay input string directly from the Delay Input textbox
        delayInput = self.ui.textEdit_delayInput.toPlainText()
        all_delays = np.asarray([])
        # First check for paranthesis enclosed ranges:
        measurement_strings = re.findall("(\(?[-\d.,;:\s]+\)?(?:\*\d+)?)", delayInput)


        # print(f"delayInput: {delayInput}")
        # print(f"meansurement_strings: {measurement_strings}")

        for measurement_string in measurement_strings:
            # Measurement string should always have either 1 or 2 substrings, depending

            substrings = re.findall("[-\d.,;:\s]+", measurement_string)
            # print(f"substrings: {substrings}")
            # print(f"len(substrings): {len(substrings)}")
            multiplier = 1
            if len(substrings) == 2:
                multiplier = int(substrings[1])
            elif len(substrings) == 1:
                multiplier = 1
            else:
                raise DelayParseException(f"Unable to make out a measurement and multiplier for this string: {measurement_string}, which gives {len(substrings)} substrings")
            # print(multiplier)
            measurement_delays = np.asarray([])

            # Split the string on ; first.
            series_strings = re.findall("[^;]+", substrings[0])
            # Now do something for each string that defines a series:
            for series_string in series_strings:
                # Then split on , or any whitespace to find the range specifiers: "?:?:?"
                range_strings = re.findall("[^,\s]+", series_string)
                # print(f"range strings: {range_strings}")

                series = np.asarray([])
                for range_string in range_strings:
                    # Extract the numbers by splitting on :.
                    number_strings = re.findall("[^:]+", range_string)
                    # If the range specifier is not either 1 or 3 string representations of numebers, the input is invalid:
                    # 3 Numbers specify a range
                    if len(number_strings) == 3:
                        start = float(number_strings[0])
                        step = float(number_strings[1])
                        stop = float(number_strings[2])
                        numberofsteps = abs(round(1.0 + abs((stop - start)/step)))
                        
                        this_range = np.linspace(start,stop,int(numberofsteps))
                        # print(f"this_range: {this_range}")
                        # range = np.arange(start, stop, step)
                        # range = np.append(range,stop)
                    # 1 number just specifies a single number
                    elif len(number_strings) == 1:
                        this_range = np.asarray([float(number_strings[0])])
                    else:
                        raise DelayParseException(
                            f"Error! Following substring does not lead to either 1 or 3 numbers: {range_string}")

                    # Add all of the series to the range:
                    series = np.concatenate((series, this_range))
                    # print(f"series: {series}")

                # Now the series is complete, and must be sorted according to the option the user has chosen:
                delayScheme_index = self.ui.delayScheme_comboBox.currentIndex()

                # 0: No sorting:

                # 1: Sort up
                if delayScheme_index == 1:
                    series = np.sort(series)

                # 2: Sort down
                elif delayScheme_index == 2:
                    series = series[np.argsort(-series)]

                # Staggered Acending
                elif delayScheme_index == 3:
                    series = np.sort(series)
                    firstHalf = series[0::2]
                    secondHalf = series[1::2]
                    # Reverse the second half to get staggered ascending:
                    secondHalf = secondHalf[::-1]
                    series = np.concatenate((firstHalf, secondHalf))

                # Staggered decending
                elif delayScheme_index == 4:
                    series = series[np.argsort(series)]
                    firstHalf = series[0::2]
                    secondHalf = series[1::2]
                    # Reverse the first half to get staggered decending:
                    firstHalf = firstHalf[::-1]
                    series = np.concatenate((firstHalf, secondHalf))

                # Concatenate together all the delays
                measurement_delays = np.concatenate((measurement_delays, series))

            # Repeat according to the multiplier, and add to all_delays
            all_delays = np.concatenate((all_delays, np.tile(measurement_delays, multiplier)))

        currentDelayIdx = self.ui.cBox_stageMode.currentIndex()

        #print(f"all delays: {all_delays}")

        if currentDelayIdx > 0:            
            all_delays = self.ConvertTimeInDistance(all_delays,self.ui.offset_spinBox.value(), self.relateDelayIdx_to_NumberofPass(currentDelayIdx))
        # Save the delays as a field parameter
        self._stagePositions = all_delays.round(5)
        # Send position array as a signal
        self.signal_stagepositionarray.emit(self._stagePositions)
        # Update the delays plot
        self.updateDelaysPlot()


    def relateDelayIdx_to_NumberofPass(self,index):
        numberofpass = 1
        if index == 1:
            numberofpass = 1
        elif index == 2:
            numberofpass = 2
        elif index == 3:
            numberofpass = 1
        elif index == 4: 
            numberofpass = 2
        return numberofpass

    def relateDelayIndex_to_speedOfLight(self,index):
        c__in_mm_per_timeUnit = 1
        # index 0 is "mm"
        
        # index 1 and 2 are ps
        if index == 1 or index == 2:
            c_in_mm_per_timeUnit = 0.299792458/1.00026905462751
        # Index 3 and 4 are fs:
        elif index == 3 or index == 4:
            c_in_mm_per_timeUnit = 0.299792458/1.00026905462751 * 1e-3
        return

    #Function that reacts to the move button   
    def moveStage_button(self):   
        self.parseDelayInput()        
        try:
            self.run_movingstage(self._stagePositions[0])
        except Exception as e:
            print('Cannot read array, check input')
            return
    #Function that reacts to the stop button            
    def stopStage_button(self):  
        self.end_movingstage()
        print('Reached killing of thread')
        self._stage.stop_motion()
        # try:
            # self.ui.status_position.setText(f'{self._stage.get_pos()}')  
        # except Exception as e:
        #     logging.error(str(e))
        #     return
        if self._moving_stage_thread is not None:
            self._moving_stage_thread.cancel()
            self._moving_stage_thread = None         
    #Function that take care of the motion of the stage
    def moveStage(self,destination,numberoftry = 0):
        #Checking motor status
        if not self._stage.check_no_error:
            self._stage.enable()

        #Initial postion
        initialpos = self._stage.get_pos()   
        lastpos = initialpos 
        self.signal_stagepositionupdated.emit(lastpos)

        #Moving command            
        self._stage.move_to_pos(pos=destination)        
        #Checking stage motion and updating current position
        while abs(destination-lastpos)>self._stage.errorPosition and self._in_motion:
            try:
                time.sleep(0.1)
                lastpos = self._stage.get_pos()   
                print(lastpos)
                self.signal_stagepositionupdated.emit(lastpos)
                # self.status_position.setText(f'{lastpos}')
                print(round(100 * (lastpos-initialpos)/(destination-initialpos)))
                # self.motion_progressBar.setValue(round(100 * (lastpos-initialpos)/destination))
            except Exception as e:
                logging.error(str(e))
                return                
        #Checking final position
        # if abs(lastpos - destination) > 0.01:            
            # print(f'Crashed at {lastpos}mm\nNumber of try is {numberoftry}')
            # if numberoftry < 5:
                # self._stage.enable()
                # self.moveStage(destination,numberoftry + 1)                
            # else:
                # print('Stage failed to reached destination')
        else: 
            print('Finished')
            self.end_movingstage()
 
     #Function to convert time input in distance as a function of the number of pass
    def ConvertTimeInDistance(self,time_delays,t0_in_mm,numberofpass):
        #speedoflight_in_mmperps = 0.299792458/1.00026905462751; # value for 800 nm in our lab %1.000348;
        # Time unit is either ps or fs. This relates the index of the stageMode cBox to the right value:
        c_in_mm_per_timeUnit = self.relateDelayIndex_to_speedOfLight(self.ui.cBox_stageMode.currentIndex())

        return (time_delays*c_in_mm_per_timeUnit/(2*numberofpass))+t0_in_mm

     #Command that launch the move stage thread
    @QtCore.Slot(float)     
    def run_movingstage(self,destination):
        if self._moving_stage_thread is not None:
                self._moving_stage_thread.cancel()
                self._moving_stage_thread = None
        self._in_motion = True        
        self.signal_stagepositionfixed.emit(True)    
        self._moving_stage_thread = BasicThread(self.moveStage,(destination,))           
        self._moving_stage_thread.start()

    #Command that kills the move stage thread
    def end_movingstage(self):        
        self._moving_stage_thread.cancel()
        self._in_motion = False
        self.signal_stagepositionfixed.emit(False)       


    def closeEvent(self, event: QtGui.QCloseEvent) -> None:    
        self._stage.end_movingstage()
        self._stage.close_communication()
        return super().closeEvent(event)

def main():
    import sys
    import logging
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    app = QtWidgets.QApplication([])    
    config = StageControl()
    app.lastWindowClosed.connect(config.deinitializeStage)
    config.show()
    
    app.exec_()
if __name__=="__main__":
    main()
# # # Start up the application. This seems to be the background basis for any QT UI
# app = QtWidgets.QApplication(sys.argv)

# # Make a window in the application. This window is our StageControl class.
# window = StageControl()

# # Show the window
# window.show()

# # I'm not 100% sure what this does, but if think it defines what should happen when you press the little exit button
# # that is in every window.
# sys.exit(app.exec_())
