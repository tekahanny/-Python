# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""


import string


def encrypt_message(value):
    new = value
    for i in value:
        if i == "y":
            index = value.index(i)
            y = "a"
            new = new[:index] + y + new[index+1:]
            
        elif i == "z":
            index = value.index(i)
            z = "b"
            new = new[:index] + z + new[index+1:]
        else:
            x =chr(ord(i) + 2)
            index = value.index(i)
            new = new[:index] + x + new[index+1:]
    return new

print("*********** encrypt message ***********")
print(encrypt_message("abc"))
print(encrypt_message("xyz"))
print(encrypt_message(""))

print("************ encrypt message 2 ************")


def encrypt_message2(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypt = ""
    for i in message:
        index = alphabet.index(i)
        encrypt_index = (index + 2) % 26
        encrypt += alphabet[encrypt_index]
        
    return encrypt

print(encrypt_message2("abc"))
print(encrypt_message2("xyz"))
print(encrypt_message2(""))

print("********** split method in a string *********")

def split_method(message):
    new_message = message.split(" ")
    message_again = ""
    for i in new_message:
        again_message = new_message.index(i)
        message_again = new_message[again_message]
        print(message_again)
    return again_message

print(split_method("I am learning how to code Python"))

# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]

def word_lengths(string):
    new_string = string.split(" ")
    each_word = []
    
    for i in new_string:
        each_word.append(len(i))

    return each_word
print("************ word length ***********")
print(word_lengths("Mary Poppins was a nanny"))
print(word_lengths("Somebody stole my donut"))

# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""

print("************ cleanup ************")

def cleanup(list_strings):
    if " "in list_strings:
        list_strings.remove(" ")
    if "" in list_strings:
        list_strings.remove("")
    together = ""
    together = " ".join(list_strings)
    return together

print(cleanup(["cat", "er", "pillar"]))
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "]) )

print("**************** zip function **********")

first = [1, 2, 3, 4, 5, 6]
second = [5, 4, 3, 2, 1, 6]
same = []

for f, s in zip(first, second):
    if f == s:
        same.append(f)
print(same)


# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0
print("************* nested sum ***********")

def nested_sum(numbers):
    value = 0
    for one in numbers:
        for two in one:
            value += two
            
    return value

print(nested_sum([[1, 2, 3], [4, 5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]]))   

# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""

print("************** fancy concatenate *************")

def fancy_concatenate(strings):
    value = ""

    for list_out in strings:
        for list_in in list_out:
            if len(list_out) == 3:
                value = value + list_in
            
    return value

print(fancy_concatenate([["A", "B", "C"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))
print(fancy_concatenate([["A", "B"], ["C", "D"]]) )


# Uncomment the commented lines of code below and complete the list comprehension logic

# The floats variable should store the floating point values 
# for each string in the values list.
values = ["3.14", "9.99", "567.324", "5.678"]
floats = [float(value) for value in values]
print(floats)

# The letters variable should store a list of 5 strings. 
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
name = "Boris"
letters = [char+char+char for char in name]
print(letters)

# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
lengths = [len(element) for element in elements]
print(lengths)

# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]

print("************* Destroy elements ************")

def destroy_elements(value1, value2):
    values = [value for value in value1 if value not in value2]
    return values

    

print(destroy_elements([1, 2, 3], [1, 2]) )
print(destroy_elements([1, 2, 3], [1, 2, 3]))
print(destroy_elements([1, 2, 3], [4, 5]) )

# To get list of squares of the values using
# 1) list comprehension
# 2) the map function

print("********* list comprehension ***********")

values = [3.45, 5.67, 7.89]



print([value ** 2 for value in values])

print("*********** map ************")

values = [3.45, 5.67, 7.89]

def square(val):
        return val ** 2


print(list(map(square, values)))
