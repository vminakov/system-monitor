
import psutil

from wsw.model import QAbstractItemModel, QTimer
from wsw.model import Signal
from model.util import humanize_bytes

class NetworkInfo(QAbstractItemModel):

    bytesSentChanged = Signal(str)
    bytesReceivedChanged = Signal(str)
    packetsSentChanged = Signal(str)
    packetsReceivedChanged = Signal(str)

    bytesSentSpeedChanged = Signal(str)
    bytesReceivedSpeedChanged = Signal(str)
    packetsSentSpeedChanged = Signal(str)
    packetsReceivedSpeedChanged = Signal(str)

    def __init__(self, iface, refreshRate = 1, parent=None):
        super(NetworkInfo, self).__init__(parent)

        self._iface = iface
        self._refreshRate = refreshRate

        self._bytesSent = None
        self._bytesReceived = None
        self._packetsSent = None
        self._packetsReceived = None

        self._bytesSentSpeed = None
        self._bytesReceivedSpeed = None
        self._packetsSentSpeed = None
        self._packetsReceivedSpeed = None

        self._firstRun = True

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._refresh)
        self.timer.start(self._refreshRate * 1000)

    def _refresh(self):
        if self._iface != 'total':
            netinfo = psutil.network_io_counters(pernic=True)[self._iface]
        else:
            netinfo = psutil.network_io_counters()    
        
        
        if self._firstRun:
            self._bytesSentSpeed = '0 bytes/s'
            self._bytesReceivedSpeed = '0 bytes/s'
            self._packetsSentSpeed = '0 packets/s'
            self._packetsReceivedSpeed = '0 packets/s'

            self.bytesSentSpeedChanged.emit(self._bytesSentSpeed)
            self.bytesReceivedSpeedChanged.emit(self._bytesReceivedSpeed)
            self.packetsSentSpeedChanged.emit(self._packetsSentSpeed)
            self.packetsReceivedSpeedChanged.emit(self._packetsReceivedSpeed)

            self._bytesSent = netinfo.bytes_sent
            self._bytesReceived = netinfo.bytes_recv
            self._packetsSent = netinfo.packets_sent
            self._packetsReceived = netinfo.packets_recv

            self.bytesSentChanged.emit(humanize_bytes(self._bytesSent, 2))
            self.bytesReceivedChanged.emit(humanize_bytes(self._bytesReceived, 2))
            self.packetsSentChanged.emit(str(self._packetsSent))
            self.packetsReceivedChanged.emit(str(self._packetsReceived))

            self._firstRun = False

        else:
            # calculate data transmision speeds per minute
            speed = humanize_bytes((netinfo.bytes_sent - self._bytesSent) / self._refreshRate, 2) + '/s'
            if speed != self._bytesSentSpeed:
                self._bytesSentSpeed = speed
                self.bytesSentSpeedChanged.emit(self._bytesSentSpeed)

            speed = humanize_bytes((netinfo.bytes_recv - self._bytesReceived) / self._refreshRate, 2) + '/s'
            if speed != self._bytesReceivedSpeed:
                self._bytesReceivedSpeed = speed
                self.bytesReceivedSpeedChanged.emit(self._bytesReceivedSpeed)

            speed = str(netinfo.packets_sent - self._packetsSent) + ' packets/s'
            if speed != self._packetsSentSpeed:
                self._packetsSentSpeed = speed
                self.packetsSentSpeedChanged.emit(self._packetsSentSpeed)

            speed = str(netinfo.packets_recv - self._packetsReceived) + ' packets/s'
            if speed != self._packetsReceivedSpeed:
                self._packetsReceivedSpeed = speed
                self.packetsReceivedSpeedChanged.emit(self._packetsReceivedSpeed)


            # calculate total data transfered
            if (netinfo.bytes_sent != self._bytesSent):
                self._bytesSent = netinfo.bytes_sent
                #print(self._iface + ': Bytes sent: ' + str(self._bytesSent))
                self.bytesSentChanged.emit(humanize_bytes(self._bytesSent, 2))

            if (netinfo.bytes_recv != self._bytesReceived):
                self._bytesReceived = netinfo.bytes_recv
                #print(self._iface + ': Bytes received' + str(self._bytesReceived))
                self.bytesReceivedChanged.emit(humanize_bytes(self._bytesReceived, 2))

            if (netinfo.packets_sent != self._packetsSent):
                self._packetsSent = netinfo.packets_sent
                self.packetsSentChanged.emit(str(self._packetsSent))

            if (netinfo.packets_recv != self._packetsReceived):
                self._packetsReceived = netinfo.packets_recv
                self.packetsReceivedChanged.emit(str(self._packetsReceived))
