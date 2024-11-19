thistuple = ("apple", "banana", "cherry")
# print(thistuple[:-1])

if "apple" not in thistuple:
    print("yes")
else:
    print("no")



# Change Tuple Values
x = ("apple", "banana", "cherry","dfd")
y = list(x)
y[3] = "kiwi"
x = tuple(y)
print(x)

# adding item to the tuples
x = ("apple", "banana", "cherry","dfd")
y = list(x)
y.append("mango")
x = tuple(y)
print(x)

x = ("apple", "banana", "cherry","dfd")
y = ("orange",)
x += y
print(x)

# remove() items
x = ("apple", "banana", "cherry","dfd")
y = list(x)
y.remove("dfd")
print(y)



# unpacking tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)

print()

# loop tuple
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
for x in range(len(fruits)):
    print(fruits[x])

print()

fruits = ("cat", "car", "banana", "realhuice", "beetroot")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# join tuple
tuple1 = ("cat", "car", "banana", "realhuice", "beetroot")
tuple2 = (True, False, True, False)

tuple3 = tuple1 + tuple2
print("Joining tuple", tuple3)

# mutipleof tuple 
tuple4 = tuple2*2
print(tuple4)


# tuple methods
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
tuplecount = thistuple.count(5)
tupleindex = thistuple.index(1)
print(tuplecount)


# List Comprehension in Python
string = "hello world"
upper_letter = [
    char.upper() for char in string if char.isalpha()
    ]
print(upper_letter)

original_list = [1, 2, 3, 4, 5]
doubled_list = [
    (lambda x : x * 2)(x) for x in original_list
]
print(doubled_list)

# Nested Loops in Python List Comprehension

list1=[1,2,3]
list2=[4,5,6]
CombLst=[(x,y) for x in list1 for y in list2] 
print (CombLst)

# Conditionals in Python List Comprehension
list1 = [x for x in range(1,100) if x%2==0]
print(list1)



# List Comprehensions vs For Loop

# Example Using For Loop

chars = []
for ch in 'TutorialsPoint':
    if ch not in 'aeiou':
        chars.append(ch)
print(chars)

# Example Using List Comprehension
listObj = [char for char in 'TutorialsPoint' if char not in 'aeiou']
print(listObj)