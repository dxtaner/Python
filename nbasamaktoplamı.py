def solution(N):
    def digit_sum(num):
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total

    target_sum = digit_sum(N)

    while True:
        N += 1
        if digit_sum(N) == target_sum:
            return N


# Örnekler
N1 = 28
solution_N1 = solution(N1)
print(f"{N1} için çözüm: {solution_N1}")

N2 = 734
solution_N2 = solution(N2)
print(f"{N2} için çözüm: {solution_N2}")

N3 = 1990
solution_N3 = solution(N3)
print(f"{N3} için çözüm: {solution_N3}")

N4 = 1000
solution_N4 = solution(N4)
print(f"{N4} için çözüm: {solution_N4}")
