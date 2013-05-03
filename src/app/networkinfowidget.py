from PySide import QtGui
from ui.ui_networkinfo import Ui_NetworkInfo

class NetworkInfoWidget(QtGui.QWidget):

    def __init__(self, iface, netmodel, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_NetworkInfo()
        self.ui.setupUi(self)

        self.ui.groupBox.setTitle("%s:" % iface)
        self.model = netmodel

        self.model.bytesSentChanged.connect(self.ui.labelBytesSentTotal.setText)
        self.model.bytesReceivedChanged.connect(self.ui.labelBytesReceivedTotal.setText)
        self.model.packetsSentChanged.connect(self.ui.labelPacketsSentTotal.setText)
        self.model.packetsReceivedChanged.connect(self.ui.labelPacketsReceivedTotal.setText)
        
        self.model.bytesSentSpeedChanged.connect(self.ui.labelBytesSentSpeed.setText)
        self.model.bytesReceivedSpeedChanged.connect(self.ui.labelBytesReceivedSpeed.setText)
        self.model.packetsSentSpeedChanged.connect(self.ui.labelPacketsSentSpeed.setText)
        self.model.packetsReceivedSpeedChanged.connect(self.ui.labelPacketsReceivedSpeed.setText)