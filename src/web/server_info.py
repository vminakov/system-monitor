# -*- coding: utf-8 -*-
#
#     server_info.py
#       
#     WebSocket server responsible for handling 
#     general system infomation

import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

from autobahn.websocket import listenWS
from autobahn.wamp import WampServerFactory, WampServerProtocol

from wsw.wsmodel.event import Signal, Slot
from model.systeminfo import SystemInfo


class SystemInfoServerProtocol(WampServerProtocol):
   """
   This is simple system info server protocol.

   As with other server classes, model is created, when new connection
   is established, and deleted when client closes websocket connection
   """

   uri = "http://system-monitor.com"

   def onSessionOpen(self):
      """
      When connection is established, we create our
      model instances and register them for RPC if needed.
      """

      # all websocket signals and slots must use
      # current protocol as the communication channel
      Signal.wampProtocol = self
      Slot.wampProtocol = self

      # create system info model and register methods for RPC
      self.infoModel = SystemInfo()
      self.registerMethodForRpc(self.uri + '/sysInfo.getTotalMemory', self.infoModel, lambda i: self.infoModel.getTotalMemory())
      self.registerMethodForRpc(self.uri + '/sysInfo.getCpu', self.infoModel, lambda i: self.infoModel.getCpu())
      self.registerMethodForRpc(self.uri + '/sysInfo.getKernel', self.infoModel, lambda i: self.infoModel.getKernel())
      self.registerMethodForRpc(self.uri + '/sysInfo.getDistro', self.infoModel, lambda i: self.infoModel.getDistro())



   def connectionLost(self, reason):
      """
      When connection is gone (i.e. client close window, navigated
      away from the page), stop the model timer, which holds last
      reference to model, and delete the model
      """
      WampServerProtocol.connectionLost(self, reason)
      self.infoModel = None



if __name__ == '__main__':

   if len(sys.argv) > 1 and sys.argv[1] == 'debug':
      log.startLogging(sys.stdout)
      debug = True
   else:
      debug = False

   factory = WampServerFactory("ws://localhost:9000", debugWamp = debug)
   factory.protocol = SystemInfoServerProtocol
   factory.setProtocolOptions(allowHixie76 = True)
   listenWS(factory)

   webdir = File(".")
   web = Site(webdir)
   reactor.listenTCP(8080, web)

   reactor.run()
