# Declare a Musician class that accepts age and income parameters. 

# In the instantiation process for an object, assign the two parameters
# to two attributes with the same name.

# Declare an enter_club instance method. 
# If the musician is less than 21 years old, the method should 
# return the string "Access denied!”. 
# If the musician is 21 or older, the method should
# return the string "Access granted!".

# Declare a play_show instance method. The method should
# increment the musician’s income by 5.

# EXAMPLES
#

class Musician():
    def __init__(self, age, income):
        self.age = age
        self.income = income

    def enter_club (self):
        if self.age < 21:
            return "Access denied!"
        elif self.age >= 21:
            return "Access granted!"

    def play_show(self):
        self.income += 5

cliff = Musician(age = 27, income = 0)
print(cliff.age)    # 27
print(cliff.enter_club())  # "Access granted!"
print(cliff.income) # 0
cliff.play_show()
print(cliff.income) # 5
cliff.play_show()
print(cliff.income) # 10