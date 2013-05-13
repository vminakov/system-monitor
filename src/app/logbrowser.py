from PySide import QtGui
from ui.ui_logbrowser import Ui_LogBrowser
from model.loginfo import LogInfo

class LogBrowser(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_LogBrowser()
        self.ui.setupUi(self)

        self.ui.comboBox.currentIndexChanged.connect(self.logChanged)

        self.model = LogInfo()
        self.model.setLogFile('/var/log/syslog')
        self.ui.textBrowser.append(''.join(self.model.readLastLines()))
        self.model.lineAdded.connect(self.addLogEntry)

    def addLogEntry(self, line):
    	self.ui.textBrowser.append(line)

    def logChanged(self, index):
    	paths = [
    		'/var/log/syslog',
    		'/var/log/messages',
    		'/var/log/kern.log',
    		'/var/log/auth.log']
    	path = paths[index]

    	self.model.setLogFile(path)
    	self.ui.textBrowser.setPlainText(''.join(self.model.readLastLines()))
