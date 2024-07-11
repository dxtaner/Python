class NineMensMorris:
    def __init__(self):
        self.board = [" " for _ in range(24)]  # 24 noktalı oyun tahtası
        self.player1 = "X"
        self.player2 = "O"
        self.current_player = self.player1

    def display_board(self):
        print(
            f"{self.board[0]}----------{self.board[1]}----------{self.board[2]}")
        print(f"|          |          |")
        print(
            f"|   {self.board[3]}------{self.board[4]}------{self.board[5]}   |")
        print(f"|   |      |      |   |")
        print(
            f"{self.board[6]}---{self.board[7]}--{self.board[8]}   {self.board[9]}--{self.board[10]}---{self.board[11]}")
        print(f"|   |      |      |   |")
        print(
            f"|   {self.board[12]}------{self.board[13]}------{self.board[14]}   |")
        print(f"|          |          |")
        print(
            f"{self.board[15]}----------{self.board[16]}----------{self.board[17]}")

    def is_valid_move(self, move):
        if move < 0 or move > 23 or self.board[move] != " ":
            return False
        return True

    def make_move(self, move):
        self.board[move] = self.current_player

    def is_mill(self, move):
        lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11),
                 (12, 13, 14), (15, 16, 17), (0, 6, 12), (1, 7, 13),
                 (2, 8, 14), (3, 9, 15), (4, 10, 16), (5, 11, 17),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8), (12, 13, 14), (15, 16, 17))

        for line in lines:
            if move in line:
                if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] == self.current_player:
                    return True
        return False

    def remove_piece(self, move):
        self.board[move] = " "

    def play(self):
        while True:
            self.display_board()
            print(f"Oyuncu {self.current_player}'in sırası.")
            move = int(input("Taşın konumunu seçin (0-23): "))
            if self.is_valid_move(move):
                self.make_move(move)
                if self.is_mill(move):
                    remove = int(input(
                        "Bir değirmen oluşturdunuz, rakibin taşını çıkarmak için konum seçin (0-23): "))
                    if self.board[remove] == self.player2:
                        self.remove_piece(remove)
                self.current_player = self.player1 if self.current_player == self.player2 else self.player2
            else:
                print("Geçersiz hamle. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    game = NineMensMorris()
    game.play()
