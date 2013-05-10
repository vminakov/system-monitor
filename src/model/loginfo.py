
import os
from PySide import QtCore
from wsw.model import QAbstractItemModel, Signal

class LogInfo(QAbstractItemModel):

    lineAdded = Signal(str)

    def __init__(self, pathToFile='/var/log/syslog', parent=None):
        super(LogInfo, self).__init__(parent)

        self._path = pathToFile
        self._f = open(self._path, 'r')
        #self._f.seek(0, os.SEEK_END)
        #self._fPos = self._f.tell()


        self.watcher = QtCore.QFileSystemWatcher()
        self.watcher.addPath(self._path)
        self.watcher.fileChanged.connect(self.readNewLines)

    def readNewLines(self, path):
        newLines = self._f.read().splitlines()
        for line in newLines:
            self.lineAdded.emit(line)
        