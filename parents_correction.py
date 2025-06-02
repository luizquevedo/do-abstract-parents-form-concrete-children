'''
A dire mistake was implemented.
ABCs will not have __init__ called. So this file is almost the same as parents.py, with a correction.'''



from abc import abstractmethod, ABC

class Animal(ABC):
    
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

