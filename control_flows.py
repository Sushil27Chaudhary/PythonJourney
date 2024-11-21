# if statements
# x = int(input("please enter an integer: "))
# if x < 0:
#     # x = 0
#     print("negative changed to zero")
# elif x == 0:
#     print('zero')
# elif x == 1:
#     print('single')
# else:
#     print('More')

# for statements

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# create a sample collection
users = {
    'Hans': 'active', 
    'Éléonore': 'inactive', 
    '景太郎': 'active'
}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print("deleted user is:",user)

# Strategy:  Create a new collection
active_users = {}

for user, status in users.copy().items():
    if status == 'active':
        active_users[user] = status
        print(user)


# The range() Function
for i in range(2,10):
    print(i)

x = list(range(1,10))
print(x)

y = range(2,10)
print(y)

# sum
z = sum(range(4))
print('sum(range(4) is:',z)


# break and continue statement
for n in range(2,10):
    for x in range(2, n):
        if  n % x == 0:
            print (f"{n} equals {x} * {n//x}")
            break

# continue statement
for num in range(2,10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

# match statement
def http_error(status):
    match status:
        case 400:
            print("Bad request")
        case 401:
            print("Unauthorized")
        case 403:
            print("Forbidden")
        case 404:
            print("Not found")
        case _:
            print("Something went wrong")
http_error(4040)


from enum import Enum

class Color(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"  

# Get user input and ensure the input matches the expected values
user_input = input("Enter your choice of 'Red', 'Green', or 'Blue': ").capitalize()

# Try to match the user input with the enum
try:
    color = Color[user_input]  # Access the enum member by its name
    match color:
        case Color.RED:
            print("I see red", color)
        case Color.GREEN:
            print("I see green", color)
        case Color.BLUE:
            print("I see blue", color)
except KeyError:
    print("Invalid color choice!")


