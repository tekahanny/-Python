
# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# EXAMPLES
# sum_of_lengths(["Hello", "Bob"])                  => 8
# sum_of_lengths(["Nonsense"])                      => 8
# sum_of_lengths(["Nonsense", "or", "confidence"])  => 20

def sum_of_lengths(strings):
    total = 0
    for value in strings:
        total += len(value)
    return total
print("sum of the string lengths")
print(sum_of_lengths(["Hello", "Bob"]))
print(sum_of_lengths(["Nonsense"]))
print(sum_of_lengths(["Nonsense", "or", "confidence"]) )

# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# EXAMPLES
# product([1, 2, 3])     => 6
# product([4, 5, 6, 7])  => 840
# product([10])          => 10

def product(numbers):
    total = 1
    for value in numbers:
        total *= value
    return total

print("product of numbers")
print(product([1, 2, 3]))
print(product([4, 5, 6, 7]))
print(product([10])) 

# A function that add only add numbrs from the list and return the odd numbers

values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]

def odds_sum(number):
    total = 0
    for i in number:
         if i % 2 != 0:
            total += i
    return total

print("sum of odd numbers ")
print(odds_sum(values))
print(odds_sum(other_values))

# A function that find the grates number from the list and return that number

def greatest_value(numbers):
    greatest = numbers[0]
    for i in numbers:
        if i > greatest:
            greatest = i
    return greatest

print("greatest")
print(greatest_value(values))
print(greatest_value(other_values))
print(greatest_value([3, 2, 1]))
print(greatest_value([-3, -2, -1]))

# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.
#
# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

def smallest_number(numbers):
    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i
    return smallest

print("Smallest")
print(smallest_number([1, 2, 3]))
print(smallest_number([3, 2, 1]))
print(smallest_number([4, 5, 4]))
print(smallest_number([-3, -2, -1]))

# Define a concatenate function that accepts a list of strings. 
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""

def concatenate(strings):
    conc = ""
    for i in strings:
        if len(i) >= 3:
            conc += i
    return conc

print("concatenated string")
print(concatenate(["abc", "def", "ghi"]))
print(concatenate(["abc", "de", "fgh", "ic"]))
print(concatenate(["ab", "cd", "ef", "gh"]))

# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter “s” in each word. 
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12




def super_sum(strings):
    num = 0
    for word in strings:
        if "s" in word:
            num += word.index("s",0,)
    return num      

print("Sum of the index positions of the first occurence of the letter s")
print(super_sum([]))
print(super_sum(["mustache"]))
print(super_sum(["mustache", "greatest"]))
print(super_sum(["mustache", "pessimist"]))
print(super_sum(["mustache", "greatest", "almost"]))

# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
#
# EXAMPLES
# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1

def in_list(strings, sep_string):
    for num, word in enumerate(strings):
        if sep_string in word:
            return num
    return -1
    

strings = ["enchanted", "sparks fly", "long live"]
print("Print index where the string exists in the list")
print(in_list(strings, "enchanted"))
print(in_list(strings, "sparks fly"))
print(in_list(strings, "fifteen") )
print(in_list(strings, "love story")) 

# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.
#
# EXAMPLES
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0

def sum_of_values_and_indices(numbers):
    total = 0
    for idx, num in enumerate(numbers):
        total = total + num + idx

    return total
 
print("sum of all of the elements along with their idex values")
print(sum_of_values_and_indices([1, 2, 3]))
print(sum_of_values_and_indices([0, 0, 0, 0]))
print(sum_of_values_and_indices([]))

