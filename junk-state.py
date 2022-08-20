class State:
    def __init__ (self, ownerMachine, enterFunction, exitFunction):
        runEnv = ownerMachine.runEnv ()
        buildEnv = ownerMachine.buildEnv.copy ()
        self._messageHandler = MessageHandler (buildEnv, runEnv)
        self._messageSender = MessageSender (buildEnv, runEnv)
        self._runnable = owner.runnable ()
        self._enter = enterFunction
        self._exit = exitFunction

    def enter (self):
        if self._enter:
            self._enter ()

    def exit (self):
        if self._exit:
            self._exit ()


class State:
    def __init__ (self, machine, name, enter, exit, handle, subMachineClass):
        self._machine = machine
        self._name = name
        self._enter = enter
        self._exit = exit
        self._handle = handle
        self._subMachineClass = subMachineClass
        self._subMachine = None

    def __repr__ (self):
        return f'<state {self.name}>'
    
    def enter (self):
        if self._subMachineClass:
            self._subMachine = self._subMachineClass (self.wrapper (), f'{self._subMachineClass.__name__}')
        self._enter ()
        
    def exit (self):
        if self._subMachine:
            self._subMachine.exit ()
        self._exit ()

    def handle (self, message):
        r = self._handle (message)
        if (not r):
            r = self.delegate (message)
        return r

    def name (self):
        subname = ''
        if self._subMachine:
            subname = ':' + self._subMachine.name ()
        return f'{self.baseName ()}{subname}'

    def baseName (self):
        return self._name

    def wrapper (self):
        return self._machine.wrapper ()

    def next (self, nextStateName):
        self._machine.next (nextStateName)

    def delegate (self, message):
        if self._subMachine:
            return self._subMachine.handle (message)
        else:
            return False

        
