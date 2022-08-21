;; machine colour
λ(yellow:...).
 λ(green:...).
  λ(red:...).
   λ(machineEnter:noop).
    λ(machineExit:noop).
     λ(enterDefault:...).
      λ(next:...).
       λ(enterState:...).
	λ(exitState:...).
	 λ(reset:...).
	  λ(_outputq:FIFO()).
	   λ(send:fsend).
	    λ(outputs:foutputs).
		      ...
 (list
   (
yellow
green
red


def fsend (self, port, message, cause, env):
    env._outputq.enqueue (Message (port, message, cause))
def foutputs (self, env):
    list (env._outputq)

def fyellow (self).
    (
     enter:noop
     exit:noop
     handle:λ(message).next(green)
    )
