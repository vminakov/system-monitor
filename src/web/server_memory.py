# -*- coding: utf-8 -*-
#
#     server_memory.py
#       
#     WebSocket server responsible for handling memory monitoring
#     data

import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

from autobahn.websocket import listenWS
from autobahn.wamp import WampServerFactory, \
                          WampServerProtocol

from wsw.wsmodel.event import Signal, Slot
from model.memorychart import MemoryChart
from model.memoryinfo import MemoryInfo


class MemoryMonitorServerProtocol(WampServerProtocol):
   """
   This is simple memory monitor server protocol.

   As with other server classes model is created, when new connection
   is established, and deleted when client closes websocket connection
   """

   uri = "http://system-monitor.com"

   def onSessionOpen(self):
      """
      When connection is established, we create our
      model instances and register them for RPC. that's it.
      """

      # all websocket signals and slots must use
      # current protocol as the communication channel,
      # so pass 'self' to signalNamespace method of models


      # first of all, create and setup chart models
      self.memoryChartVirt = MemoryChart("virt")
      self.memoryChartVirt.signalNamespace(self, "memoryChartVirt")
      self.registerMethodForRpc(self.uri + '/memoryChartVirt.data', self.memoryChartVirt, self.memoryChartVirt.data)

      self.memoryChartSwap = MemoryChart("swap")
      self.memoryChartSwap.signalNamespace(self, "memoryChartSwap")
      self.registerMethodForRpc(self.uri + '/memoryChartSwap.data', self.memoryChartSwap, self.memoryChartSwap.data)

      # thereafter, setup memory info models
      self.memoryInfoVirt = MemoryInfo("virt")
      self.memoryInfoVirt.signalNamespace(self, "memoryInfoVirt")
      self.registerMethodForRpc(self.uri + '/memoryInfoVirt.getCounters', self.memoryInfoVirt, lambda i: self.memoryInfoVirt.getCounters())

      self.memoryInfoSwap = MemoryInfo("swap")
      self.memoryInfoSwap.signalNamespace(self, "memoryInfoSwap")
      self.registerMethodForRpc(self.uri + '/memoryInfoSwap.getCounters', self.memoryInfoSwap, lambda i: self.memoryInfoSwap.getCounters())


   def connectionLost(self, reason):
      """
      When connection is gone (i.e. client close window, navigated
      away from the page), stop the model timer, which holds last
      reference to model, and delete the model
      """
      
      WampServerProtocol.connectionLost(self, reason)

      self.memoryChartVirt.timer.stop()
      self.memoryChartVirt = None

      self.memoryChartSwap.timer.stop()
      self.memoryChartSwap = None

      self.memoryInfoVirt.timer.stop()
      self.memoryInfoVirt = None

      self.memoryInfoSwap.timer.stop()
      self.memoryInfoSwap = None



if __name__ == '__main__':

   if len(sys.argv) > 1 and sys.argv[1] == 'debug':
      log.startLogging(sys.stdout)
      debug = True
   else:
      debug = False

   factory = WampServerFactory("ws://192.168.1.66:9002", debugWamp = debug)
   factory.protocol = MemoryMonitorServerProtocol
   factory.setProtocolOptions(allowHixie76 = True)
   listenWS(factory)

   webdir = File(".")
   web = Site(webdir)
   reactor.listenTCP(8082, web)

   reactor.run()
