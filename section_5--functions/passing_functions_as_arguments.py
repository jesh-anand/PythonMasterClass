"""passing_functions_as_arguments.py: As the title of the script denotes"""


def add(a, b):
    return a + b


def square(c):
    return c ** 2


result = square(add(2, 3))
print(result)
