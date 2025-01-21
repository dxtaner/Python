def cardPackets(cardTypes):
    # Minimum paket sayısını bulmak için kart türlerini sıralayın
    cardTypes.sort()

    # Minimum ve maksimum paket sayısını belirleyin
    min_packets = 2  # En az 2 paket gerekecektir
    # Maksimum paket sayısı en yüksek kart sayısına eşittir
    max_packets = cardTypes[-1]

    min_additional_cards = float('inf')  # Başlangıçta sonsuz bir değer atayın

    # Minimum ek kart sayısını hesaplayın
    for num_packets in range(min_packets, max_packets + 1):
        additional_cards = 0

        for quantity in cardTypes:
            target_quantity = num_packets * (quantity // num_packets)
            additional_cards += abs(quantity - target_quantity)

        min_additional_cards = min(min_additional_cards, additional_cards)

    return min_additional_cards


# Örnek giriş
cardTypes = [3, 9, 7, 6, 5, 2]

# İşlevi çağırın ve sonucu yazdırın
result = cardPackets(cardTypes)
print("Minimum ek kart sayısı:", result)
