def ArrayChallenge(arr):
    if len(arr) < 2:
        return -1  # Hisse senedi fiyatlarından kâr elde edilemiyor.

    max_profit = 0
    min_price = arr[0]

    for price in arr:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    if max_profit == 0:
        return -1  # Hisse senedi fiyatlarından kâr elde edilemiyor.
    else:
        return max_profit


# Testlerin sonuçlarını saklamak için bir liste oluşturalım
results = []

# İlk test
result1 = ArrayChallenge([10, 12, 4, 5, 9])
results.append(result1)

# İkinci test
result2 = ArrayChallenge([14, 20, 4, 12, 5, 11])
results.append(result2)


# Sonuçları ChallengeToken'a göre düzenleyip yazdıralım
challenge_token = "nfq4398t7c"
for result in results:
    result_string = str(result)
    result_string_lower = result_string.lower()

    for char in challenge_token:
        result_string_lower = result_string_lower.replace(char.lower(), "")

    if not result_string_lower:
        print("EMPTY")
    else:
        print(result_string_lower)
