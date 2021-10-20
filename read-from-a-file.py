# Reading a File with the open Function and read
# Method

# with open("cupcakes.txt", "r") as cupcakes_file:
#     print("The file has been opened")
#     content = cupcakes_file.read()
#     print(content)

# print("The file has been closed. We are outside the context block.")

# **************************************************************************

# Read file line by line

# filename = input("What file would you like to open? ")
# with open(filename, "r") as file_object:
#     print(file_object.read())

# with open("cupcakes.txt") as file_object:
#     for line in file_object:
#         print(line.strip())

# ****************************************************************************

# write to a file

# file_name = "my_first_file.txt"

# with open(file_name, "w") as file_object:
#     file_object.write("Hello file!\n")
#     file_object.write("You're my favorite file!")



# *******************************************************************************

# Append to a file

with open("my_first_file.txt", "a") as file_object:
    file_object.write("\nThird line is the best line!")


