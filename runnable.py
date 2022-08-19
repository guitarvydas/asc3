from fifo import FIFO
from messagesender import MessageSender

class Runnable (MessageSender):
    def __init__ (self, buildEnv, runEnv):
        self._buildEnv = buildEnv
        self._runEnv = runEnv
        self._inputq = FIFO ()
        self._outputq = FIFO ()

    # external to-be-implemented in descendent
    def step (self, message):
        raise Exception (f'step must be overridden for {self.name}')
    def isBusy (self):
        raise Exception ("isBusy not overridden")

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


