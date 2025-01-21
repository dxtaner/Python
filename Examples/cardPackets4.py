def cardPackets(cardTypes):
    cards_required = 0

    # Her kart türü için ek kart sayısını hesaplayın ve maksimuma ekleyin
    for quantity in cardTypes:
        additional_cards = quantity % 2
        cards_required += additional_cards

    # En az iki paket olacak şekilde düzenleme yapın
    if cards_required % 2 != 0:
        cards_required += 1

    return cards_required


# Örnek giriş
cardTypes = [3, 9, 7, 6, 5, 2]

# İşlevi çağırın ve sonucu yazdırın
result = cardPackets(cardTypes)
print("Minimum ek kart sayısı (en az iki paket):", result)
