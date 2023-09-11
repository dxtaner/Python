import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "gonderen@example.com"  # Gönderen mail adresi
mesaj["To"] = "alici@example.com"  # Alıcı mail adresi
mesaj["Subject"] = "Smtp Mail Gönderme"

yazi = """
smtp ile gönderdim
1-2-3----

taner ozer

"""

mesajgovdesi = MIMEText(yazi, "plain")
mesaj.attach(mesajgovdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    # E-posta adresi ve şifre
    mail.login("your_email@gmail.com", "your_password")
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail Gönderildi..")
    mail.close()
except:
    sys.stderr.write("Bir hata oluştu...")
    sys.stderr.flush()
