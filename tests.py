import unittest
from exercises import *

class TestStringMethods(unittest.TestCase):
    # create a new list with same values as old list
    def test_exercise1(self):
        arg = [1, 2, 3]
        result = exercise1(arg)

        self.assertEqual(result, [1, 2, 3])
        self.assertIsNot(arg, result)

    # create a new list by transforming each element
    def test_exercise2(self):
        arg = [1, 2, 3]
        result = exercise2(arg)

        self.assertEqual(result, [1, 4, 9])
        self.assertIsNot(arg, result)

    # create a new list based on some condition (filtering)
    # only get evens
    def test_exercise3(self):
        arg = [1, 2, 3, 4, 5]
        result = exercise3(arg)

        self.assertEqual(result, [2, 4])
        self.assertIsNot(arg, result)

    # chained condition: divisible by 3 or 5
    def test_exercise3dot1(self):
        arg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = exercise3dot1(arg)

        self.assertEqual(result, [3, 5, 6, 9, 10])
        self.assertIsNot(arg, result)

    # do it with a transformation
    def test_exercise3dot2(self):
        arg = [1, 2, 3, 4, 5, 6]
        result = exercise3dot2(arg)

        self.assertEqual(result, [9, 25, 36])
        self.assertIsNot(arg, result)

    # do the transformation using an if/else statement. no filtering
    # if even, double. if odd, triple.
    def test_exercise4(self):
        arg = [1, 2, 3]
        result = exercise4(arg)

        self.assertEqual(result, [3, 4, 9])
        self.assertIsNot(arg, result)

    # do a transformation with nested comps
    # do a square of squares
    def test_exercise5(self):
        arg = [1, 2, 3]
        result = exercise5(arg)

        self.assertEqual(result, [1, 16, 81])
        self.assertIsNot(arg, result)

    # use a list, then create a list for each element of values added to index
    def test_exercise6(self):
        arg = [1, 2]
        result = exercise6(arg)

        self.assertEqual(result, [[1, 2], [2, 3]])
        self.assertIsNot(arg, result)

    # generate all combinations of elements given two lists
    def test_exercise7(self):
        # given elements [1, 2] and [3, 4]. combinations = 2 * 2 = 4 = (1, 3), (1, 4), (2, 3), (2, 4)
        arg1 = [1, 2]
        arg2 = [3, 4]
        result = exercise7(arg1, arg2)

        self.assertEqual(result, [(1, 3), (1, 4), (2, 3), (2, 4)])

     # generate all combinations of elements given two lists only if element in first list is even
    def test_exercise8(self):
        # given elements [1, 2] and [3, 4]. combinations = 2 * 2 = 4 = (2, 3), (2, 4)
        arg1 = [1, 2]
        arg2 = [3, 4]
        result = exercise8(arg1, arg2)

        self.assertEqual(result, [(2, 3), (2, 4)])

    #  create a list of lists. i.e a matrix.
    def test_exercise9(self):
        arg = [1, 2, 3] # each value is all the values for each row in the matrix
        result = exercise9(arg)

        self.assertEqual(result, [[1, 1, 1], [2, 2, 2], [3, 3, 3]])
        self.assertIsNot(arg, result)

    #  flattening a list of lists
    def test_exercise11(self):
        arg = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = exercise11(arg)

        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertIsNot(arg, result)

    # list of 100 numbers from 0 to 100
    def test_exercise13(self):
        result = exercise13(5)
        self.assertEqual(result, [0, 1, 2, 3, 4])

    def test_exercise14(self):
        arg = [[[1], [2], [3]], [[4], [5], [6]]]
        result = exercise14(arg)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()