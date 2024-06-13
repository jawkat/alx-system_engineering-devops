import unittest

from test import square, double

class TestSquare(unittest.TestCase):
    def	test1(self):
        self.assertEqual(square(2),4)
        self.assertEqual(square(3.0),9.0)
        self.assertNotEqual(square(-3),-9)

unittest.main()
