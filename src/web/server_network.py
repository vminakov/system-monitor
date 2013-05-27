# -*- coding: utf-8 -*-
#
#     server_network.py
#       
#     WebSocket server responsible for handling network monitoring
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
from model.networkinfo import NetworkInfo


class NetworkInfoServerProtocol(WampServerProtocol):
   """
   This is simple netowrk monitor server protocol.

   As with other server classes, model is created, when new connection
   is established, and deleted when client closes websocket connection
   """

   uri = "http://system-monitor.com"

   def onSessionOpen(self):
      """
      When connection is established, we create our
      model instances and register them for RPC if needed.
      """

      # create and setup network info model
      self.netInfoModels = []

      ifaces = self.getIfaces()
      for iface in ifaces:
         netInfoModel = NetworkInfo(iface, 2)
         modelName = 'netInfoModel' + iface
         netInfoModel.signalNamespace(self, modelName)
         self.netInfoModels.append(netInfoModel)

      self.registerForRpc(self, self.uri + '/network#')


   def connectionLost(self, reason):
      """
      When connection is gone (i.e. client close window, navigated
      away from the page), stop the model timer, which holds last
      reference to model, and delete the model
      """
      WampServerProtocol.connectionLost(self, reason)

      for model in self.netInfoModels:
         model.timer.stop()

      self.netInfoModels = []

   @exportRpc
   def getIfaces(self):
      """
      Return names of all available network interfaces
      """
      ifaces = psutil.network_io_counters(pernic=True).keys()
      ifaces.append('total')

      return ifaces


if __name__ == '__main__':

   if len(sys.argv) > 1 and sys.argv[1] == 'debug':
      log.startLogging(sys.stdout)
      debug = True
   else:
      debug = False

   factory = WampServerFactory("ws://localhost:9004", debugWamp = debug)
   factory.protocol = NetworkInfoServerProtocol
   factory.setProtocolOptions(allowHixie76 = True)
   listenWS(factory)

   webdir = File(".")
   web = Site(webdir)
   reactor.listenTCP(8084, web)

   reactor.run()
