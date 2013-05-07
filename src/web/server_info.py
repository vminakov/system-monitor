###############################################################################
##
##  Copyright 2011,2012 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from twisted.python import log
from twisted.internet import reactor, defer
from twisted.web.server import Site
from twisted.web.static import File

from autobahn.websocket import listenWS
from autobahn.wamp import exportRpc, \
                          WampServerFactory, \
                          WampServerProtocol

from wsw.wsmodel.event import Signal, Slot
from model.systeminfo import SystemInfo


class SystemInfoServerProtocol(WampServerProtocol):
   """
   Demonstrates creating a simple server with Autobahn WebSockets that
   responds to RPC calls.
   """

   uri = "http://example.com/simple"

   def onSessionOpen(self):

      Signal.wampProtocol = self
      Slot.wampProtocol = self

      # when connection is established, we create our
      # model instances and register them for RPC. that's it.

      # create system info model and register methods for RPC
      self.infoModel = SystemInfo()
      self.registerMethodForRpc(self.uri + '/sysInfo.getTotalMemory', self.infoModel, lambda i: self.infoModel.getTotalMemory())
      self.registerMethodForRpc(self.uri + '/sysInfo.getCpu', self.infoModel, lambda i: self.infoModel.getCpu())
      self.registerMethodForRpc(self.uri + '/sysInfo.getKernel', self.infoModel, lambda i: self.infoModel.getKernel())
      self.registerMethodForRpc(self.uri + '/sysInfo.getDistro', self.infoModel, lambda i: self.infoModel.getDistro())



   def connectionLost(self, reason):
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
