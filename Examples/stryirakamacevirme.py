def custom_parse_int(str):
    result = 0
    for char in str:
        if char.isdigit():
            digit = int(char)
            result = result * 10 + digit
        else:
            break
    return result

str_metin = "14"
d_sonuc = custom_parse_int(str_metin)
print(d_sonuc)  # 14 çıktısı alınır
