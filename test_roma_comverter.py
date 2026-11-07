import unittest
from roma_converter import RomanNumeralConverter

class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        print("Creating a new RomanNumeralConverter...")
        self.cvt = RomanNumeralConverter()

    def tearDown(self):
        print("Destroying the RomanNumeralConverter...")
        self.cvt = None

    # pojedyncze cyfry 

    def test_parsing_millenia(self):
        self.assertEqual(1000, self.cvt.convert_to_decimal("M"))

    def test_pol_milenium(self):
        self.assertEqual(500, self.cvt.convert_to_decimal("D"))

    def test_wiek(self):
        self.assertEqual(100, self.cvt.convert_to_decimal("C"))

    def test_pol_wieku(self):
        self.assertEqual(50, self.cvt.convert_to_decimal("L"))

    def test_dekada(self):
        self.assertEqual(10, self.cvt.convert_to_decimal("X"))

    def test_pol_dekady(self):
        self.assertEqual(5, self.cvt.convert_to_decimal("V"))

    def test_jeden(self):
        self.assertEqual(1, self.cvt.convert_to_decimal("I"))

    # zero

    def test_zero(self):
        # Rzymianie nie mieli zera, więc pusty napis daje 0
        self.assertEqual(0, self.cvt.convert_to_decimal(""))

    # wartości nie rzymskie

    def test_nie_rzymskie(self):
        for napis in ("Z", "A", "1", "m", "MZ"):
            with self.subTest(napis=napis):
                self.assertRaises(KeyError, self.cvt.convert_to_decimal, napis)

    # wartości złożone

    def test_zlozone(self):
        self.assertEqual(4668, self.cvt.convert_to_decimal("MMMMDCLXVIII"))
        self.assertEqual(2024, self.cvt.convert_to_decimal("MMXXIIII"))
        self.assertEqual(1666, self.cvt.convert_to_decimal("MDCLXVI"))
        self.assertEqual(3, self.cvt.convert_to_decimal("III"))

if __name__ == "__main__":
    unittest.main()
