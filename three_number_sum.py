# Define a three_number_sum function that accepts a 3-character string as an argument. 
# The function should add up the sum of the digits of the string. 
# HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.
#
# EXAMPLES:
# three_number_sum("123")   => 6
# three_number_sum("567")   => 18
# three_number_sum("444")   => 12
# three_number_sum("000")   => 0

def three_number_sum(word):
    return print(int(word[0]) + int(word[1]) + int(word[2]))

three_number_sum("123")
three_number_sum("567")
three_number_sum("444")
three_number_sum("000")