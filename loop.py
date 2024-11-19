# i = 1
# while i <= 6:
#     print(i)
#     i +=1

# break statement
j = 0 
while j < 10:
    print(j)
    if j == 7:
        break
    j += 1

print()

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print()

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")



# for loop
fruits = ["apple","banana","grapes"]
for x in fruits:
   print(x)
   if x == "banana":
    break