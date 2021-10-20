# Declare a Country class with an empty body.

# Instantiate an object from the class and assign it to an “america" variable.

# Instantiate another object from the class and assign it to a “canada” variable.

# Instantiate a third object from the class and assign it to a “mexico” variable.

class Country():
    pass

america = Country()
canada = Country()
mexico = Country()

# Declare a Superhero class with an empty body.

# Instantiate an object from the class and assign it to an “spiderman" variable.

# Instantiate another object from the class and assign it to a “batman” variable.

# Instantiate a third object from the class and assign it to a “superman” variable.

class Superhero():
    pass

spiderman = Superhero()
batman = Superhero()
superman = Superhero()

# Declare a Musical class that accepts a name parameter. 
# In the initialization process for an object, assign the
# name parameter to a name attribute on the object.
#
# Instantiate a Musical object with the name “Rent” 
# and assign it to an “rent" variable.
#
# Instantiate a second Musical object with the name “Book of Mormon" 
# and assign it to a “mormon” variable.
#
# Instantiate a third object from the class with the name “Chicago" 
# and assign it to a “chicago” variable.

class Musical():
    def __init__(self,name):
        self.name = name

rent = Musical("Rent")

mormon = Musical("Book of Mormon")

chicago = Musical("Chicago")

# Declare a Shape class that accepts a sides parameter. 

# In the initialization process for an object, assign the sides parameter to a sides attribute on the object.

# Instantiate a Shape object with 3 sides and assign it to a “triangle" variable.

# Instantiate a Shape object with 4 sides and assign it to a “square" variable.

# Instantiate a Shape object with 10 sides and assign it to a “decagon" variable.

class Shape():
    def __init__(self, sides):
        self.sides = sides

triangle = Shape(3)
square = Shape(4)
decagon = Shape(10)

# Declare a Skyscraper class that accepts name and year parameters. 

# In the initialization process for an object, assign the name parameter to a name attribute 
# and the year parameter to a year attribute.

# Instantiate a Skyscraper object with the name “Empire State Building”  and the year 1931. 
# Assign it to a “empire" variable.

# Instantiate a Skyscraper object with the name “One World Trade Center” and the year 2014. 
# Assign it to a “wtc" variable.

class Skyscraper():
    def __init__(self, name, year):
        self.name = name
        self.year = year

empire = Skyscraper("Empire State Building", 1931)
wtc = Skyscraper("One World Trade Center", 2014)


# Declare a Zombie class that accepts health and brains_eaten parameters. 

# In the initialization process for a Zombie object, assign the 
# two parameters to two attributes with the same name.
#
# If the instantiation does not pass a health parameter, 
# it should be assigned a default value of 100.
#
# If the instantiation does not pass a brains_eaten parameter, 
# it should be assigned a default value of 5.

# Instantiate a Zombie object with 80 health and 5 brains eaten. 
# Assign it to a “bob” variable.
#
# Instantiate a Zombie object with 120 health and 3 brains eaten.
# Assign it to a “sally” variable.
#
# Instantiate a Zombie object with no custom parameters.
# Assign it to a “benjamin” variable.
#
# Practice instantiating the objects with both positional and keyword arguments.

class Zombie():
    def __init__(self, health = 100, brains_eaten = 5):
        self.health = health
        self.brains_eaten = brains_eaten

bob = Zombie(80)
sally = Zombie(120, 3)
benjamin = Zombie()


