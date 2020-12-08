import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj=MIMEMultipart()

mesaj["From"] = "" #gonderen mail adresi
mesaj["To"] = "" #alici mail adresi
mesaj["Subject"] = "Smtp Mail Gönderme"

yazi="""
smtp ile gonderdim
1-2-3----

taner ozer

"""

mesajgovdesi=MIMEText(yazi,"plain")
mesaj.attach(mesajgovdesi)

try:
    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("","") #mail adresi ve sifremiz
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("Mail Gönderildi..")
    mail.close()
except:
    sys.stderr.write("bir hata olustu...")
    sys.stderr.flush()