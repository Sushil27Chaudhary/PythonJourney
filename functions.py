def my_function():
  print("Hello from a function")
my_function()


def my_function(fname,lname, age):
  print(fname + " Refsnes " + lname, age)
my_function("john", "chaudhary", 303)
# my_function("john")
# my_function("john")


def info(fnames, lnames):
  print(fnames + " " + lnames)
info("john", "doe")


# Arbitrary Arguments, *args
def my_function(*kids):
  print("childs are:"+kids[0])
#   print("The youngest child is :"+",".join(kids))

my_function("Emil", "Tobias", "Linus")


def my_function(child1,child2,child3):
  print("the youngest child is "+child3)

my_function(child1="child1", child2 = "child1", child3 = "child3")


# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["fname"]+ "," + kid["lname"])
my_function(fname = "alexa", lname = "johnson")


def fruits_fun(**fruits):
  print("Fruits are:" + fruits["fruit1"]+ "," + fruits["fruit2"]+ "," + fruits["fruit3"]+ "," + fruits["fruit4"])
fruits_fun(fruit1="apple",fruit2="banana",fruit3="avogandu",fruit4="watermelon")


# Default Parameter Value
def country_func(country = "Nepal"):
  print("I am from " + country)
country_func("India")
country_func("Pakistan")
country_func("Bangladesh")
country_func()


# Passing a List as an Argument
def my_func(food):
  for key, value in food.items():
    print(f"{key}: {value}")

fruits = {
  "name" : "apple",
  "color" : "red",
  "weight" : "10gm"
}
my_func(fruits)



# Positional-Only Arguments
# example 1
def intr(amt, rate , /):
  val = amt * rate / 100
  return val
print(intr(316200, 4))


# example 2
# def intr(amt, rate, /):
#   val = amt * rate / 100
#   return val
# print(intr(amt = 316200, rate = 4))

# Example 3
def myfunction(x, /, y, *, z):
  print(x, y, z)
myfunction(10, y = 20, z = 30)
myfunction(10, 20, z = 30)


# Arbitrary Arguments (*args)
# Arbitrary Arguments Example

def add(*args):
  s = 0
  for x in args:
    s = s+x
  return s
result = add(10,20,30,40)
print(result)
result = add(1,2,3)
print(result)

# Required Arguments With Arbitrary Arguments

def avg(first, *rest):
   second=min(rest)
   return (first+second)/2
result=avg(30,4,10,3)
print (result)


# Arbitrary Keyword Arguments (**kwargs)
def address(**kwargs):
  for k,v in kwargs.items():
    print("{}:{}".format(k,v))
print("pass two keyword args")
address(name="John", city="Mumbai")
address(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001", CIN="400001")


# Multiple Arguments With Arbitrary Keyword Arguments
def percent(math, sci, **opt):
  print("maths", math)
  print("science", sci)
  s = math + sci
  for k,v in opt.items():
    print("{}:{}".format(k,v))
    s = s + v
    print(s)
  return s/(len(opt)+2)

result = percent(math=39, sci=49, eng=48, hist=29, nepali = 29)
print("percentage:", result)

# Python Variable Scope
# local variable
def myfunction():
  a = 10
  b = 20
  print("variable a:", a)
  print("variable b:", b)
  return a + b
print(myfunction())

# global variables
name = 'TutorialsPoint'
marks = 50 
def myfunction():
  # accessing inside the function
  print("name:", name)
  print("marks:", marks)
# fucntion call
myfunction()

# python modules
import math as maths
print ("Square root of 100:", maths.sqrt(100))
import platform
print(platform.system())


# lambda function
x = lambda a: a + 10 
print(x(5))

x = lambda a, b : a * b
print(x(5,6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunct(n):
  return lambda a : a * n
mydoubler = myfunct(2)
print(mydoubler(11))


def myfucn(n):
  return lambda a : a * n
x = myfucn(4)
print(x(3))