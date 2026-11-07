import unittest
from roma_converter import RomanNumeralConverter

class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        print("Creating a new RomanNumeralConverter...")
        self.cvt = RomanNumeralConverter()

    def tearDown(self):
        print("Destroying the RomanNumeralConverter...")
        self.cvt = None

    def test_parsing_millenia(self):
        self.assertEquals(1000, self.cvt.convert_to_decimal("M"))