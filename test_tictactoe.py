import unittest
from tictactoe import TicTacToe, Player, play


class GraczZListy(Player):
    # ruchy z gotowej listy
    def __init__(self, letter, ruchy):
        super().__init__(letter)
        self.ruchy = list(ruchy)

    def get_move(self, game):
        return self.ruchy.pop(0)


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.gra = TicTacToe()

    def wykonaj_ruchy(self, ruchy):
        #ruchy to lista par (pozycja, litera)
        for pozycja, litera in ruchy:
            self.gra.make_move(pozycja, litera)

    # Poczatek

    def test_plansza_ma_9_pol(self):
        self.assertEqual(len(self.gra.board), 9)

    def test_plansza_pusta(self):
        self.assertEqual(self.gra.board, [' '] * 9)
        self.assertTrue(self.gra.empty_squares())
        self.assertEqual(self.gra.num_empty_squares(), 9)

    def test_brak_zwyciezcy_na_starcie(self):
        self.assertIsNone(self.gra.current_winner)

    # prawidłowy ruch

    def test_ruch_na_wolne_pole(self):
        self.assertTrue(self.gra.make_move(4, 'X'))
        self.assertEqual(self.gra.board[4], 'X')
        self.assertEqual(self.gra.num_empty_squares(), 8)
        self.assertIsNone(self.gra.current_winner)

    def test_ruch_na_zajete_pole(self):
        self.gra.make_move(4, 'X')
        self.assertFalse(self.gra.make_move(4, 'O'))
        self.assertEqual(self.gra.board[4], 'X')  # pole się nie zmieniło

    # wygrana

    def test_wygrana_wiersz(self):
        for wiersz in ([0, 1, 2], [3, 4, 5], [6, 7, 8]):
            with self.subTest(wiersz=wiersz):
                self.gra = TicTacToe()
                self.wykonaj_ruchy([(p, 'X') for p in wiersz])
                self.assertEqual(self.gra.current_winner, 'X')

    def test_wygrana_kolumna(self):
        for kolumna in ([0, 3, 6], [1, 4, 7], [2, 5, 8]):
            with self.subTest(kolumna=kolumna):
                self.gra = TicTacToe()
                self.wykonaj_ruchy([(p, 'O') for p in kolumna])
                self.assertEqual(self.gra.current_winner, 'O')

    def test_wygrana_przekatna(self):
        for przekatna in ([0, 4, 8], [2, 4, 6]):
            with self.subTest(przekatna=przekatna):
                self.gra = TicTacToe()
                self.wykonaj_ruchy([(p, 'X') for p in przekatna])
                self.assertEqual(self.gra.current_winner, 'X')

    def test_brak_wygranej_gdy_dwa_w_rzedzie(self):
        self.wykonaj_ruchy([(0, 'X'), (1, 'X')])
        self.assertIsNone(self.gra.current_winner)

    # remis

    def test_remis(self):
        # X | O | X
        # X | O | O
        # O | X | X
        self.wykonaj_ruchy([(0, 'X'), (1, 'O'), (2, 'X'), (4, 'O'), (3, 'X'),
                            (5, 'O'), (7, 'X'), (6, 'O'), (8, 'X')])
        self.assertFalse(self.gra.empty_squares())
        self.assertEqual(self.gra.available_moves(), [])
        self.assertIsNone(self.gra.current_winner)

    def test_remis_cala_gra(self):
        #rozgrywka przez funkcję play(). Przy remisie zwraca None
        x = GraczZListy('X', [0, 2, 3, 7, 8])
        o = GraczZListy('O', [1, 4, 5, 6])
        wynik = play(self.gra, x, o, print_game=False)
        self.assertIsNone(wynik)

    #Dostępne ruchy

    def test_dostepne_ruchy_na_starcie(self):
        self.assertEqual(self.gra.available_moves(), list(range(9)))

    def test_dostepne_ruchy_po_ruchach(self):
        self.wykonaj_ruchy([(0, 'X'), (4, 'O'), (8, 'X')])
        self.assertEqual(self.gra.available_moves(), [1, 2, 3, 5, 6, 7])
        self.assertNotIn(4, self.gra.available_moves())


if __name__ == '__main__':
    unittest.main()
