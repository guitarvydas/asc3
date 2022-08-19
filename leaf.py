from runnable import Runnable
from messagehandler import MessageHandler
from messagesender import MessageSender
from runnable import Runnable

class Leaf:
    def __init__ (self, buildEnv, runEnv):
        self._messageHandler = MessageHandler (self, buildEnv, runEnv)
        self._messageSender = MessageSender (self, buildEnv, runEnv)
        self._runnable = Runnable (self, buildEnv, runEnv)
        
    # a Leaf always completes a step when Handle() is called
    # and is never busy
    # (This is different for composite state machines)
    def step (self):
        pass
    
    def isBusy (self):
        return False

    # delegations...
    def run (self):
        self._runnable.run ()

    
    def Handle (self, message):
        return self._messageHandler.Handle (message)
    def handleIfReady (self):
        return self._messageHandler.handleIfReady ()
    def inject (self, message):
        return self._messageHandler.inject (message)
    def isReady (self, message):
        return self._messageHandler.Handle ()
        

    def send (self, port, message, cause):
        return self._messageSender.send (port, message, cause)
    def outputs (self):
        return self._messageSender.outputs ()
