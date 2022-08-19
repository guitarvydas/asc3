from component import Component

class Leaf (Component):
    def __init__ (self, buildEnv, runEnv):
        super ().__init__ (buildEnv, runEnv)
        
    def run (self):
        while self.isBusy ():
            self.step ()
        while self.handleIfReady ():
            while self.isBusy ():
                self.step()


    # a Leaf always completes a step when Handle() is called
    # and is never busy
    # (This is different for composite state machines)
    def step (self):
        pass
    
    def isBusy (self):
        return False

# worker bees
    def handleIfReady (self):
        if self.isReady ():
            m = self.dequeueInput ();
            self.Handle (m)
            return True
        else:
            return False
    
