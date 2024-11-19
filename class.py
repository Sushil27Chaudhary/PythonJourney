# defing a class

# class Smartphone:
#     # constructor
#     def __init__(self, device, brand):
#         self.device = device
#         self.brand = brand
    
#     # method of the class
#     def description(self):
#         return f"{self.device} of {self.brand} supports android 14"

# # creating object of the class
# phoneObj = Smartphone("Smartphone", "Samsung")
# print(phoneObj.description())



# example 2
# class UserDetails:
#     # constructor 
#     def __init__(self, name, address, age):
#         self.name =  name
#         self.address = address
#         self.age = age
    
#     # method
#     def result(self):
#         return f"{self.name} is live in {self.address} and his/her age is {self.age}"
    
# # creating object of the class
# detailObj = UserDetails("Ram", "Kathmanddu", 39)
# print(detailObj.result())



# Encapsulation
class Desktop:
   def __init__(self):
      self.__max_price = 25000
      self.abc = 349995

   def sell(self):
      return f"Selling Price: {self.__max_price}"

   def set_max_price(self, price):
      if price > self.__max_price:
         self.__max_price = price

# Object
desktopObj = Desktop()
print(desktopObj.sell()) 

# modifying the price directly
desktopObj.__max_price = 3500065
desktopObj.ram = "kjsjdfkjkl"
print(dir(desktopObj))

print(desktopObj.ram)
print(desktopObj.sell()) 

# modifying the price using setter function
desktopObj.set_max_price(35000)
print(desktopObj.sell()) 