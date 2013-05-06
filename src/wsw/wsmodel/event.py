
import traceback

class Signal(object):

    wampProtocol = None

    def __init__(self, acceptedType, signalName=None, uri=None):
        if Signal.wampProtocol is None:
            raise RuntimeError("Cannot create a WebSocket Signal - no WampProtocol is registered")

        if signalName is None:
            (filename,line_number,function_name,text) = traceback.extract_stack()[-2]
            self.signalName = text[:text.find('=')].strip()
            try:
                # remove '.' from signal name (e.g. if it was assigned like self.dataChanged = Signal())
                self.signalName = self.signalName[self.signalName.rindex('.') + 1:]
            except:
                pass

        else:
            self.signalName = signalName

        if uri is None:
            self.uri = Signal.wampProtocol.uri
        else:
            self.uri = uri

    def setInstanceName(self, instanceName):
        self.instanceName = instanceName
        self.uri = self.uri + '/' + self.instanceName + '.' + self.signalName
        self.wampProtocol.registerForPubSub(self.uri)


    def emit(self, data1, data2):
        Signal.wampProtocol.dispatch(self.uri, data1)


class Slot(object):

    wampProtocol = None

    def _init_(self, name, uri=None):
        if Slot.wampProtocol is None:
            raise RuntimeError("Cannot create a WebSocket Signal - no WampProtocol is registered")
        self.name = name
        if uri is None:
            self.uri = Slot.wampProtocol.uri
        else:
            self.uri = uri

    def connect(self, callback):
        pass
