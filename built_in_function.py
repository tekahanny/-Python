from typing import Counter


numbers = [4, 8, 15, 16, 23, 42]

l = []
i = 0
j = len(numbers) - 1
while i < j:
    l.append(numbers[j]) # l [42, 23]
    l.append(numbers[i]) # l [42, 23,]
    i = i + 1 # 1 , 2, 3
    j = j - 1 # 4 , 3, 2 s
    if i == j:
        l.append(numbers[i])
print(l)

print("*********************")

animals = ["cat", "bear", "zebra", "donkey", "cheetah"]
print(map(len, animals))
animal_list = [len(animal) for animal in animals]
print(animal_list)
print(list(map(len, animals)))

long_words = [animal for animal in animals if len(animal) > 5]
print(long_words)

def is_long_animal(animal):
    return len(animal) > 5

print(list(filter(is_long_animal, animals)))

print("*************** lambda ***********")
metals = ["gold", "silver", "platinum", "palladium"]

print(list(filter(lambda letter_p: "p" in letter_p, metals)))

print(list(map(lambda letter_l: letter_l.count("l"), metals)))
print(list(map(lambda word: word.replace("s", "$"), metals)))

# Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#
# EXAMPLES:
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3)     => ['cat', 'dog', 'ace']
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5)     => ['heart']
# right_words([], 4)                                         => []

print("************ right words ***********")

# def right_words(words, number):
#     value = []
#     for word in words:
#         if len(word) == number:
#              value.append(word)
#     return value

def right_words(words, number):
    return list(filter(lambda word: len(word) == number,words))

print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))
print(right_words([], 4))

# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#
# EXAMPLES:
# only_odds([1, 3, 5, 6, 7, 8])      =>  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])            =>  []

print("************** only odds *************")

# def only_odds(numbers):
#     odd = []
#     for number in numbers:
#         if number % 2 != 0:
#             odd.append(number)
#     return odd

def only_odds(numbers):
    return list(filter(lambda number: number % 2 != 0, numbers))

print(only_odds([1, 3, 5, 6, 7, 8]))
print(only_odds([2, 4, 6, 8]))

# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# EXAMPLES:
# count_of_a(["alligator", "aardvark", "albatross"])    => [2, 3, 2]
# count_of_a(["plywood"])                               => [0]
# count_of_a([])                                        => []

print("************ count of a ************")

# def count_of_a(strings):
#     value = []
#     for letter in strings:
#         value.append(letter.count("a"))
#     return value

def count_of_a(strings):
    return list(map(lambda letter: letter.count("a"), strings) )

print(count_of_a(["alligator", "aardvark", "albatross"]))
print(count_of_a(["plywood"]))
print(count_of_a([]) )

# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.
#
# EXAMPLES
# greater_sum([1, 2, 3], [1, 2, 4]) => [1, 2, 4]
# greater_sum([4, 5], [2, 3, 6])    => [2, 3, 6]
# greater_sum([1], [])              => [1]

print("**************** greater sum ***************")

def greater_sum(num1, num2):
    value = []
    if sum(num1) > sum(num2):
        value = num1
    else:
        value = num2

    return value

print(greater_sum([1, 2, 3], [1, 2, 4]))
print(greater_sum([4, 5], [2, 3, 6]))
print(greater_sum([1], []))

# Declare a sum_difference function that accepts two lists of numbers.
# It should return the difference between the sum of values in the first list and the second list
#
# EXAMPLES
# sum_difference([1, 2, 3], [1, 2, 4]) => 6 - 7 => -1
# sum_difference([4, 5], [2, 3, 6])    => 9 - 11 => -2
# sum_difference([1], [])              => 1

print("************** sum difference *************")

def sum_difference(num1, num2):
    return (sum(num1) - sum(num2))

print(sum_difference([1, 2, 3], [1, 2, 4]))
print(sum_difference([4, 5], [2, 3, 6]) )
print(sum_difference([1], []) )





