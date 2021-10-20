def one():
    return 1

print(type(one))

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def calculate(func, a, b):
    return func(a, b)

print(calculate(add, 5, 3))
print(calculate(substract, 5, 3))

# Define an invoke_thrice function.
# It should accept a single argument (which will be a function)
# In its body, the invoke_thrice function should invoke
# the function that's passed in exactly three times.

def invoke_thrice(func):
    func(), func(), func()

def sample():
    print("A")
    print("B")
    print("C")

invoke_thrice(sample)

