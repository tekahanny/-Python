# Create an empty dictionary and assign it to the variable empty.

# Create a dictionary with three key-value pairs. 
# The keys should be strings and the values should be integer values. 
# Assign the dictionary to a my_dict variable.

# A dictionary’s keys can be any immutable data structure. 
# Create a dictionary with two key-value pairs and assign it to
# a winning_lottery_numbers variable. 
# Both of the keys should be tuples. 
# One of the values should be True, the other value should be False.

from typing_extensions import IntVar


print("************ Dictionaries **********")

empty = {}

my_dict = {
    "Hanny": 31,
    "Thomas": 34,
    "George": 30
}

winning_lottery_numbers = {
    (12345,): True,
    (34567,): False
}

print(empty)
print(my_dict)
print(winning_lottery_numbers)

# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#
# EXAMPLE:
# detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}
print()

print("**************** to dictionary function *****************")

# def to_dictionary(strings):
#     dic_strings = {}
    
#     for word in strings:
#         dic_strings[word] = strings.index(word)

#     return dic_strings

def to_dictionary(elements):
    results = {}

    for index, element in enumerate(elements):
        results[element] = index

    return results


detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
print(to_dictionary(detectives))

# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 
# 2 strings with 7 letters, and 1 string with 4 letters.
print()
print("*************** length counts ************")

# def length_counts(strings):
#     words = {}
#     length = 0

#     for word in strings:
#         length = len(word)
#         if length in words:
#             words[length] += 1
#         else:
#             words[length] = 1

#     return words

def length_counts(elements):
    counts = {}

    for element in elements:
        length = len(element)
        current_count = counts.get(length, 0)
        counts[length] = current_count + 1
    
    return counts



sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
print(length_counts(sa_countries))

# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings. 
# For each string in the list, if the string exists as a dictionary key, 
# delete the key-value pair from the dictionary. 
#
# If the string does not exist as a dictionary key, avoid an error. 
# The return value should be the modified dictionary object.
#
# EXAMPLE:
# my_dict = {
#   "A": 1,
#   "B": 2,
#   "C": 3
# }
#
# strings = ["A", "C"]
# delete_keys(my_dict, strings) => {'B': 2}

print()
print("*************** delete keys ***********")

def delete_keys(keys, values):
    for value in values:
        if value in keys:
            keys.pop(value)

    return keys

my_dict = {
  "A": 1,
  "B": 2,
  "C": 3
}

strings = ["A", "C"]
print(delete_keys(my_dict, strings))


# dict function
print()
print("************ dict function ************")

hanny_family = [
    ["Absalat", "daugther"],
    ["Yohannes", "son"],
    ["Thomas", "husband"],
    ["Aynalem", "mother"],
    ["Abebe", "father"]
]

adey_family = [
    ["Ariam", "daugther"],
    ["Mariamwit", "daughter"],
    ["Melaku", "husband"],
    ["Aynalem", "mother"],
    ["Abebe", "father"]
]

change_hanny = dict(hanny_family)
change_adey = dict(adey_family)
print(change_hanny)

hanny_adey = change_hanny.update(change_adey)
print()
print(change_adey)

family = {
    "Abebe_Aynalem":{
        "Son":{
            "first": "Abidela",
            "second": "Tadiwose",
            "third": "Semeone"
        },
        "Daughter": {
            "first": "Zelalem",
            "second": "Muna",
            "third": "Metasebia",
            "fourth": "Adey",
            "fifth": "Hanny"
        }
    },
    "Abidela_Sindu":{
        "first": "Niba",
        "second": "Yafite"
    }
}

print()
print("*********** nested dictionaries ***********")

print(family["Abidela_Sindu"]["first"])

# update

print()
print("************ update ************")

d1 = {
    "a": 5,
    "b": 10,
    "c": 5
}

d2 = {
    "a": 8,
    "b": 12,
    "d": 16
}

d1.update(d2)
print(d1)
# d1.pop("f1")

