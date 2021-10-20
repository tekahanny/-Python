# Define a same_first_and_last_letter function that accepts a string as an argument. 
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same_first_and_last_letter("runner")   => True
# same_first_and_last_letter("Runner")   => False
# same_first_and_last_letter("clock")    => False
# same_first_and_last_letter("q")        => True

'''
def same_first_and_last_letter(letter):
    first = letter[0]
    second = letter[-1]
    if first == second:
        return True
    else:
        return False
'''
def same_first_and_last_letter(letter):
    return print(letter[0] == letter[-1])

same_first_and_last_letter("runner") 
same_first_and_last_letter("Runner")
same_first_and_last_letter("clock")
same_first_and_last_letter("q")