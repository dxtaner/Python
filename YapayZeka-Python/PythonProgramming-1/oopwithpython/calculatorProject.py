class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        else:
            return a / b


# Example usage:
calc = Calculator()

# Addition
result_add = calc.add(5, 3)
print("Addition:", result_add)  # Output: 8

# Subtraction
result_sub = calc.subtract(8, 3)
print("Subtraction:", result_sub)  # Output: 5

# Multiplication
result_mul = calc.multiply(4, 6)
print("Multiplication:", result_mul)  # Output: 24

# Division
result_div = calc.divide(10, 2)
print("Division:", result_div)  # Output: 5.0

# Division by zero
result_div_error = calc.divide(5, 0)
# Output: Error: Division by zero!
print("Division by zero:", result_div_error)
