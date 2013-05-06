
from twisted.internet import task
from wsw.wsmodel.event import Signal

class Timer(object):
	def __init__(self, parent=None):
		self.timeout = TimeoutSignal()

	def start(self, delay=1000):
		time_in_sec = float(delay) / float(1000)
		self.l = task.LoopingCall(self.timeout.callback)
		self.l.start(time_in_sec)

	def stop(self):
		self.l.stop()

class TimeoutSignal(object):
	def connect(self, callback):
		self.callback = callback




class AbstractItemModel(object):
    def __init__(self, parent=None):
        self.dataChanged = Signal()

    def signalNamespace(self, name):
    	for attribute in dir(self):
    		if type(getattr(self, attribute)) == Signal:
    			getattr(self, attribute).setInstanceName(name)

