class HSM:
    def __init__ (functions, defaultStateName, enter, states, exit):
        self._functions = functions
        self._defaultStateName = defaultStateName
        self._enter = enter
        self._states = states
        self._exit = exit
        self._state = None
        self.enterDefault ()
        
    def enterDefault (self):
        self._state = self.lookupState (self._defaultStateName, self._states)
        self.enterState ()

    def enter (self):
        f = self._enter
        if f:
            f (self)
            
    def exit (self):
        f = self._exit
        if f:
            f (self)

    def enterState (self):
        self._state.enter ()
        
    def exitState (self):
        self._state.exit ()
        
    def next (self, stateName):
        self.exitState ()
        self._state = self.lookupState (stateName, self._states)
        self.enterState ()

        
    def reset (self):
        self._state.reset ()
        self._state.exit ()
        self.enterDefault ()

    def send (self, port, data, cause):
        self._parent.send (port, data, cause)
    def outputs (self):
        self._parent.outputs ()

# worker

    def lookupState (self, name, stateList):
        if (0 >= len (stateList)):
            return None
        elif (name == stateList [0].name:
              return stateList [0]
        else:
              return self.lookupState (name, stateList [1:])
