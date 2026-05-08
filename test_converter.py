import unittest
from converter import *

class TestConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)
    
    def test_km_to_miles(self):
        self.assertAlmostEqual(km_to_miles(1), 0.621371)

if __name__ == "__main__":
    unittest.main()