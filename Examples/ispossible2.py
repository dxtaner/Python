def isPossible(a, b, c, d):
    if a == c and b == d:
        return 'Evet'

    # (a, b) çiftini temsil eden bir anahtar kullanarak bir bellek (cache) oluşturun
    cache = {}

    # Yardımcı bir iç işlev tanımlayın
    def dp(x, y):
        # İşlem sonucunu cache'ten kontrol edin
        if (x, y) in cache:
            return cache[(x, y)]

        # İlk işlemi (a, b) çiftiyle başlatın
        result1 = dp(x + y, y)
        result2 = dp(x, x + y)

        # Eğer herhangi bir işlem sonucu 'Evet' ise sonucu 'Evet' olarak işaretleyin
        if result1 == 'Evet' or result2 == 'Evet':
            cache[(x, y)] = 'Evet'
            return 'Evet'

        # İşlem sonucunu 'Hayır' olarak işaretleyin ve cache'e kaydedin
        cache[(x, y)] = 'Hayır'
        return 'Hayır'

    # İlk işlemi başlatın ve sonucu döndürün
    return dp(a, b)


# Stdin'den giriş oku
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# İşlevi çağırın ve sonucu yazdırın
print(isPossible(a, b, c, d))
