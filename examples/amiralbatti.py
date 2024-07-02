import random


def display_board(board):
    print("\n\t\t  0 1 2 3 4 5 6 7 8 9")
    for i in range(10):
        print(f"\t\t{chr(i + 65)}  ", end="")
        for j in range(10):
            print(board[i][j], end=" ")
        print()


def place_ships(ships, quantities, table):
    for i, ship_size in enumerate(ships):
        for _ in range(quantities[i]):
            while True:
                direction = random.randint(0, 1)  # 0 for down, 1 for right
                y = random.randint(0, 9)
                x = random.randint(0, 9)
                if direction == 0:
                    if y + ship_size <= 10:
                        hata = False
                        for n in range(ship_size):
                            if table[y + n][x] != '-':
                                hata = True
                                break
                        if hata:
                            continue
                        else:
                            for n in range(ship_size):
                                table[y + n][x] = 'O'
                            break
                else:
                    if x + ship_size <= 10:
                        hata = False
                        for n in range(ship_size):
                            if table[y][x + n] != '-':
                                hata = True
                                break
                        if hata:
                            continue
                        else:
                            for n in range(ship_size):
                                table[y][x + n] = 'O'
                            break


def play(turns, player_table, opponent_table):
    display_board(player_table)
    while turns > 0:
        print(f"\n\tHak Sayisi = {turns}, Kalan Vurulacak Alan = {
              count_remaining(opponent_table)}")
        coordinate = input(
            "\tOnce Karakteri Sonra Sayiyi Girerek\n\tHamlenizi Yapacaginiz Koordinatlari Giriniz-->")
        try:
            x, y = int(coordinate[1]), ord(coordinate[0].upper()) - 65
            if 0 <= x <= 9 and 0 <= y <= 9:
                if opponent_table[y][x] == '-':
                    if player_table[y][x] == 'O':
                        opponent_table[y][x] = 'X'
                    else:
                        opponent_table[y][x] = 'O'
                        turns -= 1
                else:
                    print("\n\tZaten Daha Once Bu Konumu Kullandiniz.")
            else:
                print("\n\tYanlis Girildi.")
        except (IndexError, ValueError):
            print("\n\tYanlis Girildi.")
        display_board(player_table)
    print("\n\t\t  HAKKINIZ BITTI!")


def count_remaining(table):
    return sum(row.count('O') for row in table)


def main():
    player_board = [['-' for _ in range(10)] for _ in range(10)]
    opponent_board = [['-' for _ in range(10)] for _ in range(10)]

    ships = [5, 4, 3, 2]
    quantities = [1, 2, 3, 4]

    place_ships(ships, quantities, player_board)
    place_ships(ships, quantities, opponent_board)

    print("OYUN MODU:")
    print("1. Kolay")
    print("2. Orta")
    print("3. Zor")
    mode = input("Seçiminizi yapınız (1/2/3): ")

    if mode == '1':
        turns = sum(quantities) * 2
    elif mode == '2':
        turns = int(sum(quantities) * 1.5)
    elif mode == '3':
        turns = sum(quantities)
    else:
        print("Geçersiz oyun modu seçimi!")
        return

    print("\nSıra sizde...")
    play(turns, player_board, opponent_board)
    player_score = sum(ships) * sum(quantities) - count_remaining(player_board)
    opponent_score = sum(ships) * sum(quantities) - \
        count_remaining(opponent_board)

    print(f"\n1. Oyuncunun Puanı: {player_score}")
    print(f"2. Oyuncunun Puanı: {opponent_score}")

    if player_score > opponent_score:
        print("1. Oyuncu Kazandı!")
    elif player_score < opponent_score:
        print("2. Oyuncu Kazandı!")
    else:
        print("Berabere!")


if __name__ == "__main__":
    main()
