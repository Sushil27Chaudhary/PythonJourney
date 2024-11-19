thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))
print("Lenght of 'thisset' :", len(thisset))
print("banana" in thisset)
print("banana" not in thisset)

# set constructor

set1 = set(("apple","toyota","dog",True,1))
# set1 = {"abc", 34, True, 40, "male"}
print(set1)



# adding items to the set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


set2 = {"apple", "banana", "cherry"}
set3 = {"pineapple", "mango", "papaya"}
set2.update(set3)
print(set2)

set2.remove("apple")
set2.discard("orange")
print(set2)


# difference_update()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)