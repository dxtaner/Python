def is_palindrome(input_string):
    input_string = input_string.lower().replace(" ", "")
    stack = []

    for char in input_string:
        stack.append(char)

    reversed_string = ""
    while len(stack) > 0:
        reversed_string += stack.pop()

    return input_string == reversed_string


is_palindrome("alisa")
