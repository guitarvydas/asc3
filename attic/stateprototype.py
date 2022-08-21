from runnable import Runnable
from messagehandler import MessageHandler
from messagesender import MessageSender
from runnable import Runnable

class StatePrototype:
    def __init__ (self, machine, buildEnv):
        self._machine = machine
        self._messageHandler = MessageHandler (self, buildEnv, machine.runEnv ())
        self._messageSender = machine.messageSender ()
        self._runnable = machine.runnable ()

    def step (self):
        if self._buildEnv.subLayer:
            self._buildEnv.subLayer.step ()
        else:
            pass
    
    def isBusy (self):
        if self._buildEnv.subLayer:
            return self._buildEnv.subLayer.isBusy ()
        else:
            return False

    def send (self, port, message, cause):
        return self._machine.messageSender ().send (port, message, cause)

    def enter (self):
        self._buildEnv.enter (self)

    def exit (self):
        self._buildEnv.exit (self)            
