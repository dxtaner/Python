import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys


def eposta_gonder(gonderen, alici, konu, icerik, smtp_sunucusu, smtp_port, kullanici_adi, sifre):
    msg = MIMEMultipart()
    msg['From'] = gonderen
    msg['To'] = alici
    msg['Subject'] = konu
    msg.attach(MIMEText(icerik, 'plain'))

    try:
        server = smtplib.SMTP(smtp_sunucusu, smtp_port)
        server.starttls()
        server.login(kullanici_adi, sifre)
        server.sendmail(gonderen, alici, msg.as_string())
        server.quit()
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print("E-posta gönderilirken hata oluştu:", e)


# Kullanım örneği
gonderen = "gonderen@mail.com"
alici = "alici@mail.com"
konu = "mail E-postası"
icerik = "bu bir test mail e-postasıdır."
smtp_sunucusu = "smtp.example.com"
smtp_port = 587
kullanici_adi = "username"
sifre = "password"

eposta_gonder(gonderen, alici, konu, icerik, smtp_sunucusu,
              smtp_port, kullanici_adi, sifre)
