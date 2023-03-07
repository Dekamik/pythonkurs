import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_1plus1_returns2(self):
        self.assertEqual(self.calculator.add(1, 1), 2)
    
    def test_add_2plus5_returns7(self):
        self.assertEqual(self.calculator.add(2, 5), 7)


if __name__ == "__main__":
    unittest.main()
