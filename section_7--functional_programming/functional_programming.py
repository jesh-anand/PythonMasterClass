"""
functional_programming.py
=>  Functional programming to passing function to another function as argument.
    This script is doing just that - add_ten function passed to twice function

    NOTE the use of data type func declared in the argument of the 'twice' function
"""


def add_ten(x):
    return x + 10


def twice(func, arg):
    return func(func(arg))


print(twice(add_ten, 10))
