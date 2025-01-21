def solution(s):
    unique_chars = set(s)
    max_count = 0

    for char in unique_chars:
        char_count = s.count(char)
        max_count = max(max_count, char_count)

    return max_count


string = "hello world"
print(solution(string))
# Örnekler
print(solution('world'))  # 1
print(solution('dddd'))   # 4
print(solution('cycle'))  # 2
print(solution('abba'))   # 2
