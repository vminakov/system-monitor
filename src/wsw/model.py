from PySide.QtGui import QApplication

import __main__

try:
    if __main__.__IN_QT__ == True:
    # we're inside QApplication
        from PySide.QtCore import QAbstractItemModel as BaseAbstractItemModel
        from PySide.QtCore import QAbstractTableModel as BaseAbstractTableModel
except (NameError, AttributeError):
    print ("importing from WSW")
    from wsw.wsmodel.model import AbstractItemModel as BaseAbstractItemModel
    #from wsw.wsmodel.model import AbstractTableModel as BaseAbstractTableModel
   

class QAbstractItemModel(BaseAbstractItemModel):
    pass

#class QAbstractTableModel(BaseAbstractTableModel):
#    pass