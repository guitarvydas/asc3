from component import Component

debugHSM = True
class HSM (Component):
    def __init__ (self, buildEnv, runEnv):
        super ().__init__ (buildEnv, runEnv))
        self._machineEnter = buildEnv ["enter"]
        self._machineExit = buildEnv ["exit"]
        self._state = None
        self._defaultStateName = defaultStateName
        self._states = buildEnv ["states"]
        self.enterDefault ()
        
    def __repr__ (self):
        return f'<machine {self.name ()}>'

    def name (self):
        return f'{super ().name ()}[{self._state.name ()}]'

    def enter (self):
        if debugHSM:
            print (f'< {self.name ()} >')
        if self._machineEnter:
            self._machineEnter ()
        self._state.enter ()

    def exit (self):
        if debugHSM:
            print (f'</ {self.name ()} >')
        self._state.exit ()
        if self._machineExit:
            self._machineExit ()

    def enterDefault (self):
        self._state = self.lookupState (self._defaultStateName)
        self.enter ()

    def reset (self):
        self.exit ()
        self.enterDefault ()

    def handle (self, message):
        if debugHSM:
            print (f'<handle {self.name ()} />')
        r = self._state.handle (message)
        assert r and (r == True or r == False)
        if not r:
            self.unhandledMessage (message)
        else:
            return True

    def next (self, nextStateName):
        self.exit ()
        self._state = self.lookupState (nextStateName)
        self.enter ()

    def run (self):
        while self.isBusy ():
            self.step ()
        while self.handleIfReady ():
            while self.isBusy ():
                self.step()


    # a raw state machine always completes a step when handle() is called
    # and is never busy
    # (This is different for composite state machines)
    def step (self):
        pass
    
    def isBusy (self):
        return False

    def wrapper (self):
        # the topmost HSM wraps all layers below it
        return self

    def unhandledMessage (self, message):
        raise Exception (f'unhandled message {message.port} in {self.name ()}')
                         
# worker bees
    def lookupState (self, name):
        for state in self._states:
            if state.baseName () == name:
                return state
        raise Exception (f'internal error: State /{name}/ not found in {self.baseName ()}') 
