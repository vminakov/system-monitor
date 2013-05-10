from PySide import QtGui
from ui.ui_logbrowser import Ui_LogBrowser
#from model.process import Process

class LogBrowser(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_LogBrowser()
        self.ui.setupUi(self)

        # self.model = Process()

        # self.ui.tableView.setModel(self.model)
        