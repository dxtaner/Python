import random
import tkinter as tk
from tkinter import messagebox


class BatakOyunu:
    def __init__(self, pencere):
        self.pencere = pencere
        self.kartlar = [
            "AS", "PAPAZ", "KIZ", "VALE", "10", "9", "8", "7", "6", "5", "4", "3", "2"
        ]
        self.seriler = [
            "Sinek", "Kupa", "Karo", "Maça"
        ]
        self.destede_kartlar = [(kart, seri)
                                for seri in self.seriler for kart in self.kartlar]
        random.shuffle(self.destede_kartlar)

        self.oyuncu_el = []
        self.bilgisayar_el = []
        self.masa = []

        for _ in range(13):
            self.oyuncu_el.append(self.destede_kartlar.pop())
            self.bilgisayar_el.append(self.destede_kartlar.pop())

        self.masa = self.destede_kartlar[-4:]
        self.destede_kartlar = self.destede_kartlar[:-4]

        self.oyuncu_label = tk.Label(self.pencere, text="Oyuncu El:")
        self.oyuncu_label.pack()

        self.oyuncu_el_label = tk.Label(self.pencere, text=self.oyuncu_el)
        self.oyuncu_el_label.pack()

        self.masa_label = tk.Label(self.pencere, text="Masa:")
        self.masa_label.pack()

        self.masa_kart_label = tk.Label(self.pencere, text=self.masa)
        self.masa_kart_label.pack()

        self.bilgisayar_label = tk.Label(self.pencere, text="Bilgisayar El:")
        self.bilgisayar_label.pack()

        self.bilgisayar_el_label = tk.Label(
            self.pencere, text=self.bilgisayar_el)
        self.bilgisayar_el_label.pack()

        self.oyuncu_kart_sec_button = tk.Button(
            self.pencere, text="Kart Seç", command=self.oyuncu_kart_sec)
        self.oyuncu_kart_sec_button.pack()

    def oyuncu_kart_sec(self):
        kart = random.choice(self.oyuncu_el)
        self.oyuncu_el.remove(kart)
        self.masa.append(kart)

        self.oyuncu_el_label.config(text=self.oyuncu_el)
        self.masa_kart_label.config(text=self.masa)

        if len(self.oyuncu_el) == 0:
            self.oyuncu_kart_sec_button.config(state=tk.DISABLED)
            self.bilgisayar_oyna()

    def bilgisayar_oyna(self):
        kart = random.choice(self.bilgisayar_el)
        self.bilgisayar_el.remove(kart)
        self.masa.append(kart)

        self.masa_kart_label.config(text=self.masa)
        self.bilgisayar_el_label.config(text=self.bilgisayar_el)

        if len(self.bilgisayar_el) == 0:
            self.bilgisayar_kazandi()

    def bilgisayar_kazandi(self):
        messagebox.showinfo("Oyun Bitti", "Bilgisayar kazandı!")
        self.pencere.destroy()


pencere = tk.Tk()
pencere.title("Batak Oyunu")

oyun = BatakOyunu(pencere)

pencere.mainloop()
