""" The values in the list are implemented with the function.

This approach can then be replaced with the use of the use of lambda
"""


def add(x):
    return x + 2


oldList = [10, 20, 30, 40, 50]

result = list(map(add, oldList))
print(result)

# --- Using lambda with the similar outcome above
oldList1 = [10, 20, 30, 40, 50]
lambda_result = list(map(lambda x: x * 2, oldList1))
print(lambda_result)
