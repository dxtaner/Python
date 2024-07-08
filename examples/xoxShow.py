import tkinter as tk
from tkinter import messagebox


class XOXOyunu:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("XOXOyunu Oyunu")
        self.tahta = [[" " for _ in range(3)] for _ in range(3)]
        self.oyuncular = ["X", "O"]
        self.sira = 0

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(pencere, text="", font=("normal", 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.hamle_yap(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def hamle_yap(self, satir, sutun):
        if self.tahta[satir][sutun] == " ":
            oyuncu = self.oyuncular[self.sira % 2]
            self.tahta[satir][sutun] = oyuncu
            self.buttons[satir][sutun].config(
                text=oyuncu, state="disabled", disabledforeground="black")
            self.sira += 1

            if self.oyun_kazanan(oyuncu):
                messagebox.showinfo("Sonuç", f"{oyuncu} kazandı!")
                self.pencere.quit()
            elif self.oyun_berabere():
                messagebox.showinfo("Sonuç", "Oyun berabere bitti!")
                self.pencere.quit()

    def oyun_kazanan(self, oyuncu):
        for i in range(3):
            if all(self.tahta[i][j] == oyuncu for j in range(3)) or all(self.tahta[j][i] == oyuncu for j in range(3)):
                return True
        if all(self.tahta[i][i] == oyuncu for i in range(3)) or all(self.tahta[i][2 - i] == oyuncu for i in range(3)):
            return True
        return False

    def oyun_berabere(self):
        return all(self.tahta[i][j] != " " for i in range(3) for j in range(3))


if __name__ == "__main__":
    root = tk.Tk()
    oyun = XOXOyunu(root)
    root.mainloop()
