class Upward:
    def __init__ (self, parent, messageSender):
        self._parent = parent
        self._messageSender = messageSender

    def send (self, port, data, cause):
        if self._parent:
            self._parent.send (port, data, cause)
        else:
            self._messageSender.send (port, data, cause)
