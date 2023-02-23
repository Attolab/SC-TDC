import threading
from threading import Thread


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

class RepeatThread(Thread):

    def __init__(self, n_repeats, function, args=[], kwargs={}):
        Thread.__init__(self)
        self.repeats = n_repeats
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = threading.Event()

    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.finished.set()

    def run(self):
        self._currentrepeat = 0
        while not self.finished.is_set() and self._currentrepeat < self.repeats:
            self.function(*self.args, **self.kwargs)
            self._currentrepeat +=1
        self.finished.set()