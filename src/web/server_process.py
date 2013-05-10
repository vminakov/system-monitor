# -*- coding: utf-8 -*-
#
#     server_process.py
#       
#     WebSocket server responsible for handling process monitoring
#     data

import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
from autobahn.websocket import listenWS
from autobahn.wamp import WampServerFactory, WampServerProtocol
from wsw.wsmodel.event import Signal, Slot
from model.process import Process

class ProcessMonitorServerProtocol(WampServerProtocol):
   """
   This is simple process monitor server protocol.

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
      # current protocol as the communication channel
      Signal.wampProtocol = self
      Slot.wampProtocol = self

      # set up process model
      self.processModel = Process()
      self.processModel.signalNamespace("processModel")

      # expose model methods for RPC
      self.registerMethodForRpc(self.uri + '/processModel.rowCount', self.processModel,
         lambda i: self.processModel.rowCount())
      self.registerMethodForRpc(self.uri + '/processModel.columnCount', self.processModel,
         lambda i: self.processModel.columnCount())
      self.registerMethodForRpc(self.uri + '/processModel.headerData', self.processModel, 
         lambda section, i: self.processModel.headerData(i))
      self.registerMethodForRpc(self.uri + '/processModel.allData', self.processModel, 
         lambda i: self.processModel.allData())
      


   def connectionLost(self, reason):
      """
      When connection is gone (i.e. client close window, navigated
      away from the page), stop the model timer, which holds last
      reference to model, and delete the model
      """
      WampServerProtocol.connectionLost(self, reason)

      self.processModel.timer.stop()
      self.processModel = None


if __name__ == '__main__':

   if len(sys.argv) > 1 and sys.argv[1] == 'debug':
      log.startLogging(sys.stdout)
      debug = True
   else:
      debug = False

   factory = WampServerFactory("ws://localhost:9001", debugWamp = debug)
   factory.protocol = ProcessMonitorServerProtocol
   factory.setProtocolOptions(allowHixie76 = True)
   listenWS(factory)

   webdir = File(".")
   web = Site(webdir)
   reactor.listenTCP(8081, web)

   reactor.run()
