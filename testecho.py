from message import Message

from echo import Echo

# {},{} =>
#  λ(buildEnv,runEnv).
#   lifoPrepend({'name':'echo tester'},buildEnv),runEnv =>
#     λ(buildEnv,runEnv).
#       buildEnv, lifoPrepend({'parent':None},runEnv) =>
#         λ(buildEnv,runEnv).
#           buildEnv, lifoPrepend({'instanceName':'instanceE'},runEnv) =>
#             λ(buildEnv,runEnv).
#               Echo (buildEnv, runEnv) =>
#                 λ (e).
#                   e.inject (Message (None, '', '', None)
#                   print ('injected')
#                   e.run () => 
#                     λ (outputs).
#                       print ('done:')
#                       print (outputs)
#
# N.B. lifoPrepend () == cons ()
#
buildEnv = {'name': 'echo tester'} 
runEnv = {'parent': None, 'instanceName': 'instanceE', }

h = Echo (buildEnv, runEnv)
h.inject (Message (None, '', 'hello', None))
print ('injected')
outputs = h.run ()
print ('done:')
print (h.outputs ())

w = Echo (buildEnv, runEnv)
w.inject (Message (None, '', 'world', None))
print ('injected')
outputs = w.run ()
print ('done:')
print (w.outputs ())
