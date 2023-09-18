class MersennePrimeFinder:
    def __init__(self, limit):
        self.limit = limit
        self.primes = []
        self.calculate_mersenne_primes()

    def is_prime(self, number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def calculate_mersenne_primes(self):
        # Mersenne asal sayılar 2^p - 1 şeklinde ifade edilir, bu n değerini temsil eder.
        n = 2
        while len(self.primes) < self.limit:
            candidate = 2 ** n - 1  # Mersenne adayı hesapla
            if self.is_prime(candidate):  # Eğer bu aday bir asal sayı ise
                # Mersenne asal sayılar listesine ekle
                self.primes.append(candidate)
            n += 1

    def get_mersenne_primes(self):
        return self.primes


# İstenen sayıda Mersenne asal sayısını bul
limit = 5  # Örneğin ilk 5 Mersenne asal sayısını bulmak için
prime_finder = MersennePrimeFinder(limit)

# Bulunan Mersenne asal sayılarını al
mersenne_primes = prime_finder.get_mersenne_primes()

# Sonuçları görüntüle
print(f"İlk {limit} Mersenne Asal Sayısı:")
for prime in mersenne_primes:
    print(prime)
