from pipelinecomponent import PipelineComponent

from echo import Echo

class HelloWorld (PipelineComponent):
    def __init__ (self, parent, name, data):
        step1 = { 'clss' : Echo, 'name' : f'h1[{name}]', 'instanceData' : 'hello' }
        pipeline = [step1,]
        super ().__init__ (parent, name, data, pipeline)
