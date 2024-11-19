class Person:
    def __init__(self, name, age, address):
        self.Name = name
        self.Age = age
        self.address = address
    
    def __str__(self):
        return f"{self.Name} {self.Age}"
    
p1 = Person("john", 30, "ktm")
print(p1)
# print(p1.Name)
# print(p1.Age)
# print(p1.address)


# object methods
class Person:
    def __init__(selfs, name, age, address):
        selfs.Name = name
        selfs.Age = age
    
    def myfunc(selfs):
        print("my name is " + selfs.Name)

    
p1 = Person("john", 30, "ktm")
p1.myfunc()

