class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Inicjalizacja pustej planszy
        self.current_winner = None  # Śledzenie zwycięzcy

    def print_board(self):
        # Wyświetlanie aktualnego stanu planszy
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')

    def print_board_nums(self):
        # Wyświetlanie planszy z numerami pól
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row)+' |')

    def available_moves(self):
        # Zwraca listę dostępnych ruchów (pozycji)
        return [i for i, x in enumerate(self.board) if x == ' ']

    def empty_squares(self):
        # Sprawdza, czy są wolne pola
        return ' ' in self.board

    def num_empty_squares(self):
        # Zwraca liczbę wolnych pól
        return len(self.available_moves())

    def make_move(self, position, letter):
        # Wykonuje ruch na planszy, jeśli pozycja jest wolna
        if self.board[position] == ' ':
            self.board[position] = letter
            if self.winner(position, letter):
                self.current_winner = letter  # Aktualizacja zwycięzcy
            return True
        return False

    def winner(self, position, letter):
        # Sprawdza, czy aktualny ruch prowadzi do zwycięstwa
        # Sprawdzenie wiersza
        row_ind = position // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Sprawdzenie kolumny
        col_ind = position % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Sprawdzenie przekątnych
        if position % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

class Player:
    def __init__(self, letter):
        self.letter = letter  # 'X' lub 'O'

    def get_move(self, game):
        pass  # Metoda do nadpisania w klasach pochodnych

class HumanPlayer(Player):
    def get_move(self, game):
        # Pobieranie ruchu od gracza
        valid_move = False
        val = None
        while not valid_move:
            move = input(f"{self.letter}'s turn. Input move (0-8): ")
            try:
                val = int(move)
                if val in game.available_moves():
                    valid_move = True
                else:
                    print('Nieprawidłowy ruch. Pole zajęte lub poza zakresem.')
            except ValueError:
                print('Nieprawidłowe wejście. Wprowadź liczbę od 0 do 8.')
        return val

def play(game, x_player, o_player, print_game=True):
    # Główna pętla gry
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Zaczyna 'X'
    while game.empty_squares():
        if letter == 'O':
            position = o_player.get_move(game)
        else:
            position = x_player.get_move(game)

        if game.make_move(position, letter):
            if print_game:
                print(f"{letter} wykonał ruch na polu {position}")
                game.print_board()
                print('')  # Pusta linia

            if game.current_winner:
                if print_game:
                    print(f"{letter} wygrywa!")
                return letter  # Koniec gry
            # Zmiana gracza
            letter = 'O' if letter == 'X' else 'X'
        else:
            if print_game:
                print('Nieprawidłowy ruch. Spróbuj ponownie.')

    if print_game:
        print("Remis!")

if __name__ == '__main__':
    # Rozpoczęcie gry między dwoma graczami
    x_player = HumanPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player)