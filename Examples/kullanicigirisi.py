kullanici="taner"
sifre="1234"

ad=input("Kullanıcı adı girin :")
parola=input("Şifre girin:")

if ad==kullanici and parola==sifre:
    print("Giriş Başaralı")
elif ad!=kullanici and parola==sifre:
    print("Kullanıcı adı yanlış")
elif ad==kullanici and parola!=sifre:
    print("Şifre yanlış")
else:
    print("Kulanıcı adı ve şifre yalış")