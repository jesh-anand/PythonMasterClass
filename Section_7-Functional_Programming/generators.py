"""generators.py: This script uses the generator function from Python.
            Any function that uses yield is using the generator
"""


def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1


for x in function():
    print(x)
