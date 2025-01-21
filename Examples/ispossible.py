def isPossible(a, b, c, d):
    if a == c and b == d:
        return 'Yes'
    elif a > c or b > d:
        return 'No'
    else:
        # Try both possible operations
        result1 = isPossible(a + b, b, c, d)
        result2 = isPossible(a, a + b, c, d)
        
        if result1 == 'Yes' or result2 == 'Yes':
            return 'Yes'
        else:
            return 'No'

# Input from stdin
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Call the function and print the result
print(isPossible(a, b, c, d))
