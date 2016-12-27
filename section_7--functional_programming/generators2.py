"""generators2.py: Uses the generator function with yield and stores them in a list """


def even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(even_numbers(20)))
