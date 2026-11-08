import unittest
from car import Samochod, AccelerateError, EmptyFuelTankError, NoEnaughtFuelError


class TestSamochodBledy(unittest.TestCase):

    def setUp(self):
        # spala 10 l/100 km, przyspieszenie 1 km/s^2, bak 50 l
        self.auto = Samochod("Fiat", 10, 1, 50)

    # AccelerateError

    def test_za_male_przyspieszenie(self):
        for przyspieszenie in (0.09, 0.05, 0, -1):
            with self.subTest(przyspieszenie=przyspieszenie):
                auto = Samochod("Fiat", 10, przyspieszenie, 50)
                with self.assertRaises(AccelerateError):
                    auto.przyspiesz()
                self.assertEqual(auto.predkosc, 0)  # prędkość się nie zmieniła

    def test_przyspieszenie_komunikat(self):
        auto = Samochod("Fiat", 10, 0.05, 50)
        with self.assertRaisesRegex(AccelerateError, "Przyspieszenie zbyt małe"):
            auto.przyspiesz()

    def test_przyspieszenie_granica_ok(self):
        # 0.1 to minimalne dozwolone przyspieszenie - błędu być nie powinno
        auto = Samochod("Fiat", 10, 0.1, 50)
        auto.przyspiesz()
        self.assertAlmostEqual(auto.predkosc, 0.1)

    # EmptyFuelTankError

    def test_pusty_bak(self):
        self.auto.poziom_paliwa = 0
        with self.assertRaisesRegex(EmptyFuelTankError, "Bak jest pusty"):
            self.auto.jedz(10)

    def test_pusty_bak_po_jezdzie(self):
        self.auto.przyspiesz()       # 1 km/s
        self.auto.jedz(500)          # 500 km = dokładnie 50 l, bak pusty
        self.assertEqual(self.auto.poziom_paliwa, 0)
        with self.assertRaises(EmptyFuelTankError):
            self.auto.jedz(1)

    def test_auto_z_pustym_bakiem(self):
        auto = Samochod("Fiat", 10, 1, 0)
        with self.assertRaises(EmptyFuelTankError):
            auto.jedz(10)

    # NoEnaughtFuelError

    def test_za_malo_paliwa(self):
        self.auto.przyspiesz()       # 1 km/s
        with self.assertRaisesRegex(NoEnaughtFuelError, "Za mało paliwa"):
            self.auto.jedz(600)      # 600 km = 60 l, a w baku jest 50 l
        self.assertEqual(self.auto.poziom_paliwa, 50)  # paliwo nie zostało zużyte

    def test_za_malo_paliwa_o_troche(self):
        self.auto.przyspiesz()
        with self.assertRaises(NoEnaughtFuelError):
            self.auto.jedz(501)      # potrzeba 50.1 l

    # właściwy typ błędu

    def test_pusty_bak_to_nie_brak_paliwa(self):
        # pusty bak musi dać EmptyFuelTankError, a nie NoEnaughtFuelError
        self.auto.poziom_paliwa = 0
        self.auto.przyspiesz()
        with self.assertRaises(EmptyFuelTankError) as kontekst:
            self.auto.jedz(100)
        self.assertNotIsInstance(kontekst.exception, NoEnaughtFuelError)


if __name__ == "__main__":
    unittest.main()
