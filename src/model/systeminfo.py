
import psutil, subprocess, platform

from PySide import QtCore
from wsw.model import QAbstractItemModel
from model.util import humanize_bytes

class SystemInfo(QAbstractItemModel):

    def __init__(self, parent=None):
        super(SystemInfo, self).__init__(parent)

    def getTotalMemory(self):
        return humanize_bytes(psutil.virtual_memory().total)

    def getCpu(self):
        cpuInfo = []

        cmd = "cat /proc/cpuinfo | grep 'model name'"
        d = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        lines = d.stdout.readlines()
        for line in lines:
            cpuInfo.append(line.split(':', 1)[1].strip())

        return cpuInfo

    def getKernel(self):
        return platform.release()

    def getDistro(self):
        distro, version, codename = platform.linux_distribution()
        distro = distro[0].upper() + distro[1:]
        codename = codename[0].upper() + codename[1:]

        return " ".join([distro, version, codename])
        