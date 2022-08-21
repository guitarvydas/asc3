class StateDescriptor:
    def __init__ (self, kind, ownerMachine, enterFunction, handleFunction, exitFunction):
        self._kind = kind
        self._ownerMachine = ownerMachine
        self._enter = enterFunction
        self._handle = handleFunction
        self._exit = exitFunction
