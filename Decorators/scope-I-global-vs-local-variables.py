# Scope is the locations in a program in which a name can be used.
# shadow variable is a local variable that shares the same name as a global variable.
# constant is a name for a value that does not change over the program's execution
# LEGB is Local/ Enclosing Functions / Global / Built-in
# Closure is a programming pattern in which a scope retains access to an enclosing scope's names

x = 10
vlaue = 10

def outer():
    x = 20

    def inner():
        x = 5
        return x

    return inner()

print(outer())
    
def a():
    value = 20
    return value

print(a())


def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def calculate(func, a, b):
  return func(a, b)

print(calculate(multiply, 10, 5))


def a():
  def b():
    def c():
      return val
    return c()
  return b()
val = "Hello"
print(a())

a = 1
def modify_a(b):
   global a
   a = b
    
modify_a(10)
print(a)

def first():
    first_name = "Hanny"

    def last():
        nonlocal first_name
        first_name = "Teka"

    last()
    return first_name

print(first())


def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you. i'm inner functon")
        fn(*args, **kwargs)
        print("i'm fn function")

    return inner  

def complex_fn(another):
    "a function that is going to be passed"
    print(f"I'm complex_fn function {another}") 
    

def make_x():
    global x
    x = 10

def make_y():
    global y
    y = 20

make_x()
make_y()
print(x + y)


import functools

def uppercase(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()

    return wrapper

@uppercase
def concatenate(a, b):
    """Combines two strings together"""
    return a + b

print(concatenate("pyt", "hon"))

import timeit

def time_it(fun):
    fun()
    print(timeit.timeit(fun))

    





