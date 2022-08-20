from fifo import FIFO
from messagesender import MessageSender

class Runnable:
    def __init__ (self, owner, buildEnv, runEnv):
        self._owner = owner
        self._buildEnv = buildEnv
        self._runEnv = runEnv
        self._inputq = FIFO ()
        self._outputq = FIFO ()

    # external to-be-implemented in owner
    def step (self):
        return self._owner.step ()
    def isBusy (self):
        return self._owner.isBusy ()
    def handleIfReady (self):
        return self._owner.handleIfReady ()

    # exported
    def run (self):
        while self.isBusy ():
            self.step ()
        while self.handleIfReady ():
            while self.isBusy ():
                self.step()

            
            
    def name (self):
        parentname = ''
        if self._buildEnv.parent:
            parentname = self._buildEnv.parent.name () + '/'
        return f'{parentname}{self._runEnv.instanceName}'

    def baseName (self):
        return self._runEnv.instanceName


