from wsw.wsmodel.event import Signal

class AbstractItemModel(object):
    def __init__(self, parent=None):
        self.dataChanged = Signal("dataChanged signal")
        