#dxtaner
def isPrime(number):
    if (number <= 1 ):
        return False
    isPrime = True
    for i in range(2, int(number/2)):
        if number % i == 0:
            isPrime = False
    return isPrime

def main():
    with open("number.txt", 'r') as file:
        triangle = file.readlines()

    arr = list()
    for t in triangle:
        numbers = t.split(" ")
        arr.append(numbers)

    for i in range(0, len(arr)):
        for j in range(0, i + 1):
            arr[i][j] = int(arr[i][j])

    for i in range(0, len(arr)):
        for j in range(0, i + 1):
            if isPrime(arr[i][j]):
                arr[i][j] = -555

    for i in range(len(arr) - 1, -1, -1):
        for j in range(0, i):
            arr[i - 1][j] += max(arr[i][j], arr[i][j + 1])

    print("Max :",arr[0])

if __name__ == "__main__":
    main();