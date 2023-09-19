from scipy.optimize import linprog

# Taşıma maliyetleri (fabrikalar x depolar)
c = [5, 7, 6, 8, 10, 8, 9, 6, 7, 12, 14, 5]

# Fabrikaların arzları
A_eq = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]]

# Depoların talepleri
b_eq = [20, 30, 25]

# Her taşıma işleminin üst sınırları
bounds = [(0, None) for _ in range(12)]

# Lineer programlama çözümü
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Çözümü görüntüleme
print("Çözüm:")
print(result.x)
print("Toplam Maliyet:", result.fun)
