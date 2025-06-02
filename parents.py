'''
Let A be an abstract base class with a method m() and a variable _v.

'Abstract parents pass their variables onto their concrete children'(from title) in case a child B, who inherits A, is implemented doing overlapping only on the method m(), not the variable _v. 
The title is true if and only if B._v is called succesfully, not throwing NameError.'''

from abc import abstractmethod, ABC

class Animal(ABC):
    
    def __init__(self):
        _v = 'vee'
        v = 'maybee'
    @abstractmethod
    def method(self):
        pass

#----
class Bee(Animal):

    def __init__(self):
        super().__init__

    def method(self):
        print('Doing something')
        return 'Doing something'

#----

#--Probing--
def probe():
    b = Bee()
    b.method()  # sanity check
    b.v
    b._v

#probe()


