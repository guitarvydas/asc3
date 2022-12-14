from porthandler import PortHandler
from leaf import Leaf
from procedure import Procedure

class Echo (Procedure):
    def f1 (self, message):
        self.send ('stdout', message.data, message)

    def __init__ (self, buildEnv, runEnv):
        h1 = PortHandler ('', self.f1)
        # buildEnv' = cons ([h1], buildEnv)
        buildEnvPrime = buildEnv.copy ()
        buildEnvPrime['handlerFunctions'] = [h1]
        # 
        super ().__init__ (buildEnv=buildEnvPrime, runEnv=runEnv)
