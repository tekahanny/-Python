# Declare a months tuple with the last 4 months of the year (September, October, November, December) as strings.
# Make sure the first letter of each month is capitalized.


# Create a faves variable with a list of your 3 three favorite movies as strings. 
# Use the tuple function to convert the list to a tuple and save the result in a movies variable.


# Create a numbers_a, numbers_b, and numbers_c tuple. 
# Each tuple should contain 3 integers. 
# Declare an all_numbers tuple containing these three tuples.

months = ("September", "October", "November", "December")
faves = ["Titanic", "A walk to remember", "Save the last dance"]

movies = tuple(faves)
print(movies)

numbers_a = (1, 2, 3)
numbers_b = (4, 5, 6)
numbers_c = (7, 8, 9)

all_numbers = (numbers_a, numbers_b, numbers_c)

print(all_numbers)


# Given the tuple below, destructure the three values and
# assign them to position, city and salary variables
# Do NOT use index positions (i.e. job_opening[1])
job_opening = ("Software Engineer", "New York City", 100000)

position, city, salary = job_opening

# Given the tuple below, 
# - destructure the first value and assign it to a street variable
# - destructure the last value and assign it to a zip_code variable
# - destructure the middle two values into a list and assign it to a city_and_state variable
address = ("35 Elm Street", "San Francisco", "CA", "94107")

street, *city_and_state, zip_code = address

# Declare a sum_of_evens_and_odds function that accepts a tuple of numbers.
# It should return a tuple with two numeric values:
# -- the sum of the even numbers
# -- the sum of the odd numbers.
#
# sum_of_evens_and_odds((1, 2, 3, 4))   => (6, 4)
# sum_of_evens_and_odds((1, 3, 5))      => (0, 9)
# sum_of_evens_and_odds((2, 4, 6))      => (12, 0)(

# def sum_of_evens_and_odds(args):
#     even = 0
#     odd = 0
#     *first, last = args
#     if last % 2 == 0:
#         even = last
#     else:
#         odd = last

#     for i in first:
#         if i % 2 == 0:
#             even += i
#         else:
#             odd += i
  
#     return even, odd

def sum_of_evens_and_odds(numbers):
    even_numbers = [num for num in numbers if num %2 == 0]
    odd_numbers = [num for num in numbers if num %2 != 0]
    return(sum(even_numbers), sum(odd_numbers))

# def sum_of_evens_and_odds(numbers):
#     even = []
#     odd = []
#     j = 0
#     k = 0
#     for i in numbers:
#         if i % 2 ==0:
#             even.insert(j, i)
#             j +=1
#         else:
#             odd.insert(k, i)
#             k += 1

            
#     return sum(even), sum(odd)

print("*********** sum of evens and odds *********")
print(sum_of_evens_and_odds((1, 2, 3, 4)))
print(sum_of_evens_and_odds((1, 3, 5)))
print(sum_of_evens_and_odds((2, 4, 6)))



        


