# Declare a set with 3 of your favorite movies as strings.
# Assign it to a movies variable.


# Declare a set with the first four months of the year as strings.
# Assign it to a months variable.
# Make sure the first letter of each month is capitalized.


# Create an empty set and assign it to an empty variable.


# Define a remove_duplicates function that accepts a single list as an argument. 
# The function should return a list with all of the duplicates from the original list removed. 
# The order of elements in the returned list is irrelevant.
#
# EXAMPLES:
# remove_duplicates([1, 2, 1, 2])  => [1, 2] or [2, 1]
# remove_duplicates([1, 2, 3, 4])  => [1, 2, 3, 4] in some order

print()
print("************* Set Basics *************")

movies = {"save the last dance", "A walk to remember", "Titanic" }
months = {"January", "February", "March", "April"}
empty = set()
def remove_duplicates(single_list):
    remove_dup = set(single_list)
    single_list = list(remove_dup)

    return single_list

print(remove_duplicates([1, 2, 1, 2]))
print(remove_duplicates([1, 2, 3, 4]))

print()
print("************** Quiz ***********")

values = [0, 0.0, "0.0"]
print(set(values))

pages = { 10, 20, 30}
element = pages.remove(30)
print(element)
print(pages)

# Only immutable types can be added to a set.
# the remove method returns None.

print()
print("********** Intersection *************")

candey_bars = {"Milky way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch kids", "Reeses Pieces", "Snickers"}
sweet = candey_bars.intersection(sweet_things)
sweet_sweet = candey_bars & sweet_things
print(sweet)
print(sweet_sweet)

print()
print("********** difference ************")
diff = candey_bars.difference(sweet_things)
diff_min = candey_bars - sweet_things
diff_sweet = sweet_things - candey_bars
print(diff)
print(diff_min)
print(diff_sweet)

print()
print("********** Quiz *********")
gatorade_flavors = {"blue", "red", "orange"}
powerade_flavors = {"red", "green", "yellow"}

print(gatorade_flavors.intersection(powerade_flavors))
# The difference method returns a set with all values present in gatorade_flavors but not present in powerade_flavors.
print(gatorade_flavors.difference(powerade_flavors)) 
# The ​symmetric_difference​ method returns a set with elements that are in either of the sets but are NOT shared by both sets.
print(gatorade_flavors.symmetric_difference(powerade_flavors))
# The union method returns all strings found across BOTH sets (with duplicates removed, of course).
print(gatorade_flavors.union(powerade_flavors))

juice_flavors = {"Lemon", "Peach", "Raspberry", "Apple"}
tea_flavors = {"Peach", "Grape", "apple"}
# differences between "Apple" and "apple"
print(juice_flavors & tea_flavors)
# This is the union of both sets, the combination of all elements across the two of them.
print(juice_flavors | tea_flavors)
# these are all the elements are that are NOT shared by the two sets. "Peach" is excluded.
print(juice_flavors ^ tea_flavors)
# These are all the strings found in juice_flavors that are NOT contained in tea_flavors.
print(juice_flavors - tea_flavors)


print()
print("******* issubset and issuperset *********")

a = {1, 2, 3}
b= {1, 2, 3, 4, 5}

print(a.issubset(b))
print(b.issuperset(a))
print(a < b)
print( a <= b)
print(b > a)
print(b >= a)

c= {1,2}
d = {1,2}

print()
print(c.issubset(d))
print(d.issuperset(c))
print(d.issubset(c))

e = c.issubset(d)
print()
print(e)
