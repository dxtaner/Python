import random
import tkinter as tk
from tkinter import messagebox


class EslestirmeOyunu:
    def __init__(self, pencere, kartlar):
        self.pencere = pencere
        self.kartlar = kartlar
        self.acik_kartlar = []
        self.oyun_sonu = False

        random.shuffle(self.kartlar)

        self.kart_butonlari = []
        for kart in self.kartlar:
            kart_butonu = tk.Button(
                self.pencere, image=kart, command=lambda k=kart: self.kart_ac(k))
            kart_butonu.pack(side=tk.LEFT)
            self.kart_butonlari.append(kart_butonu)

    def kart_ac(self, kart):
        if not self.oyun_sonu:
            if kart in self.acik_kartlar:
                messagebox.showinfo("Hata", "Bu kartı zaten açtınız!")
            else:
                index = self.kartlar.index(kart)
                self.kart_butonlari[index].config(state=tk.DISABLED)
                self.acik_kartlar.append(kart)

                if len(self.acik_kartlar) == 2:
                    self.pencere.after(1000, self.kart_kapat)

    def kart_kapat(self):
        if not self.oyun_sonu:
            if self.acik_kartlar[0] == self.acik_kartlar[1]:
                self.acik_kartlar.clear()
                self.kontrol_oyunu_sonu()
            else:
                index1 = self.kartlar.index(self.acik_kartlar[0])
                index2 = self.kartlar.index(self.acik_kartlar[1])
                self.kart_butonlari[index1].config(state=tk.NORMAL)
                self.kart_butonlari[index2].config(state=tk.NORMAL)
                self.acik_kartlar.clear()

    def kontrol_oyunu_sonu(self):
        if all(kart.config()["state"][4] == tk.DISABLED for kart in self.kart_butonlari):
            messagebox.showinfo(
                "Oyun Bitti", "Tebrikler! Tüm kartları eşleştirdiniz.")
            self.oyun_sonu = True


pencere = tk.Tk()
pencere.title("İskambil Eşleştirme Oyunu")

kart1 = tk.PhotoImage(file="kart1.png")
kart2 = tk.PhotoImage(file="kart2.png")
kart3 = tk.PhotoImage(file="kart3.png")
kart4 = tk.PhotoImage(file="kart4.png")

kartlar = [kart1, kart2, kart3, kart4] * 4

oyun = EslestirmeOyunu(pencere, kartlar)

pencere.mainloop()
