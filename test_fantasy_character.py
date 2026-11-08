import unittest
from fantasy_character import *


class TestKonstruktor(unittest.TestCase):

    def test_domyslne(self):
        p = FantasyCharacter("Bilbo")
        self.assertEqual(p.health, 100)
        self.assertEqual(p.inventory, [])
        self.assertEqual(p.position, (0, 0))
        self.assertEqual(p.states, ["idle"])

    def test_wszystkie_parametry(self):
        p = FantasyCharacter("Frodo", 50, ["pierscien"], (3, 4), ["injured"])
        self.assertEqual(p.name, "Frodo")
        self.assertEqual(p.health, 50)
        self.assertEqual(p.inventory, ["pierscien"])
        self.assertEqual(p.position, (3, 4))
        self.assertEqual(p.states, ["injured"])

    # nazwa
    def test_nazwa_ok(self):
        self.assertEqual(FantasyCharacter("Elf123").name, "Elf123")
        self.assertEqual(FantasyCharacter("A").name, "A")

    def test_nazwa_zla(self):
        with self.assertRaises(ValueError):
            FantasyCharacter("Gan dalf")
        with self.assertRaises(ValueError):
            FantasyCharacter("Gandalf!")
        with self.assertRaises(ValueError):
            FantasyCharacter("")

    # zdrowie - wartosci brzegowe
    def test_zdrowie_0(self):
        self.assertEqual(FantasyCharacter("Bob", 0).health, 0)

    def test_zdrowie_100(self):
        self.assertEqual(FantasyCharacter("Bob", 100).health, 100)

    def test_zdrowie_1_i_99(self):
        self.assertEqual(FantasyCharacter("Bob", 1).health, 1)
        self.assertEqual(FantasyCharacter("Bob", 99).health, 99)

    def test_zdrowie_minus_1(self):
        with self.assertRaises(ValueError):
            FantasyCharacter("Bob", -1)

    def test_zdrowie_101(self):
        with self.assertRaises(ValueError):
            FantasyCharacter("Bob", 101)

    def test_zdrowie_string(self):
        with self.assertRaises(TypeError):
            FantasyCharacter("Bob", "50")

    # ekwipunek
    def test_ekwipunek_10(self):
        p = FantasyCharacter("Bob", 100, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        self.assertEqual(len(p.inventory), 10)

    def test_ekwipunek_11(self):
        with self.assertRaises(OveloadError):
            FantasyCharacter("Bob", 100, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])

    # pozycja
    def test_pozycja_0(self):
        self.assertEqual(FantasyCharacter("Bob", position=(0, 0)).position, (0, 0))

    def test_pozycja_999(self):
        self.assertEqual(FantasyCharacter("Bob", position=(999, 999)).position, (999, 999))

    def test_pozycja_1_i_998(self):
        self.assertEqual(FantasyCharacter("Bob", position=(1, 998)).position, (1, 998))
        self.assertEqual(FantasyCharacter("Bob", position=(998, 1)).position, (998, 1))

    def test_pozycja_minus_1(self):
        with self.assertRaises(PositionError):
            FantasyCharacter("Bob", position=(-1, 0))

    def test_pozycja_1000(self):
        with self.assertRaises(PositionError):
            FantasyCharacter("Bob", position=(0, 1000))

    # stany
    def test_kilka_stanow(self):
        p = FantasyCharacter("Bob", states=["injured", "stunned"])
        self.assertEqual(p.states, ["injured", "stunned"])

    def test_wszystkie_stany(self):
        stany = ["idle", "moving", "attacking", "talking", "injured",
                 "unconscious", "dead", "stunned", "hidden", "equip with miecz"]
        p = FantasyCharacter("Bob", 100, ["miecz"], (0, 0), stany)
        self.assertEqual(p.states, stany)

    def test_zly_stan(self):
        with self.assertRaises(ValueError):
            FantasyCharacter("Bob", states=["flying"])

    def test_equip_bez_przedmiotu_w_konstruktorze(self):
        # nie mozna miec zalozonego miecza jak nie ma go w ekwipunku
        with self.assertRaises(NoItemError):
            FantasyCharacter("Bob", 100, [], (0, 0), ["equip with miecz"])


class TestMetody(unittest.TestCase):

    def setUp(self):
        self.p = FantasyCharacter("Aragorn", 80, ["miecz"], (10, 10))

    # take
    def test_take(self):
        self.p.take("tarcza")
        self.assertEqual(self.p.inventory, ["miecz", "tarcza"])

    def test_take_za_duzo(self):
        for i in range(9):
            self.p.take("rzecz")
        self.assertEqual(len(self.p.inventory), 10)
        with self.assertRaises(OveloadError):
            self.p.take("rzecz")

    # drop
    def test_drop(self):
        self.p.drop("miecz")
        self.assertEqual(self.p.inventory, [])

    def test_drop_pusty(self):
        self.p.drop("miecz")
        with self.assertRaises(NoItemError):
            self.p.drop()

    def test_drop_nie_ma_takiego(self):
        with self.assertRaises(NoItemError):
            self.p.drop("topor")
        self.assertEqual(self.p.inventory, ["miecz"])

    # move
    def test_move(self):
        self.p.move(5, -3)
        self.assertEqual(self.p.position, (15, 7))
        self.assertIn("moving", self.p.states)

    def test_move_na_granice(self):
        self.p.move(-10, 989)
        self.assertEqual(self.p.position, (0, 999))

    def test_move_poza_zakres(self):
        with self.assertRaises(PositionError):
            self.p.move(-11, 0)
        with self.assertRaises(PositionError):
            self.p.move(0, 990)
        self.assertEqual(self.p.position, (10, 10))

    # equip / unequip
    def test_equip(self):
        self.p.equip("miecz")
        self.assertIn("equip with miecz", self.p.states)

    def test_equip_brak_przedmiotu(self):
        with self.assertRaises(NoItemError):
            self.p.equip("topor")

    def test_unequip(self):
        self.p.equip("miecz")
        self.p.unequip("miecz")
        self.assertNotIn("equip with miecz", self.p.states)

    def test_unequip_nie_zalozony(self):
        with self.assertRaises(NoItemEquiptError):
            self.p.unequip("miecz")

    # attack
    def test_attack(self):
        self.p.equip("miecz")
        self.p.attack()
        self.assertIn("attacking", self.p.states)

    def test_attack_bez_broni(self):
        with self.assertRaises(NoItemToEquiptError):
            self.p.attack()

    # hide / talk
    def test_hide(self):
        self.p.hide()
        self.assertIn("hidden", self.p.states)

    def test_talk(self):
        self.p.talk()
        self.assertIn("talking", self.p.states)

    def test_talk_ukryty(self):
        self.p.hide()
        with self.assertRaises(TalkingError):
            self.p.talk()

    # status
    def test_show_status(self):
        s = self.p.show_status()
        self.assertEqual(s["name"], "Aragorn")
        self.assertEqual(s["health"], 80)
        self.assertEqual(s["inventory"], ["miecz"])
        self.assertEqual(s["position"], (10, 10))
        self.assertEqual(s["state"], ["idle"])


if __name__ == "__main__":
    unittest.main()
