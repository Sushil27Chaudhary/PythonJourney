# Using % operator
name = "Tutorialspoint"
print("Welcome to %s" % name)

# using format() method
str = "Welcome to {}"
print(str.format("Tutorialspoint"))


strs = "Ssuhil {}"
print(strs.format("chaudhary"))

# Using f-string
item1 = 2400
item2 = 2405
total = f'Total: {item1+item2}'
print(total)
