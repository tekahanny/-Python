# book.py

# Let’s say we want to model a Book as a Python object. 
# A Book has an author and a publisher, which are characteristics that cannot change. 
# A Book also has a page_count, which could be altered if you rip some pages from the book.

# Declare a Book class that accepts author, publisher, and page_count parameters. 
# Each of the parameters should be assigned to an attribute. 
# The author and publisher attributes should be designated as protected (use an underscore). 
# The page_count attribute should be designated public.

# Define a copyright instance method that returns a string with information about the copyright. 
# It should look the string below, where “Grant Cardone” is the value of the protected
# author attribute and “10X Enterprises” is the value of the protected publisher attribute.

# => Copyright Grant Cardone, 10X Enterprises

# The public page_count attribute can always be manually modified. 
# However, we can still define an instance method that modifies it. 

# Declare a rip_in_half instance method. 
# If the book has more than 1 page, it should halve the page_count. 
# If the book has 1 page or less, it should set the page_count to 0.

# See sample execution below


from typing import Counter


class Book():
    def __init__(self, author, publisher, page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count

    def copyright(self):
       
        return f"Copyright {self._author},{self._publisher}"

    def rip_in_half(self):
        if self.page_count > 1:
            self.page_count /= 2
            return self.page_count
        elif self.page_count <= 1:
            self.page_count = 0
            return self.page_count





book = Book(author = "Grant Cardone", publisher = "10X Enterprises", page_count = 10)

print(book.copyright()) # Copyright Grant Cardone, 10X Enterprises

print(book.page_count) # 10
book.rip_in_half()
print(book.page_count) # 5.0
book.rip_in_half()
print(book.page_count) # 2.5
book.rip_in_half()
print(book.page_count) # 1.25
book.rip_in_half()
print(book.page_count) # 0.625
book.rip_in_half()
print(book.page_count) # 0
book.rip_in_half()
print(book.page_count) # 0

print()
print()
print()

# Declare a PizzaPie class that accepts a total_slices parameter. 
# In the instantiation process for an object, assign the parameter to an 
# attribute with the same name. 

# A PizzaPie object should also be initialized with a _slices_eaten 
# protected attribute set to 0.

# Define a slices_eaten property. 
# The getter method should retrieve the value of the _slices_eaten attribute. 
# The setter method should set a new value for the _slices_eaten attribute
# but only if the argument is less than total_slices.

# Define a percentage property that calculates how much of the pie has been eaten 
# (the number of slices eaten divided by the total slices available). 
# The percentage property should be read-only.

# See sample execution below
#
# cheese = PizzaPie(8)
# cheese.slices_eaten = 2
# print(cheese.percentage) # 0.25
#
# cheese.slices_eaten = 4
# print(cheese.percentage) # 0.5
#
# cheese.slices_eaten = 10 # _slices_eaten should not change because there's only 8 slices in pie
# print(cheese.percentage) # 0.5
#
# ERROR - AttributeError: can't set attribute
# cheese.percentage = 0.50

class PizzaPie():
    def __init__(self, total_slices):
        self.total_slices = total_slices
        self._slices_eaten = 0

    def get_slices_eaten(self):
        return self._slices_eaten

    def set_slices_eaten(self, slices_eaten):
        if slices_eaten < self.total_slices:
            self._slices_eaten = slices_eaten


    slices_eaten = property(get_slices_eaten, set_slices_eaten)

    @property
    def percentage(self):
        return self.slices_eaten / self.total_slices    
    
   

cheese = PizzaPie(8)
cheese.slices_eaten = 2
print(cheese.percentage) # 0.25

cheese.slices_eaten = 4
print(cheese.percentage) # 0.5

cheese.slices_eaten = 10 # _slices_eaten should not change because there's only 8 slices in pie
print(cheese.percentage) # 0.5

# ERROR - AttributeError: can't set attribute
#cheese.percentage = 0.50

print()
print()
print()

class Counter():
    

    def __init__(self, count):
        self.count = count
        self.count += 1

    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        print("New number of Counter objects created: {cls.count}")
        return two_counters

cac = Counter(0)
print(cac.count)

class Coffee:
    def __init__(self, cream, sugar, half_and_half):
        self.cream = cream
        self.sugar = sugar
        self.half_and_half = half_and_half
 
 
morning_joe = Coffee(True, False, True)
print(morning_joe.cream)
print(morning_joe.sugar)
print(morning_joe.half_and_half)
 
for val in [
    "cream",
    "pumpkin spice",
    "cinnamon",
    "sugar",
    "half_and_half",
]:
    print()
    print(hasattr(morning_joe, val))
    print()
    if hasattr(morning_joe, val):
        setattr(
            morning_joe, val, not getattr(morning_joe, val)
        )
 
print(
    morning_joe.cream,
    morning_joe.sugar,
    morning_joe.half_and_half,
)
