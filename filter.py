ages = [5, 12, 17, 18, 24, 32, 100]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myFunc, ages)
for x in adults:
    print(x)


# map() function
def mapFunc(n):
    return len(n)
x = map(mapFunc, ('apple','banana', 'cherry'))
print(x)
print(list(x))

print()

def myfunc(a, b):
  return a + b
x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)
#convert the map into a list, for readability:
print(list(x))