# get and setdefault methods

print()
print("*********** get and setdefult methods ************")

hanny = {
    "mother": "Aynalem",
    "father": "Abebe"
}

hanny.setdefault("daugther", "Absalat")
print(hanny)

x = hanny.get("husband", "Thomas")
print(x)


# Write the syntax to access the value of 20 from within this nested data structure.

nba_finals = {
  "Game 1": {
    "date": "05/05/2019",
    "location": "San Francisco",
    "statistics": {
      "points": 200,
      "rebounds": 20,
      "assists": 25
    }
  }
}


print()
print("************ syntax ********** ")     

print(nba_finals["Game 1"]["statistics"]["rebounds"])

# How many key-value pairs does the top-level dictionary hold?
my_dict = {
  "a": {
    1: 2,
    3: 4,
    5: {
      6: 7,
      8: 9
    }
  }
}

# What will the mystery dictionary look like after the code below? Write out the complete object.

mystery = {
    "a": 2
}
mystery.setdefault("A", 5)
print(mystery)
mystery.setdefault("a", 10)
print(mystery)
mystery.setdefault("B", 30)
print(mystery)
mystery.setdefault("B", 40)
print(mystery)

print()
print("********** iterate over dictionary with a for loop ***************")

pound_to_kilograms = {
    5: 2.26796,
    10: 4.53592,
    25: 11.3398
}

# 5 pounds is equal to 2.26796 kilograms

for weight in pound_to_kilograms:
    print(f"{weight} pounds is equal to {pound_to_kilograms[weight]} kilograms")


# Declare an invert function that accepts a dictionary object. 
# The function should return a new dictionary where the keys and values from the original dictionary are inverted. 
# Each key should now be a value, and each value should be a key. 
# Assume both the keys and values of the dictionary are immutable.
#
# EXAMPLE:
# my_dict = {
#   "A": "B", 
#   "C": "D",
#   "E": "F"
# }
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}

print()
print("******** invert function ***********")

def invert(dic_object):
    invert_dic = {}

    for key, value in dic_object.items():
        invert_dic.setdefault(value, key)
    return invert_dic

my_dict = {
  "A": "B", 
  "C": "D",
  "E": "F"
}
print(invert(my_dict)) # => {'B': 'A', 'D': 'C', 'F': 'E'}

# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears 
# as a value among the dictionary’s values.
#
# EXAMPLE:
# my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1

print()
print("************** count of value function **************")

def count_of_value(dic, integer):
    count = 0
    for _, number in dic.items():
        if number == integer:
            count += 1
    return count

my_dict = { "a" : 5, "b" : 3, "c" : 5 }

print(count_of_value(my_dict, 5)) # => 2
print(count_of_value(my_dict, 3)) # => 1

# Declare a sum_of_values function that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary 
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# EXAMPLES:
# my_dict = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])            => 5
# sum_of_values(my_dict, ["a", "c"])       => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])            => 0

print()
print("************ sum of values **************")

def sum_of_values(dic_value, list_strings):
    sum_value = 0

    for key, value in dic_value.items():
        if key in list_strings:
            sum_value += value

    return sum_value

my_dict = { "a": 5, "b": 3, "c": 10 }

print(sum_of_values(my_dict, ["a"])) #            => 5
print(sum_of_values(my_dict, ["a", "c"])) #       => 15
print(sum_of_values(my_dict, ["a", "c", "b"])) #  => 18
print(sum_of_values(my_dict, ["z"])) #            => 0

# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }
#
# common_elements(my_dict) => ["A", "D"]

print()
print("************* common elements function ***********")

def common_elements(dic_element):
    common = []
    i = 0
    for key in dic_element.keys():
        if key in dic_element.values():
            common.insert(i,key)
            i += 1

    return common

my_dict = {
   "A": "K",
   "B": "D",
   "C": "A",
   "D": "Z"
 }

print(common_elements(my_dict)) # => ["A", "D"]



