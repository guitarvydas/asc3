class State:
    def __init__ (self, machine, enter, handlerFunctions, exit, subMachine):
        self._machine = machine
        self._enter = enter
        self._handlerFunctions = handlerFunctions
        self._exit = exit
        self._subMachine = subMachine
        
    def step (self):
        if self._subMachine
            self._subMachine.step ()
        else:
            pass
    
    def isBusy (self):
        if self._subMachine:
            return self._subMachine.isBusy ()
        else:
            return False

    def send (self, port, message, cause):
        return self._machine.messageSender ().send (port, message, cause)

    def enter (self):
        self._enter (self)

    def exit (self):
        self._exit (self)

    def handle (self, message):
        r = self.handlerChain (self._handlerFunctions, message)
        if r:
            return r
        elif self._subMachine:
            return self._subMachine.handle (message)
        else:
            return False

    def reset (self):
        if self._subMachine:
            return self._subMachine.reset ()
        else:
            return None
