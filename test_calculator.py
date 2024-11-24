import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add(self):
        self.assertEqual(self.calc.add(1, 3), 4)
    def test_add2(self):
        self.assertEqual(self.calc.add(6, 1), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 5), 4)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(7, 10), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(3, 6), 18)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 4), 1)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(9, 3), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(2, 32), 2)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(4, 1), 0)

if __name__ == '__main__':
    unittest.main()