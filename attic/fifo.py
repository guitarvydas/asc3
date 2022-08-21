# queues.py

from collections import deque

class FIFO:
    def __init__(self):
        self._elements = deque()

    def asDeque (self):
        return self._elements
    
    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

    def len (self):
        return len (self._elements)

    def isEmpty (self):
        return (0 >= len (self._elements))
