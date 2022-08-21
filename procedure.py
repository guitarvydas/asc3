from hsm import HSM
from state import State

class Procedure:
    def __init (self, parent, handlerFunction):
        s = State (name='default', enter=None, handlerFunctions=[handlerFunction
], exit=None)
        eh = Eh ()
        down = Downward (None)
        up = Upward (eh)
        f = FunctionStack ()
        f.push ('reset', down.reset)
        f.push ('step', down.step)
        f.push ('isBusy', down.isBusy)
        f.push ('handle', down.handle)
        f.push ('isReady', down.isReady)
        f.push ('run', down.run)
        f.push ('send', up.send)
        f.push ('outputs', up.outputs)
        self._hsm = HSM (functions=f, defaultStateName='default', enter=None, states=[s], exit=None)

    
