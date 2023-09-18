def parantez_eslesme_kontrolu(metin):
    stack = []  # Parantezleri saklayacak olan stack

    # Metin içindeki her karakteri kontrol edin
    for karakter in metin:
        if karakter in "([{":
            # Eğer karakter açma parantezi ise, stack'e ekleyin
            stack.append(karakter)
        elif karakter in ")]}":
            # Eğer karakter kapama parantezi ise, stack'ten son eklenen açma parantezi çıkarın ve eşleşip eşleşmediğini kontrol edin
            if not stack:
                return False  # Açma parantez yoksa eşleşmez
            son_acma_parantez = stack.pop()
            if (karakter == ")" and son_acma_parantez != "(") or \
               (karakter == "]" and son_acma_parantez != "[") or \
               (karakter == "}" and son_acma_parantez != "{"):
                return False  # Eşleşmeyen bir kapama parantezi varsa, eşleşmez

    # Stack hala eleman içeriyorsa eşleşmez
    return len(stack) == 0


# Test
metin1 = "({})"
metin2 = "({[}])"

if parantez_eslesme_kontrolu(metin1):
    print(f"'{metin1}' doğru parantez eşleşmesi.")
else:
    print(f"'{metin1}' yanlış parantez eşleşmesi.")

if parantez_eslesme_kontrolu(metin2):
    print(f"'{metin2}' doğru parantez eşleşmesi.")
else:
    print(f"'{metin2}' yanlış parantez eşleşmesi.")
