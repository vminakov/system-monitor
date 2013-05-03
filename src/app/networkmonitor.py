
import psutil

from PySide import QtGui, QtCore
from app.networkinfowidget import NetworkInfoWidget
from model.networkinfo import NetworkInfo

class NetworkMonitor(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        vbox = QtGui.QVBoxLayout()

        # iterate over all available interfaces (+ pseudo 'all' inteface)
        ifaces = psutil.network_io_counters(pernic=True).keys()
        ifaces.append('total')
        for iface in ifaces:
            netmodel = NetworkInfo(iface)
            netwidget = NetworkInfoWidget(iface, netmodel)

            vbox.addWidget(netwidget)


        self.setLayout(vbox)
        self.show()
