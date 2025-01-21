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


# Fonksiyonu çağırdık ve sonucu aldık
result = ArrayChallenge([44, 30, 24, 32, 35, 30, 40, 38, 15])

# ChallengeToken
challenge_token = "nfq4398t7c"

# Sonuç dizesini aldık ve tüm harfleri küçük harfe çevirdik
result_string = str(result)
result_string_lower = result_string.lower()

# ChallengeToken'daki karakterleri çıkardık
for char in challenge_token:
    result_string_lower = result_string_lower.replace(char.lower(), "")

# Eğer sonuç dizesi boşsa "EMPTY" döndürdük, aksi halde sonucu döndürdük
if not result_string_lower:
    print("EMPTY")
else:
    print(result_string_lower)
