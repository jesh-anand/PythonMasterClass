import unittest

"""test_exercise.py: This script showcases the use of unit testing in Python by importing the unittest module"""


def cubeArea(radius):
    return radius ** 3


def triangleArea(base, height):
    return base * height


def checkEvenOrOdd(value):
    if value % 2 == 0:
        return "Even"
    else:
        return "Odd"


class MyTest(unittest.TestCase):
    def test_cubeArea(self):
        result = cubeArea(10)
        self.assertEqual(result, 1000)

    def test_triangleArea(self):
        result = triangleArea(10, 10)
        self.assertEqual(result, 100)

    def test_even_or_odd(self):
        self.assertEqual(checkEvenOrOdd(10), "Even")
        self.assertEqual(checkEvenOrOdd(3), "Odd")
        self.assertEqual(checkEvenOrOdd(30), "Even")
        self.assertNotEquals(checkEvenOrOdd(1), "Even")


if __name__ == '__main__':
    MyTest()
