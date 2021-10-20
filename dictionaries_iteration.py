# Assign a list of four dictionaries to a "complexity" variable below

# The first and third dictionaries should have two key-value pairs
# For those dictionaries, the keys should be strings and the values should be Booleans

# The second and fourth dictionaries should have three key-value pairs
# For those dictionaries, the keys shoulds be floats and the values should be list of strings. 
# The lists can be of any length.

print("************* Nested Data Structures ***********")

complexity = [
    {"John age is 31": True, "his weight is 56": False},
    {23.45: ["value", "price", "length"], 45.02: ["value", "price", "length"], 34.21: ["value", "price", "length"]},
    {"Anna age is 20": False, "her weight is 60": True},
    {40.23: ["strength", "temperature", "result"], 34.09: 
        ["strength", "temperature", "result"], 20.0: ["strength", "temperature", "result"]}
]


for four in complexity:
    for key, value in four.items():
        print(f"{key} , {value}")



# Declare a plenty_of_arguments function that accepts two parameters (a and b)
# and an additional **kwargs parameter.
#
# The function should return True if the sum of a, b, and the values of 
# **kwargs is greater than 100. It should return False otherwise.
#
# EXAMPLES:
# plenty_of_arguments(20, 30)                          => False
# plenty_of_arguments(a = 50, b = 75)                  => True
# plenty_of_arguments(a = 50, b = 25, c = 50)          => True
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)  => False
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)  => True

print()
print("************* keyword Arguments *************")

def plenty_of_arguments(a, b, **kwargs):
    return (a + b) + sum(kwargs.values()) > 100
        

print(plenty_of_arguments(20, 30))
print(plenty_of_arguments(a = 50, b = 75))
print(plenty_of_arguments(a = 50, b = 25, c = 50))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 25))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26))

hanny = "hanny is beautiful hello"
print(len(hanny.split(" ")))

values = [1, 2, 3, 4, 5]
print({ value: sum(values[:index + 2]) for index, value in enumerate(values) })

prices = {
  "Big Mac": 3.99,
  "French Fries": 0.99,
  "Soda": 0.99
}

calories = {
  "Big Mac": 600,
  "French Fries": 300,
  "Soda": 200
}
 
cheap_options = {meal: calories[meal] for meal, price in prices.items() if price < 1}
print(cheap_options)

# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
# channels = {
#   2: "CBS",
#   4: "NBC",
#   5: "FOX",
#   7: "ABC"
# }
# The stations_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers
#
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}

print()
print("************ Dictionary Comprehensions *************")

def stations_to_numbers(channels):
    channels_invert = {value: key for key, value in channels.items()}
        
    return channels_invert

channels = {
  2: "CBS",
  4: "NBC",
  5: "FOX",
  7: "ABC"
}
print(stations_to_numbers(channels))

# Declare a coaster_conversion function that accepts a dictionary
# The keys of the dictionary will be strings representing roller coasters
# The values will be the heights of each coaster in meters
#
# Return a new dictionary with the same keys.
# The values should be the heights converted from meters to feet,
# The final values (in feet) should also be rounded to the closest integer
# HINT: 1 meter is equal to 3.28084 feet
# HINT: The round function rounds a number to the nearest integer
#
# coasters = {
#   "Kingda Ka": 139,
#   "Top Thrill Dragster": 130,
#   "Superman: Escape From Krypton": 126
# }
#
# coaster_conversion(coasters) => {'Kingda Ka': 456, 'Top Thrill Dragster': 426, 'Superman: Escape From Krypton': 413}

print()
print("*************** coster conversion ***********")

def coaster_conversion(coasters):
    new_coasters = {key: round(value * 3.28084) for key, value in coasters.items()}

    return new_coasters

coasters = {
  "Kingda Ka": 139,
  "Top Thrill Dragster": 130,
  "Superman: Escape From Krypton": 126
}
print(coaster_conversion(coasters))

# Given the list below, write a dictionary 
# comprehension to return a dictionary where the keys are the numbers 
# and the values are their cubes. The dictionary should only use the numbers 
# that are even.

print()
print("*********** dictionary comprehension *********")
numbers = [3, 6, 7, 12, 15]
numbers_dic = {number: number**3 for number in numbers if number % 2 == 0}

print(numbers_dic)




prices = { "banana": 1.57, "orange": 2.56, "apple": 5.65, "strawberry": 6.27 }
print(prices.items())

new_prices = prices.items()
prices["apple"] = 4.45

print(new_prices)



