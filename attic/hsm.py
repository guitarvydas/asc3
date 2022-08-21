class HSM:
    def __init__ (self, buildEnv, runEnv, stateDescriptorList, defaultStateName):
        self._messageHandler = MessageHandler (self, buildEnv, runEnv)
        self._messageSender = MessageSender (self, buildEnv, runEnv)
        self._runnable = Runnable (self, buildEnv, runEnv)
        self._machineEnter = buildEnv ["enter"]
        self._machineExit = buildEnv ["exit"]
        for proto in stateDescriptorList:
            self._states.append (proto.kind (self, proto.enter, proto.handle, proto.exit)
        self._state = None
        self._defaultStateName = defaultStateName
        self.enterDefault ()
        
    def reset (self):
        self.exitState ()
        self.enterDefault ()

    def enterState (self):
        self._state.enter ()

    def exitState (self):
        self._state.exit ()

    def enterDefault (self):
        defaultState = self.LookupState ('default')
        self._state = defaultState
        self.enterState ()

    def enter (self):
        self._machineEnter ()
        if self._subLayer:
            self._subLayer.enter ()

    def exit (self):
        if self._subLayer:
            self._subLayer.exit ()
        self._machineEnter ()


    def step (self):
        self._state.step ()

    def isBusy (self):
        return self._state.isBusy ()

    def handle (self, message):
        return self._state.handle (message)

    def next (self, nextState):
        self.exitState ()
        self._state = nextState
        self.enterState ()


# delegations
    def run (self):
        self._runnable.run ()

    def handle (self, message):
        return self._state.handle (message)  # punt to _state
    def handleIfReady (self):
        return self._messageHandler.handleIfReady ()
    def inject (self, message):
        return self._messageHandler.inject (message)
    def isReady (self, message):             # trickle downwards
        if self._state.isBusy ():
            return False
        return self._messageHandler.isReady ()
        

    def send (self, port, message, cause):
        return self._messageSender.send (port, message, cause)
    def outputs (self):
        return self._messageSender.outputs ()

# worker bees
    def lookupState (self, name):
        for state in self._states:
            if state.baseName () == name:
                return state
        raise Exception (f'internal error: State /{name}/ not found in {self.baseName ()}') 
