# Define a string_adder function that accepts two strings (a and b) as arguments.
# It should return a concatenated version of the arguments with a space in between.
# If the user does not pass in arguments, both arguments should default to an empty string.
#
# EXAMPLES
# _adder("Hello", "World")      => "Hello World"
# string_adder("Emilio", "Estevez")   => "Emilio Estevez"
# string_adder()                      => " "
# string_adder("Tiger")               => "Tiger "string

def string_adder(a = "", b = ""):
    return a + " " + b


print(string_adder("Hello", "World") )
print(string_adder("Emilio", "Estevez"))
print(string_adder())
print(string_adder("Tiger"))
