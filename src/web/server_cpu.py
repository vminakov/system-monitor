# -*- coding: utf-8 -*-
#
#     server_cpu.py
#       
#     WebSocket server responsible for handling CPU monitoring
#     data

import sys, os, psutil

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

from autobahn.websocket import listenWS
from autobahn.wamp import exportRpc, \
                          WampServerFactory, \
                          WampServerProtocol

from wsw.wsmodel.event import Signal, Slot
from model.cpuchart import CpuChart


class MemoryMonitorServerProtocol(WampServerProtocol):
   """
   This is simple CPU monitor server protocol.

   As with other server classes model is created, when new connection
   is established, and deleted when client closes websocket connection
   """

   uri = "http://system-monitor.com"

   def onSessionOpen(self):
      """
      When connection is established, we create our
      model instances and register them for RPC. that's it.
      """

      # create and setup cpu models
      self.cpuModels = []
      numOfCpus = len(psutil.cpu_percent(interval=None, percpu=True))
      for i in range(numOfCpus):
         modelName = "cpuModel%s" % i
         cpuModel = CpuChart(i)
         cpuModel.signalNamespace(self, modelName)
         self.registerMethodForRpc(self.uri + '/' + modelName + '.data', cpuModel, cpuModel.data)
         self.cpuModels.append(cpuModel)

      self.registerForRpc(self, self.uri + '/cpu#')


   def connectionLost(self, reason):
      """
      When connection is gone (i.e. client close window, navigated
      away from the page), stop the model timer, which holds last
      reference to model, and delete the model
      """

      WampServerProtocol.connectionLost(self, reason)

      for model in self.cpuModels:
         model.timer.stop()

      self.cpuModels = []

   @exportRpc
   def getCpuNum(self):
      """
      Return number of CPUs in system
      """
      return len(psutil.cpu_percent(interval=None, percpu=True))


if __name__ == '__main__':

   if len(sys.argv) > 1 and sys.argv[1] == 'debug':
      log.startLogging(sys.stdout)
      debug = True
   else:
      debug = False

   factory = WampServerFactory("ws://localhost:9003", debugWamp = debug)
   factory.protocol = MemoryMonitorServerProtocol
   factory.setProtocolOptions(allowHixie76 = True)
   listenWS(factory)

   webdir = File(".")
   web = Site(webdir)
   reactor.listenTCP(8083, web)

   reactor.run()
