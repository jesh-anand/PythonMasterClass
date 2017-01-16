'''for_loop.py: A simple for loop'''


def simple_for_loop():
    for x in range(1, 11):
        print('Hello')


def loop_in_a_list():
    fruits = ['Apple', 'Banana', 'Orange']
    for x in fruits:
        print(x)


def print_even_numbers():
    # count in 2 intervals
    for x in range(0, 20, 2):
        print(x)


if __name__ == '__main__':
    print_even_numbers()
