def solution(s):
    result = []     # Alt dizileri tutacak liste
    current = ""    # Mevcut alt diziyi oluşturmak için kullanılan string

    for char in s:
        if char not in current:
            if current:
                result.append(current)
            current = char
        else:
            current += char

    result.append(current)  # Son alt diziyi ekle

    return len(result)  # Minimum alt dizi sayısını döndür


# Örnekler
print(solution('world'))  # 1
print(solution('dddd'))   # 4
print(solution('Cycle'))  # 2
print(solution('abba'))   # 2
