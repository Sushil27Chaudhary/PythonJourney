thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
print(thisdict)
print(len(thisdict))


thisdict1 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict1)

thisdict2 = dict(
    firstname = "john",
    lastname = "Doe"
    )
print(thisdict2)
x = thisdict2.get("lastname")
y = thisdict2["firstname"]
print(x,y)

z = thisdict2.keys()
print(z)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "white"

print(x) #after the changes


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)



# nested dictonaries
family = {
    "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(family)

child1 = {
    "name" : "Emil",
    "year" : 2004
}

child2 = {
    "name" : "Emil",
    "year" : 2004
}

child3 = {
    "name" : "Emil",
    "year" : 2004
}

myfamily ={
    "child1" : child1,
    "child2" : child2,
    "child3" : child3,
}
print("myfamily", myfamily)
# myfamily.clear()
# print(myfamily)