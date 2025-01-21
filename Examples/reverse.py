def kelime_ters_cevir(dizi):
    # Giriş dizisini boşluklara göre ayrı kelimelere bölen bir liste
    kelimeler_listesi = dizi.split()

    # Kelimelerin listesini tersine çevirme
    ters_kelimeler_listesi = kelimeler_listesi[::-1]

    # Tersine çevrilmiş kelimeleri tekrar tek bir dizeye boşlukla birleştirme
    ters_dizi = ' '.join(ters_kelimeler_listesi)

    return ters_dizi


# Örnek kullanım:
giris_dizi_1 = "The weather is so sunny nowadays"
cikti_dizi_1 = kelime_ters_cevir(giris_dizi_1)
print(cikti_dizi_1)

giris_dizi_2 = "Life is so beautiful"
cikti_dizi_2 = kelime_ters_cevir(giris_dizi_2)
print(cikti_dizi_2)
