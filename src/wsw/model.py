
import __main__

try:
    if __main__.__IN_QT__ == True:
    # we're inside QApplication
        
        from PySide.QtCore import QAbstractItemModel as BaseAbstractItemModel
        from PySide.QtCore import QAbstractTableModel as BaseAbstractTableModel
        from PySide.QtCore import QFileSystemWatcher as BaseFileSystemWatcher
        from PySide.QtCore import QTimer as BaseTimer
        from PySide.QtCore import Signal as BaseSignal
        from PySide.QtCore import Slot as BaseSlot
except (NameError, AttributeError):
    print ("importing from WSW")
    from wsw.wsmodel.model import AbstractItemModel as BaseAbstractItemModel
    from wsw.wsmodel.model import AbstractTableModel as BaseAbstractTableModel
    from wsw.wsmodel.model import FileSystemWatcher as BaseFileSystemWatcher
    from wsw.wsmodel.model import Timer as BaseTimer
    from wsw.wsmodel.event import Signal as BaseSignal
    from wsw.wsmodel.event import Slot as BaseSlot

class QAbstractItemModel(BaseAbstractItemModel):
    pass

class QAbstractTableModel(BaseAbstractTableModel):
    pass

class QFileSystemWatcher(BaseFileSystemWatcher):
    pass

class QTimer(BaseTimer):
	pass

class Signal(object):
	pass

class Slot(object):
	pass

Signal = BaseSignal
Slot = BaseSlot
