class MessageHandler:
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


# worker bees
    def handleIfReady (self):
        if self.isReady ():
            m = self.dequeueInput ();
            self.Handle (m)
            return True
        else:
            return False
    
            
