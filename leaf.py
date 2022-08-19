from component import Component

class Leaf (Component):
    def __init__ (self, buildEnv, runEnv):
        super ().__init__ (buildEnv, runEnv)
        
    # a Leaf always completes a step when Handle() is called
    # and is never busy
    # (This is different for composite state machines)
    def step (self):
        pass
    
    def isBusy (self):
        return False

