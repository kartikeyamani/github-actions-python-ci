import unittest
from src.calculator import add, subtract, divide 
class TestCalculator(unittest.TestCase):
   def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)
    self.assertEqual(add(-1, -1), -2)
   def test_subtract(self):
    self.assertEqual(subtract(4, 2), 2)
    self.assertEqual(subtract(-1, 1), -2)
    self.assertEqual(subtract(-1, 0), -1)
   def test_divide(self):
    self.assertEqual(divide(2, 1), 2)
    self.assertEqual(divide(-1, 1), -1)
    self.assertIsNone(divide(10, 0))  # Check if division by zero returns None
    self.assertAlmostEqual(divide(7, 3), 7/3, places=7)  # Check for float precision
if __name__ == '__main__':
   unittest.main()