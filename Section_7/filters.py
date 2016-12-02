""" Using filters in Python and lambdas

A filter sets the criteria of the values printed out from the list
"""

newList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a new filter to print out odd numbers
result = list(filter(lambda x: x % 2 == 0, newList))

print(result)
