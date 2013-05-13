# -*- coding: utf-8 -*-
#
#     server_lgo.py
#       
#     WebSocket server responsible for handling log update events

import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
from autobahn.websocket import listenWS
from autobahn.wamp import WampServerFactory, WampServerProtocol, exportRpc
from wsw.wsmodel.event import Signal, Slot
from model.loginfo import LogInfo

class LogMonitorServerProtocol(WampServerProtocol):
   """
   This is simple log browser server protocol.

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
      self.logModel = LogInfo()
      self.logModel.signalNamespace("logModel")
      self.logModel.setLogFile('/var/log/syslog')

      # expose model methods for RPC
      self.registerMethodForRpc(self.uri + '/logModel.readLastLines', self.logModel,
         lambda i: self.logModel.readLastLines())

      #self.registerForRpc(self.uri+ '/logModel', self)
      self.registerMethodForRpc(self.uri + '/logModel.changeLogFile', self,
         lambda i, logNum: self.changeLogFile(logNum))


   @exportRpc
   def changeLogFile(self, logNum):
      paths = [
         '/var/log/syslog',
         '/var/log/messages',
         '/var/log/kern.log',
         '/var/log/auth.log']
      log = paths[int(logNum)]
      self.logModel.setLogFile(log)


   def connectionLost(self, reason):
      """
      When connection is gone (i.e. client close window, navigated
      away from the page), stop the model timer, which holds last
      reference to model, and delete the model
      """
      WampServerProtocol.connectionLost(self, reason)

      #self.logModel.timer.stop()
      self.logModel = None


if __name__ == '__main__':

   if len(sys.argv) > 1 and sys.argv[1] == 'debug':
      log.startLogging(sys.stdout)
      debug = True
   else:
      debug = False

   factory = WampServerFactory("ws://localhost:9005", debugWamp = debug)
   factory.protocol = LogMonitorServerProtocol
   factory.setProtocolOptions(allowHixie76 = True)
   listenWS(factory)

   webdir = File(".")
   web = Site(webdir)
   reactor.listenTCP(8085, web)

   reactor.run()
