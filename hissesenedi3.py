def ArrayChallenge(arr):
    if len(arr) < 2:
        return -1

    max_profit = -1
    min_price = arr[0]

    for price in arr:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


# Example cases
print(ArrayChallenge([10, 12, 4, 5, 9]))  # Output: 5
print(ArrayChallenge([14, 20, 4, 12, 5, 11]))  # Output: 8
