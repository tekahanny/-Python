# Define a first_longer_than_second function that accepts two string arguments. 
# The function should return a True if the first string is longer than the second 
# and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")     => True
# first_longer_than_second("cat", "mouse")       => False
# first_longer_than_second("Steven", "Seagal")   => False

'''
def first_longer_than_second(first, second):
    if len(first) > len(second):
        return print(True)
    else:
        return print(False)
'''

def first_longer_than_second(string1, string2):
    return len(string1) > len(string2)

first_longer_than_second("Python", "Ruby")
first_longer_than_second("cat", "mouse")
first_longer_than_second("Steven", "Seagal")