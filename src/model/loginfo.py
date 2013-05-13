# -*- coding: utf-8 -*-
#
#       loginfo.py
#       
#       Model class for monitoring system log files

import os
from wsw.model import QAbstractItemModel, QFileSystemWatcher, Signal

class LogInfo(QAbstractItemModel):
    """
    Class for monitoring system log files.

    When model is instantiated and path to system log
    is set through setLogFile(), lineAdded signal is
    emitted when new line is appended to the
    monitored file
    """

    lineAdded = Signal(str)

    def __init__(self, parent=None):
        super(LogInfo, self).__init__(parent)

        self._f = None
        self._path = None


    def setLogFile(self, pathToFile):
        self._path = pathToFile

        if self._f is not None:
            self._f.close()

        self._f = open(self._path, 'r')

        self.watcher = QFileSystemWatcher()
        self.watcher.addPath(self._path)
        self.watcher.fileChanged.connect(self._readNewLines)

    def readLastLines(self, maxNumOflines=10):
        if self._f is None:
            raise RuntimeError("No path to log file has been set")
        maxOffset = 1024 * maxNumOflines
        
        if os.path.getsize(self._path) <= maxOffset:
            return self._f.read()
        else:
            self._f.seek(-maxOffset, os.SEEK_END)
            lines = self._f.readlines()
            if len(lines) > maxNumOflines:
                return lines[-maxNumOflines:]
            else:
                return lines


    def _readNewLines(self, path):
        newLines = self._f.read().splitlines()
        for line in newLines:
            self.lineAdded.emit(line)
        