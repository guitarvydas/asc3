from fifo import FIFO

class MessageHandler:
    def __init__ (self, handlerFunctions):
        self._handlerFunctions = handlerFunctions
        self._inputq = FIFO ()
        
    def inject (self, message):
        self._inputq.enqueue (message)


    def handleIfReady (self):
        if self.isReady ():
            m = self.dequeueInput ();
            self.handle (m)
            return True
        else:
            return False

    def isReady (self):
        return (0 < len (self._inputq))
    
# not exported
    def enqueueInput (self, message):
        self._inputq.enqueue (message)
        
    def dequeueInput (self):
        return self._inputq.dequeue ()


# worker bees
    def Fail (self, message):
        raise Exception (f'unhandled message {message.port} for {self.name}')
        return False

    def handlerChain (self, message, functionList, subLayer):
        if 0 == len (functionList):
            if subLayer:
                return subLayer.handle (message)
            else:
                return False
        else:
            handler = functionList.pop (0)
            restOfFunctionList = functionList
            if (message.port == handler.port):
                handler.func (message)
                return True
            else:
                return self.handlerChain (message.port, message, restOfFunctionList, subLayer)
    
            
