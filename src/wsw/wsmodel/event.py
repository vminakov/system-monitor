
import traceback, json

class Signal(object):

    wampProtocol = None

    def __init__(self, *valueTypes, **kwargs):
        """Creates new signal

        Nothing can be done really in signal constructor.
        WampProtocol is assigned during runtime, when model classes
        are instantiated. However, signals must be instantiated
        during class declaration, when wampProtocol is unknown.

        """

        self._callback = None
        self._isIntialized = False
        signalName = kwargs.pop('signalName', None)

        # if signal name is not passed, set it as name of the variable current signal instance
        # was assigned to.
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

    def init(self, instanceName, uri=None):
        """Initialize signal.

        instanceName muts be passed. Other configuration properties can be
        set from wampProtocol instance

        """
        if Signal.wampProtocol is None:
            raise RuntimeError("Cannot create a WebSocket Signal - no WampProtocol is registered")

        # by default, base signal URI is obtained from WampProtocol instances
        if uri is None:
            self.uri = Signal.wampProtocol.uri
        else:
            self.uri = uri

        # assigne instance name
        self.instanceName = instanceName
        self.uri = self.uri + '/' + self.instanceName + '.' + self.signalName
        self.wampProtocol.registerForPubSub(self.uri)

        self._isIntialized = True


    def emit(self, *data):
        if self._callback is not None:
            self._callback(*data)

        if self._isIntialized:
            serializableData = list()
            for dataItem in data:
                try:
                    json.dumps(dataItem)
                    serializableData.append(data)
                except:
                    serializableData.append(None)

            Signal.wampProtocol.dispatch(self.uri, serializableData)
            
            if self._callback is not None:
                self._callback(*data)


    def connect(self, callback):
        self._callback = callback


class Slot(object):

    wampProtocol = None

    def __init__(self, name, uri=None):
        if Slot.wampProtocol is None:
            raise RuntimeError("Cannot create a WebSocket Signal - no WampProtocol is registered")
        self.name = name
        if uri is None:
            self.uri = Slot.wampProtocol.uri
        else:
            self.uri = uri

    def connect(self, callback):
        pass
