def solution(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    max_count = max(char_count.values())

    return max_count


# Örnekler
print(solution('world'))  # 1
print(solution('dddd'))   # 4
print(solution('cycle'))  # 2
print(solution('abba'))   # 2
