# Given the great_directors list below, overwrite the “Steven Spielberg” string with a string of “Michael Bay”.
great_directors = ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]

great_directors[1] = "Michael Bay"
print(great_directors)

# Given the transformers list below, overwrite “Bumblebee” with “Grimlock”.
transformers = ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"]

transformers[2] = "Grimlock"
print(transformers)


# Given the camping_trip_supplies list below, overwrite "Socks" with "Food".
camping_trip_supplies = ["Socks", "Flashlight", "Tent", "Blanket"]

camping_trip_supplies[0] = "Food"
print(camping_trip_supplies)


# Given the tech_companies list below, overwrite the Microsoft, Blueberry, and IBM strings 
# with the strings “Facebook” and “Apple”. Use list slicing syntax.
tech_companies = ["Google", "Microsoft", "Blackberry", "IBM", "Yahoo"]

tech_companies[1:4:1] = ["Facebook", "Apple"]
print(tech_companies)


# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# EXAMPLES
# length_match(["cat", "dog", "kangaroo", "mouse"], 3))  => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5))  => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4))  => 0
# length_match([], 5))                                   => 0

def length_match(listStrings, number):
    count = 0
 
    for i in listStrings:
        if len(i) != number:
            continue
        else:
            count += 1

    return count       
        

print("*******************Length match ******************")
print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))  
print(length_match([], 5))                                   

# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# EXAMPLES
# sum_from(1, 2)   # 1 + 2                  => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5      => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8  => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12       => 42

def sum_from(number1, number2):
    total = 0
    while number2 > number1 or number1 == number2 :
        print("Current variable value: ", number1)
        total += number1
        number1 = number1 + 1
    
        if number1 > number2:
            break
    return total

print("*************** sum from ***************")
print(sum_from(9, 12))


# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# EXAMPLES
# same_index_values([1, 2, 3], [3, 2, 1])                         => [1]
# same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])   => [1, 3]

# value1[0] == value2[0] ==> 1 = 3 no
# value[1] == value[1] ==> 2 = 2 yes  ==> same[1] = index.value1(value[1])

def same_index_values(list1, list2):
    results = []

    for index, value in enumerate(list1):
        if value == list2[index]:
            results.append(index)

    return results        


print("************ same index values ***********")  
print(same_index_values([1, 2, 3], [3, 2, 1]))
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))



powerball_numbers = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    results = []
    for i in numbers:
        results.append(i * i)

    return results    

print("********** square **********")
print(squares(powerball_numbers)) # [16, 64, ...]


def convert_to_floats(numbers):
    results = []
    for i in numbers:
        num = float(i)
        results.append(num)

    return results

print("*********** conver to floats *******")
print(convert_to_floats(powerball_numbers))

def even_or_odd(numbers):
    value = []
    for i in numbers:
        if i % 2 == 0:
            value.append(True)
        else:
            value.append(False)

    return value

print("*********** even or odd ********")
print(even_or_odd(powerball_numbers))

# Define an only_evens function that accepts a list of numbers. 
# It should return a new list consisting of only the even numbers from the original list.
#
# EXAMPLES
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5])              => []
# only_evens([])                     => []

def only_evens(numebrs):
    result = []
    for i in numebrs:
        if i % 2 == 0:
            result.append(i)

    return result

print("*********** only even *********")
print(only_evens([4, 8, 16, 42]))
print(only_evens([1, 3, 5]))
print(only_evens([]))

# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []

def long_strings(strings):
    result = []
    for i in strings:
        if len(i) == 5 or len(i) > 5:
            result.append(i)

    return result

print("************ long strings *********")
print(long_strings(["Hello", "Goodbye", "Sam"]))
print(long_strings(["Ace", "Cat", "Job"]))
print(long_strings([]))

# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#
# EXAMPLES
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]

def factors(number):
    result = []
    value = range(1, number + 1)
    for i in value:
        if number % i == 0:
            result.append(i)

    return result

print("********** A positive whole number *********")
print(factors(1) )
print(factors(2))
print(factors(10))
print(factors(64))

# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it
#
# EXAMPLES
# delete_all([1, 3, 5], 3)  => [1, 5]
# delete_all([5, 3, 5], 5)  => [3]
# delete_all([4, 4, 4], 4)  => []
# delete_all([4, 4, 4], 6)  => [4, 4, 4]

def delete_all(strings, targets):
    while targets in strings:
        if targets in strings:
            strings.remove(targets)
    return strings

print("********** delete all *******")
print(delete_all([1, 3, 5], 3))
print(delete_all([5, 3, 5], 5))
print(delete_all([4, 4, 4], 4))
print(delete_all([4, 4, 4], 6))

# Declare a push_or_pop function that accepts a list of numbers
# Build up and return a new list by iterating over the list of numbers
# If a number is greater than 5, add it to the end of the new list
# If a number is less than or equal to 5, remove the last element added to the new list
# Assume the order of numbers in the argument will never require removing from an empty list
#
# EXAMPLES
# push_or_pop([10])            => [10]
# push_or_pop([10, 4])         => []
# push_or_pop([10, 20, 30])    => [10, 20, 30]
# push_or_pop([10, 20, 2, 30]) => [10, 30]

def push_or_pop(numbers):
    val = len(numbers)
    new = []
    for i in numbers:
        if i > 5:
            new.append(i)
        elif(i <= 5):
            new.pop(-1)
    return new

print("*********** push or pop ***********")
print(push_or_pop([10]))
print(push_or_pop([10, 4]) )
print(push_or_pop([10, 20, 30]))
print(push_or_pop([10, 20, 2, 30]))

# overwrite the values 4 and 5 with 6 and 8
numbers = [1, 4, 5, 7, 9]

if 4 in numbers and 5 in numbers:
    index1 = numbers.index(4)
    index2 = numbers.index(5)

    numbers.pop(index1)
    numbers.insert(index1, 6)

    numbers.pop(index2)
    numbers.insert(index2, 8)

print("************ Overwrite ****************")
print(numbers)




