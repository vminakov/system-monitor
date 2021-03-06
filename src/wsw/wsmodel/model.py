
import copy

from twisted.internet import task, inotify
from twisted.python import filepath
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

        for attributeName, attribute in self.__class__.__dict__.iteritems():
            if type(attribute) == Signal:
                setattr(self, attributeName, copy.deepcopy(attribute))

    def signalNamespace(self, protocol, name):
    	for attribute in dir(self):
    		if type(getattr(self, attribute)) == Signal:
    			getattr(self, attribute).init(protocol, name)

class AbstractTableModel(AbstractItemModel):
    class ModelIndex(object):    
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def column(self):
            return self.y

        def row(self):
            return self.x

    def index(self, x, y):
        return AbstractTableModel.ModelIndex(x, y)



class FileSystemWatcher(AbstractItemModel):
    
    directoryChanged = Signal(str)
    fileChanged = Signal(str)

    def __init__(self, parent=None):
        super(FileSystemWatcher, self).__init__(parent)

        self._paths = []
        self._notifier = inotify.INotify()
        self._notifier.startReading()

    def addPath(self, path):
        self._paths.append(path)
        self._notifier.watch(filepath.FilePath(path),
                             callbacks=[self.onChange])

    def onChange(self, watch, path, mask):
        self.fileChanged.emit(path)

    def addPaths(self, paths):
        pass

    def directories(self):
        return list()

    def files(self):
        return self._paths

    def removePath(self, path):
        pass

    def removePaths(self, paths):
        pass
