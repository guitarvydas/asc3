from fifo import FIFO
from message import Message

class Component:
    def __init__ (self, buildEnv, runEnv):
        self._buildEnv = buildEnv
        self._runEnv = runEnv
        self._inputq = FIFO ()
        self._outputq = FIFO ()

    # external to-be-implemented in descendent
    def step (self, message):
        raise Exception (f'step must be overridden for {self.name}')
    def inject (self, message):
        self._inputq.enqueue (message)
    def isBusy (self):
        raise Exception ("isBusy not overridden")

    # exported
    def run (self):
        while self.isBusy ():
            self.step ()
        while self.handleIfReady ():
            while self.isBusy ():
                self.step()


    def Handle (self, message):
        sub = None
        if 'subLayer' in self._buildEnv:
            sub = self._buildEnv ['subLayer']
        if self.HandlerChain (message, self._buildEnv ['handlerFunctions'].copy (), sub):
            return True
        else:
            self.Fail (message)

    def Fail (self, message):
        raise Exception (f'unhandled message {message.port} for {self.name}')
        return False

    def HandlerChain (self, message, functionList, subLayer):
        if 0 == len (functionList):
            if subLayer:
                return subLayer.Handle (message)
            else:
                return False
        else:
            handler = functionList.pop (0)
            restOfFunctionList = functionList
            if (message.port == handler.port):
                handler.func (message)
                return True
            else:
                return self.HandlerChain (message.port, message, restOfFunctionList, subLayer)

            
            
    def outputs (self):
        # return a dictionary of FIFOs, one FIFO per output port
        resultdict = {}
        for message in self._outputq.asDeque ():
            if (not (message.port in resultdict)):
                resultdict [message.port] = FIFO ()
            resultdict [message.port].enqueue (message.data)
        self.clearOutputs ()
        resultdict2 = {}
        for key in resultdict:
            fifo = resultdict [key]
            r = list (fifo.asDeque ())
            resultdict2 [key] = r
        return resultdict2
    def isReady (self):
        return (not self._inputq.isEmpty ())
    def name (self):
        parentname = ''
        if self._buildEnv.parent:
            parentname = self._buildEnv.parent.name () + '/'
        return f'{parentname}{self._runEnv.instanceName}'

    def baseName (self):
        return self._runEnv.instanceName

    # internal - not exported
    def clearOutputs (self):
        self._outputq = FIFO ()

    def enqueueInput (self, message):
        self._inputq.enqueue (message)
        
    def enqueueOutput (self, message):
        self._outputq.enqueue (message)
        

    def dequeueInput (self):
        return self._inputq.dequeue ()
    def dequeueOutput (self):
        return self._outputq.dequeue ()

    def send (self, portname, data, causingMessage):
        if (causingMessage == None):
            trail = [None]
        else:
            trail = [causingMessage, causingMessage.trail]
        m = Message (self, portname, data, trail)
        m.updateState ('output')
        self._outputq.enqueue (m)

# worker bees
    def handleIfReady (self):
        if self.isReady ():
            m = self.dequeueInput ();
            self.Handle (m)
            return True
        else:
            return False
    
