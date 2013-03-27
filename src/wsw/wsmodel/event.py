class Signal(object):

    wampProtocol = None

    def __init__(self, name, uri=None):
        if Signal.wampProtocol is None:
            raise RuntimeError("Cannot create a WebSocket Signal - no WampProtocol is registered")
        self.name = name
        if uri is None:
            self.uri = Signal.wampProtocol.uri
        else:
            self.uri = uri
        

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
