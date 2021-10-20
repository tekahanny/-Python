# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#
# even_or_odd(2)    => "even"
# even_or_odd(0)    => "even"
# even_or_odd(13)   => "odd"
# even_or_odd(9)    => "odd"

'''
def even_or_odd(number):
    if number % 2:
        return "even"
    
    return "odd"
'''

def even_or_odd(integer):
    if integer % 2 == 0:
        return "even"
    if integer % 2 != 0:
        return "odd"

print(even_or_odd(2))
print(even_or_odd(0))
print(even_or_odd(13))
print(even_or_odd(9))


# Define a truthy_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value _____ is ______" 
# where the first space is the argument and the second space 
# is either 'truthy' or 'falsy'. See the sample invocations below.
# 
# truthy_or_falsy(0)        => "The value 0 is falsy"
# truthy_or_falsy(5)        => "The value 5 is truthy"
# truthy_or_falsy("Hello")  => "The value Hello is truthy"
# truthy_or_falsy("")       => "The value  is falsy"

'''
def truthy_or_falsy(value):
    if bool(value):
        return f"The value {value} is truthy"

    retun f"The value {value} is falsy"
'''
def truthy_or_falsy(value):
    if value:
        return "The value " + str(value) + " is truthy"
    if value == False:
        return "The value " + str(value) + " is falsy"
    if value == '':
        return "The value " + str(value) + " is falsy"

print(truthy_or_falsy(0))
print(truthy_or_falsy(5))
print(truthy_or_falsy("Hello"))
print(truthy_or_falsy(""))

# Declare a negative_energy function that accepts a numeric argument and returns its absolute value. 
# The absolute value is the number's distance from zero.
# 
# negative_energy(5)    => 5
# negative_energy(10)   => 10
# negative_energy(-5)   => 5
# negative_energy(-8)   => 8
# negative_energy(0)    => 0

def negative_energy(number):
    if number < 0:
        return number * -1
    elif number == 0:
        return "it is zero"
    else:
        return number

print(negative_energy(5))
print(negative_energy(10))
print(negative_energy(-5))
print(negative_energy(-8))
print(negative_energy(0))

# Define a divisible_by_three_and_four function that accepts a number as its argument. 
# It should return True if the number is evenly divisible by both 3 and 4 . 
# It should return False otherwise.
#
# divisible_by_three_and_four(3)   => False
# divisible_by_three_and_four(4)   => False
# divisible_by_three_and_four(12)  => True
# divisible_by_three_and_four(18)  => False
# divisible_by_three_and_four(24)  => True

'''
def divisible_by_three_and_four(number):
    return number % 3 == 0 and number % 4 == 0
'''

def divisible_by_three_and_four(number):
    if number % 3 == 0 and number % 4 == 0:
        return True
    else:
        return False


print(divisible_by_three_and_four(3))
print(divisible_by_three_and_four(4))
print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(18))
print(divisible_by_three_and_four(24))

# Declare a string_theory function that accepts a string as an argument. 
# It should return True if the string has more than 3 characters 
# and starts with a capital “S”. It should return False otherwise.
#
# string_theory("Sansa") => True
# string_theory("Story") => True
# string_theory("See") => False
# string_theory("Fable") => False

'''
def string_theory(string):
    len(string) > 3 and string[0] == 'S':
'''

def string_theory(string):
    if len(string) > 3 and string[0] == 'S':
        return True
    else: 
        return False

print(string_theory("Sansa"))
print(string_theory("Story"))
print(string_theory("See"))
print(string_theory("Fable"))

'''
FizzBuzz is a popular programming problem to test a developer's ability to think logically with code.

The problem is simple but deceptive.

Define a fizzbuzz function that accepts a single number as an argument. The function should print every number from 1 to that argument. 

There are a couple caveats.

If the number is divisible by 3, print "Fizz" instead of the number.

If the number is divisible by 5, print "Buzz" instead of the number.

If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.

If the number is not divisible by either 3 or 5, just print the number.
'''

def fizzBuzz(number):
    
    num = 1
    while number >= num:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
           
        num += 1

fizzBuzz(30)

# def reverse(str):
#     start_index = 0
#     last_index = len(str) -1
#     reverse_string = ""

#     while last_index >= start_index:
#         reverse_string += str[last_index]
#         last_index -= 1

#     return reverse_string

# print(reverse("thomas"))   

def reverse(str):
    if len(str) <= 1:
        return str

    return str[-1] + reverse(str[:-1])

print(reverse("thomasHanny"))


# Define a function called "factorial" that accepts a single number as input
#
# A factorial represents the product of all numbers up to, and including, that number. 
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120
#
# Return the factorial calculation from your function. You should NOT use any kind of loops. 
# Instead, utilize recursion. Your function MUST call itself.
# See sample inputs and return values below
#
# factorial(1) => 1
# factorial(2) => 2
# factorial(3) => 6
# factorial(4) => 24
# factorial(5) => 120

def factorial(number):
    if number == 1:
        return number

    return number * factorial(number - 1)

print(factorial(5))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))


