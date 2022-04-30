
# Python program to
# demonstrate private members
 
# Creating a Base class
 
 
class Base:
    def __init__(self):
        self.a = "1"
        self.__c = "2"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
 
 
# Driver code
obj1 = Base()
#obj2 = Derived()
print(obj1.a)
#print(obj2.__c)
#print(obj2.a)