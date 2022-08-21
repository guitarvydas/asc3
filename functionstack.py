class FunctionStack:
    def __init__ (self):
        self._stack = []

    def push (self, name, func):
        self._stack = self._stack.copy ()
        self._stack.insert (0, {'name':name, 'func':func})

    def call (self, name, param):
        f = self.findFirst (name, self._stack)
        if f:
            return f (param)
        else:
            return None

    def findFirst (name, stack):
        if (0 >= len (stack)):
            return None
        elif name == stack [0].name:
            return stack[0].func
        else:
            return self.findFirst (name, stack [1:])
    
            
