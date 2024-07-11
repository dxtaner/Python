import random
import tkinter as tk
from tkinter import messagebox


class BlofOyunu:
    def __init__(self):
        self.oyuncular = None
        self.kartlar = [1, 2, 3, 4, 5, 6]
        self.elindeki_kartlar = {}
        self.oyuncu_sirasi = None

        self.pencere = tk.Tk()
        self.pencere.title("Blöf Oyunu")

        self.label1 = tk.Label(self.pencere, text="Oyuncu Sayısı:")
        self.label1.pack()

        self.oyuncu_sayisi_entry = tk.Entry(self.pencere)
        self.oyuncu_sayisi_entry.pack()

        self.button = tk.Button(
            self.pencere, text="Başlat", command=self.oyunu_baslat)
        self.button.pack()

    def oyunu_baslat(self):
        self.oyuncular = int(self.oyuncu_sayisi_entry.get())
        random.shuffle(self.kartlar)

        for i in range(self.oyuncular):
            self.elindeki_kartlar[i+1] = self.kartlar.pop()

        self.oyuncu_sirasi = random.randint(1, self.oyuncular)
        self.pencere.destroy()
        self.oyun_ekrani()

    def oyun_ekrani(self):
        self.pencere = tk.Tk()
        self.pencere.title("Blöf Oyunu")
        self.pencere.geometry("400x300")  # Ekrana uygun bir boyut belirleyin

        oyuncu_sira_label = tk.Label(
            self.pencere, text="Sıra oyuncuda: " + str(self.oyuncu_sirasi))
        oyuncu_sira_label.pack()

        elindeki_kart_label = tk.Label(
            self.pencere, text="Elinizdeki kart: " + str(self.elindeki_kartlar[self.oyuncu_sirasi]))
        elindeki_kart_label.pack()

        blöf_evet_button = tk.Button(
            self.pencere, text="Blöf Mü? (E)", command=self.blof_yap)
        blöf_evet_button.pack()

        blöf_hayir_button = tk.Button(
            self.pencere, text="Blöf Mü? (H)", command=self.blof_yapma)
        blöf_hayir_button.pack()

    def blof_yap(self):
        blöf_pencere = tk.Tk()
        blöf_pencere.title("Blöf Yap")
        blöf_pencere.geometry("300x200")  # Ekrana uygun bir boyut belirleyin

        tahmin_kart_label = tk.Label(
            blöf_pencere, text="Tahmin Ettiğiniz Kart:")
        tahmin_kart_label.pack()

        tahmin_kart_entry = tk.Entry(blöf_pencere)
        tahmin_kart_entry.pack()

        tahmin_adet_label = tk.Label(
            blöf_pencere, text="Tahmin Ettiğiniz Kart Adedi:")
        tahmin_adet_label.pack()

        tahmin_adet_entry = tk.Entry(blöf_pencere)
        tahmin_adet_entry.pack()

        blöf_button = tk.Button(blöf_pencere, text="Blöf Yap", command=lambda: self.blöf_kontrol(
            blöf_pencere, tahmin_kart_entry.get(), tahmin_adet_entry.get()))
        blöf_button.pack()

    def blöf_kontrol(self, pencere, tahmin_kart, tahmin_adet):
        pencere.destroy()

        toplam_adet = 0
        for kart in self.elindeki_kartlar.values():
            if kart == int(tahmin_kart):
                toplam_adet += 1

        if toplam_adet >= int(tahmin_adet):
            messagebox.showinfo("Blöf Sonucu", "Tebrikler! Blöfü geçtiniz.")
        else:
            messagebox.showinfo(
                "Blöf Sonucu", "Blöfünüz başarısız oldu. Doğru değerleri söylemediniz.")
            messagebox.showinfo(
                "Blöf Sonucu", "Elinizdeki kartlar: " + str(self.elindeki_kartlar))
            self.pencere.destroy()

        self.oyuncu_sirasi = self.oyuncu_sirasi % self.oyuncular + 1
        self.oyun_ekrani()

    def blof_yapma(self):
        self.oyuncu_sirasi = self.oyuncu_sirasi % self.oyuncular + 1
        self.oyun_ekrani()


oyun = BlofOyunu()
oyun.pencere.mainloop()
