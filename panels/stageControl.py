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
from utils.parsedelays import parseStringInput
from utils.Stage.basestage import Stage
from utils.makeConversionFactor import makeConversionFactor
# from utils.Stage.Smaract.smaract import SmarAct
# from ui.stageControl_ui import Ui_stageControl
# from ui.settingsDialogUI import Ui_SettingsDialog
# from .settingsDialog import SettingsDialog
import logging
import threading
from threading import Thread
import time
from panels.activeStabilisation import PIDModule
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
    signal_stagePositionReady = QtCore.Signal(bool)
    #Send position array
    signal_stagepositionarray = QtCore.Signal(object)
    #Update GUI
    signal_updateGUI = QtCore.Signal(object)


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
        self._stage = Stage()
        self._pid = None
        self.ui.offset_spinBox.setSuffix(self._stage.units)
        # self._stage = SmarAct()
        # self._stage.enable()
        self.updateConversionFactor()        
        self.tolerance = 10
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.blink)


        # Tof panel used for display


    def initializeStage(self):
        if self._stage is None:
            print("Initializing chosen stage")
            current_pos = self._stage.get_pos()
            self.ui.targetAbsolute_spinBox.blockSignals(True)
            self.ui.targetRelative_spinBox.blockSignals(True)
            self.ui.offset_spinBox.blockSignals(True)
            self.ui.targetAbsolute_spinBox.setValue(current_pos)
            self.ui.targetRelative_spinBox.setValue(0)
            self.ui.offset_spinBox.setValue(current_pos)   
            self.ui.offset_spinBox.blockSignals(False)
            self.ui.targetAbsolute_spinBox.blockSignals(False)
            self.ui.targetRelative_spinBox.blockSignals(False)
        else:
            print("Deinitialize previously chosen stage first")
    def deinitializeStage(self):
        if self._stage is not None:
            print("Deinitializing chosen stage")
        else:
            print("No stage initialized")    

    #Launch function when buttons are pressed
    def connectSignals(self):
        self.ui.cBox_stageSelection.currentIndexChanged.connect(self.stageSelection_changed)
        self.ui.targetAbsolute_spinBox.valueChanged.connect(lambda x:self.run_movingstage(x,False))
        self.ui.targetRelative_spinBox.valueChanged.connect(lambda x:self.run_movingstage(x,True))
        self.ui.offset_spinBox.valueChanged.connect(self.updateRelativePosition)
        self.ui.cBox_stageMode.currentIndexChanged.connect(self.updateConversionFactor)
        self.ui.stop_pushButton.pressed.connect(self.stopStage_button)
        self.signal_stagepositionupdated.connect(self.updatePosition)
        self.signal_stagepositionfixed.connect(self.stage_in_motion)      
        self.ui.activeStab_pushButton.pressed.connect(self.launchActiveStab)

    def launchActiveStab(self,):            
        if self.ui.activeStab_pushButton.isChecked():            
            self._pid.hide()
        else:
            if self._pid is None:
                self._pid = PIDModule()
                self.connectPIDsignals()
            self._pid.show()
            self._pid.start()

    def connectPIDsignals(self,):
        self._pid.ui.stabilize_pushButton.pressed.connect(self.switchMode)
        self._pid.ouputPID_signal.connect(self.setPosition)

    def switchMode(self,):
        if self._pid.ui.stabilize_pushButton.isChecked():
            self.ui.targetAbsolute_spinBox.setEnabled(True)
            self.ui.targetRelative_spinBox.setEnabled(True)
            # self.run_stageContinuously()

        else:
            self.ui.targetAbsolute_spinBox.setEnabled(False)
            self.ui.targetRelative_spinBox.setEnabled(False)



    # def run_stageContinuously(self,):
    #     if self._moving_stage_thread is not None:
    #             self._moving_stage_thread.cancel()
    #             self._moving_stage_thread = None
    #     self._in_motion = True        
    #     self.signal_stagepositionfixed.emit(True)    
    #     self._moving_stage_thread = BasicThread(self.moveStageContinuuously,)           
    #     self._moving_stage_thread.start()

    # def moveStageContinuuously(self,):
    #     while self._pid.ui.stabilize_pushButton.isChecked():
    #         self._stage.move_to_pos(pos=self.destination)      
    #         print(self.destination)  
    #     self.end_movingstage()
    
    def setPosition(self,position):
        # self.destination = position
        if self._pid.ui.stabilize_pushButton.isChecked():
            self._stage.move_to_pos(pos = position)  
            
            self.signal_stagePositionReady.emit(True)
            print(position)




    def updateRelativePosition(self,position):
        a = 0
        # old_position = self.ui.currentRelative_lineEdit.text()        
        # if not old_position:
        #     old_position = 0
        # else:
        #     old_position = float(old_position)
        # relative_position = position-old_position           
        # self.ui.targetRelative_spinBox.blockSignals(True)
        # self.ui.targetRelative_spinBox.setValue(relative_position)
        # self.ui.targetRelative_spinBox.blockSignals(False)
        # self.ui.currentRelative_lineEdit.setText(str(relative_position))
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
            self.ui.stop_pushButton.setText(f'MOVING (press to stop)')
            self.ui.stop_pushButton.setEnabled(True)
            self.timer.start(500)
        else:
            self.timer.stop()
            self.ui.stop_pushButton.setText(f'FIXED')
            self.ui.stop_pushButton.setEnabled(False)
    def blink(self):
        print('Blinking')            
    # def openSettingsDialog(self):
    #     dialog = SettingsDialog()
    #     dialog.signal_applyStageSerialPort.connect(self.set_stageCOMPort)
    #     return

    def updatePosition(self,position):
        self.ui.currentAbsolute_lineEdit.setText(str(position))
        position/=self.getConversionFactor()
        position = np.round(position,5)
        relative_position = position-self.ui.offset_spinBox.value()
        relative_position /= self.getConversionFactor()
        relative_position = np.round(relative_position,5)
        self.ui.currentRelative_lineEdit.setText(str(relative_position))

    def updateConversionFactor(self,):     
        # In
        if self.ui.cBox_stageMode.currentIndex():
            self.ui.conversionFactor_lineEdit.setEnabled(False)
            self.ui.conversionFactor_lineEdit.setText(str(self.getConversionFactor()))
        else:
            self.ui.conversionFactor_lineEdit.setEnabled(True)      

    def getConversionFactor(self,):
        # Return conversion factor from GUI units to stage units
        return float(makeConversionFactor(self.getCurrentUnits(),self._stage.units))

    def getCurrentUnits(self):
        # Get current units from GUI
        units = re.findall('(?<=\[)[^][]*(?=])',self.ui.cBox_stageMode.currentText())
        if units:
            units = units[0]
        else:
            units = self._stage.units
        return units

    def receivePositionCommand(self,destination):
        if self._pid is not None: 
            if self._pid.ui.stabilize_pushButton.isChecked():
                self._pid.ui.objective_PID_spinBox.setValue(destination)
        else:
            self.run_movingstage(destination)


    #Function that take care of the motion of the stage
    def moveStage(self,destination,):
        #Initial postion
        initialpos = self._stage.get_pos()   
        lastpos = initialpos 
        self.signal_stagepositionupdated.emit(lastpos)
        #Moving command            
        self._stage.move_to_pos(pos=destination)        
        #Checking stage motion and updating current position
        while abs(destination-lastpos)>self.tolerance and self._in_motion:
            try:
                time.sleep(0.1)
                lastpos = self._stage.get_pos()   
                print(lastpos)
                self.signal_stagepositionupdated.emit(lastpos)
                self.updatePosition(lastpos)
                print(round(100 * (lastpos-initialpos)/(destination-initialpos)))
            except Exception as e:
                logging.error(str(e))
                return                
        #Checking final position
        else: 
            print('Finished')
        self.end_movingstage()
 
    #Function that reacts to the stop button            
    def stopStage_button(self):  
        self.end_movingstage()
        self._stage.stop_motion()


     #Command that launch the move stage thread
    @QtCore.Slot(float)         
    def run_movingstage(self,destination,isRelative=False):
        destination*=self.getConversionFactor()
        if isRelative:
            destination += self.ui.offset_spinBox.value()
        if self._moving_stage_thread is not None:
                self._moving_stage_thread.cancel()
                self._moving_stage_thread = None
        self._in_motion = True        
        self.signal_stagepositionfixed.emit(False)    
        self._moving_stage_thread = BasicThread(self.moveStage,(destination,))           
        self._moving_stage_thread.start()

    #Command that kills the move stage thread
    def end_movingstage(self): 
        if self._moving_stage_thread is not None:
            self._moving_stage_thread.cancel()
            self._in_motion = False
            self._moving_stage_thread = None
            self.signal_stagepositionfixed.emit(True)       



    def closeEvent(self, event: QtGui.QCloseEvent) -> None:    
        self._stage.end_movingstage()
        self._stage.close_communication()
        self._pid.close()
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
