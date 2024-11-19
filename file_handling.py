# file = open("example.txt", "r")
# print(file.read())

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("example.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line, end='')
#         line = file.readline()


# with open("example.txt", "w") as file:
#     file.write("jkfdfjkdjfdj")
#     print ("Content added Successfully!!")


# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open("example.txt", "w") as file:
#    file.writelines(lines)
#    print ("Content added Successfully!!")

# with open("example.txt", "w") as file:
#    file.write("This is an example using the with statement.")
#    print ("File closed successfully!!")


# try:
#    file = open("example.txt", "w")
#    file.write("This is an example with exception handling.")
# finally:
#    file.close()
#    print ("File closed successfully!!")   

# file = open("example.txt", "a")
# file.write("appending this line.\n")
# file.close()
# print("File opened successfully!!")


# fo = open("foo.txt", "w")
# fo.write("helllllllllll.\nohuuuuuuuuuu\n")
# fo.close()


# with open("foo.txt","wb") as f:
#     # binary data
#     date = b"Hello worlds"
#     f.write(date)

with open("foo.txt", "w") as f:
    text = "wowowoowowowowow"
    f.write(text)


import os
# current_name = "foo.txt"
# new_name = "newfilename.txt"
# os.rename(current_name,new_name)
# print(f"File'{current_name}' renamed to '{new_name}' successfully")

file1 = "newfilename.txt"
os.remove(file1)
print(f"'{file1}' deleted successfully")