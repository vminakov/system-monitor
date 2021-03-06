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
from model.memorychart import MemoryChart
from model.memoryinfo import MemoryInfo


class MemoryMonitorServerProtocol(WampServerProtocol):
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

      # first of all, create and setup chart models
      self.memoryChartVirt = MemoryChart("virt")
      self.memoryChartVirt.signalNamespace("memoryChartVirt")
      self.registerMethodForRpc(self.uri + '/memoryChartVirt.data', self.memoryChartVirt, self.memoryChartVirt.data)

      self.memoryChartSwap = MemoryChart("swap")
      self.memoryChartSwap.signalNamespace("memoryChartSwap")
      self.registerMethodForRpc(self.uri + '/memoryChartSwap.data', self.memoryChartSwap, self.memoryChartSwap.data)

      # thereafter, setup memory info models
      self.memoryInfoVirt = MemoryInfo("virt")
      self.memoryInfoVirt.signalNamespace("memoryInfoVirt")


   def connectionLost(self, reason):
      WampServerProtocol.connectionLost(self, reason)

      self.memoryChartVirt.timer.stop()
      self.memoryChartVirt = None

      self.memoryChartSwap.timer.stop()
      self.memoryChartSwap = None



if __name__ == '__main__':

   if len(sys.argv) > 1 and sys.argv[1] == 'debug':
      log.startLogging(sys.stdout)
      debug = True
   else:
      debug = False

   factory = WampServerFactory("ws://localhost:9000", debugWamp = debug)
   factory.protocol = MemoryMonitorServerProtocol
   factory.setProtocolOptions(allowHixie76 = True)
   listenWS(factory)

   webdir = File(".")
   web = Site(webdir)
   reactor.listenTCP(8080, web)

   reactor.run()
