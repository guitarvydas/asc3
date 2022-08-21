class Downward:
    def __init__ (self, child):
        self._child = child

    def reset (self):
        return self.down0 (reset)
        
    def step (self):
        return self.down0 (step)
        
    def isBusy (self):
        return self.down1 (isBusy, False)

    def isReady (self):
        return self.down1 (isReader, False)

    def run (self):
        return self.down0 (run)

    def handle (self, message):
        child = self._child
        r = self.handleChained (message)
        if ((not r) and child):
            r = child.handleChained (message)
        return r

# worker
    def down0 (self, func):
        child = self._child
        if child:
            return child.func ()
        else:
            return None

    def down1 (self, func, v1):
        child = self._child
        if child:
            return child.func ()
        else:
