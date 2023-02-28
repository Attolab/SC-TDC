# This is a super class, which only defines the signatures (names and parameters) for a stage, but not actual implementation
# It is probably not the real python way to do it, but this is what Simon learned in his programming courses, so deal with it ;-) 
class Stage:
    def __init__(self):
        self.units = 'mm'
        return

    # Check if the stage currently gives an error code, return True if it doesn't, false if it does
    def check_no_error(self):
        pass

    # Check that the stage is currently in motion, return True if it is, False if it is not
    def check_in_motion(self):
        pass

    # Start moving the stage to the given position
    def move_to_pos(self, pos):
        pass 

    # Return the current position of the stage
    def get_pos(self):
        return 0

    # Moving or not moving?
    def get_motion_status(self):
        pass

    # Enable connection
    def enable(self):
        pass

    # Disable connection
    def disable(self):
        pass
    def stop_motion(self,):
        print('Stopping')

    def check_convergence(self, destination, threshold):
        if abs(self.get_pos() - destination) > threshold:
            return True
        else: 
            return False
    def check_in_motion(self):
        if self.get_motion_status() == 1:
            return False
        else: 
            return True            

    @property
    def units(self):
        """Exposure time in volts"""
        return self._units
    
    @units.setter
    def units(self,value):
        self._units = value