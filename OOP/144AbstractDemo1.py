from abc import ABC,abstractmethod     #(ABC = Abstract Base Class)

class Base(ABC):
    
    @abstractmethod
    def Addition(self,No1,No2):
        pass

class Derived(Base):
    pass

dobj = Derived()        #Error