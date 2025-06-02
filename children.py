'''
In: :!python3 parents.py
Out:

Traceback (most recent call last):
  File "/home/qvd/Git/ZZ-do-abstract-parents-pass-their-variables-onto-their-children/parents.py", line 32, in <module>
    b._v
AttributeError: 'Bee' object has no attribute '_v'

'''
# Note Im afraid I mistook the error alias, lol /lh. It seems children will not simply take things from their abstract parents.  



#from parents import *  # commented out
from parents_correction import *  # differs from 'import parents_correction'



#--Reimplementing--
class Bee(Animal):
    def __init__(self):
        print('Bzzz bzzz... a wild bee appears.')

    @property
    def v(self):
        self._v = Animal._v 

        # In self.v = Animal._v
        # Out AttributeError: property 'v' of 'Bee' object has no setter. Did you mean: '_v'?

        # In self.v = super()._v
        # Out AttributeError: 'super' object has no attribute '_v'

        # In self.v = _v
        # Out NameError: name '_v' is not defined



    def method(self):
        print('Doing something')
        return 'Doing something'

#----


#--Probing--
b = Bee()
b.method()
# In b.v
# Out [Nothing, empty string. Silent error?]
print(b._v)

# Output: vee
'''
Finally we made it, the variable was acquired without throwing anything.
This means:... 
**NO**, abstract parents do not pass their variables on. Though this does not mean abstract classes withhold their variables from their children - a child just needs to reach out and ask.
It can be done through localized access (imprecise name) in the form of:...

'self._v = A._v'

'''






