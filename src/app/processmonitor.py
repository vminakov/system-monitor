from PySide import QtGui
from ui.ui_processmonitor import Ui_ProcessMonitor
from model.process import Process

class ProcessMonitor(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_ProcessMonitor()
        self.ui.setupUi(self)

        self.model = Process()

        self.ui.tableView.setModel(self.model)
        