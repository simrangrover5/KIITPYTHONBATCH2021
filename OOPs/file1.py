from time import sleep

class Animal:
    def __init__(self, name, type_, color=None):
        self.name = name
        self.type = type_
        self.color = color
        
    def __repr__(self):
        return f"{self.name}"
    
    def __del__(self):
        print("\n My destructor is called.....")
        print("\n Deleting name ...")
        sleep(1)
        del self.name
        print("\n Deleting type ...")
        sleep(1)
        del self.type
        print('\n Deleting color ...')
        sleep(1)
        del self.color
            
obj1 = Animal("tuffy", "dog")
obj2 = Animal("kitty", "cat", "white")
print(obj1)
print(obj2)
del obj1  # __del__
# del obj1.name 
del obj2  # __del__
print(obj1)
