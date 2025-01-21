def solution(A, K):
    n = len(A)
    best = 0
    count = 1

    for i in range(n - 1):
        if A[i] == A[i + 1]:
            count += 1
        else:
            best = max(best, count)
            count = 1

    best = max(best, count)
    result = best + K

    return min(result, n)  # en fazla N kadar çivi varsa, sonuç N olmalı


# Test
A = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
K = 2
print(solution(A, K))  # 5


def solution(A, K):
    n = len(A)
    best = 0
    count = 1
    for i in range(n - 1):
        if (A[i] == A[i + 1]):
            count = count + 1
        else:
            count = 0
        best = max(best, count)
    result = best + K

    return result
