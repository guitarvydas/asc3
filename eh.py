from messagesender import MessageSender
from runnable import Runnable

class EH:
    def __init__ (self, protoEnv, dynamicEnv):
        self._messageSender = MessageSender ()
        self._runnable = Runnable (protoEnv, dynamicEnv)
        self._hsm = HSM (self._messageSender, self._runnable)

    def reset (self):
        return self._hsm.reset ()

    def step (self):
        return self._hsm.step ()

    def isBusy (self):
        return self._hsm.isBusy ()

    def handle (self, message):
        return self._hsm.handle (message)

    def isReady (self):
        return self._hsm.isReady ()

    def outputs (self):
        return self._messageSender.outputs ()

    def inject (self, message):
        return self._hsm.inject (message)
