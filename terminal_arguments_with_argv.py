# import sys

# print(sys.argv)

# word_lengths = 0

# for arg in sys.argv[1:]:
#     word_lengths += len(arg)

# print(f"The total length of all terminal is {word_lengths}")

# ##########
# Define a function that iterates over a list of numbers,
# multiplies each number by one less than its index position
# and returns the total sum of those products

def iterates_list_numbers(): 
    numbers = [1, 2, 3, 4, 5]
    # 0 + ()
    totalSum = 0

    for index, num in enumerate(numbers):
        
        totalSum = totalSum + ((index - 1) * num)
        

    return totalSum


print(iterates_list_numbers())