import unittest
from math import pi

from circle import circle_area


class TestCircleArea(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_jeden(self):
        self.assertAlmostEqual(circle_area(1), pi)

    def test_liczba_calkowita(self):
        self.assertAlmostEqual(circle_area(10), pi * 100)

    def test_float(self):
        self.assertAlmostEqual(circle_area(2.5), pi * 2.5 ** 2)
        self.assertAlmostEqual(circle_area(0.1), pi * 0.01)

    def test_ujemne(self):
        for r in (-1, -0.5, -100):
            with self.subTest(r=r):
                self.assertRaises(ValueError, circle_area, r)

    def test_zle_typy(self):
        for r in ("5", "abc", True, False, 3 + 5j, None, [1]):
            with self.subTest(r=r):
                self.assertRaises(TypeError, circle_area, r)


if __name__ == "__main__":
    unittest.main()
