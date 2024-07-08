def tahta_goster(tahta):
    for row in tahta:
        print(" | ".join(row))
        print("-" * 9)


def tahta_olustur():
    return [[" " for _ in range(3)] for _ in range(3)]


def hamle_yap(tahta, oyuncu, satir, sutun):
    if tahta[satir][sutun] == " ":
        tahta[satir][sutun] = oyuncu
        return True
    else:
        print("Bu hücre dolu. Lütfen başka bir hücre seçin.")
        return False


def oyun_kazanan(tahta, oyuncu):
    for i in range(3):
        if all(tahta[i][j] == oyuncu for j in range(3)) or all(tahta[j][i] == oyuncu for j in range(3)):
            return True
    if all(tahta[i][i] == oyuncu for i in range(3)) or all(tahta[i][2 - i] == oyuncu for i in range(3)):
        return True
    return False


def oyun_bitis(tahta):
    return all(tahta[i][j] != " " for i in range(3) for j in range(3))


def main():
    tahta = tahta_olustur()
    oyuncular = ["X", "O"]
    sira = 0

    while not oyun_bitis(tahta):
        tahta_goster(tahta)
        oyuncu = oyuncular[sira % 2]
        print(f"{oyuncu}'nın sırası.")
        satir = int(input("Satır seçin (0, 1, 2): "))
        sutun = int(input("Sütun seçin (0, 1, 2): "))
        if 0 <= satir < 3 and 0 <= sutun < 3:
            if hamle_yap(tahta, oyuncu, satir, sutun):
                if oyun_kazanan(tahta, oyuncu):
                    tahta_goster(tahta)
                    print(f"{oyuncu} kazandı!")
                    break
                sira += 1
        else:
            print("Geçersiz giriş. Lütfen satır ve sütunları 0, 1 veya 2 arasında seçin.")


if __name__ == "__main__":
    main()
