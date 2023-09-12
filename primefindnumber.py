# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main function to find and display prime numbers


def find_prime_numbers():
    # Initialize an empty list to store prime numbers
    prime_numbers = []

    # Iterate through numbers from 500 to 599 (3 digits starting with 5)
    for num in range(500, 600):
        # Check if the number is prime
        if is_prime(num):
            # If prime, add it to the list
            prime_numbers.append(num)

    # Display the list of prime numbers
    print("Prime numbers with 3 digits starting with 5:")
    for prime in prime_numbers:
        print(prime)


# Call the main function to find and display prime numbers
find_prime_numbers()
