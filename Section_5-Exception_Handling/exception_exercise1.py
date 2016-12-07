"""exception_exercise1.py: This script displays the use of exception handling in Python"""


def sum(a, b):
    try:
        value = a / b
        print(value)
    except ZeroDivisionError:
        print("There is a DivideByZero error!")
    finally:
        print("This will execute no matter what!")


sum(2, 0)
