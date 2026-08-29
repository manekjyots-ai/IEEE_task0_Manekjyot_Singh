"""
Define a function is_prime(n) that returns True if n is prime and
False otherwise.
"""

def is_prime(n):
    # Numbers less than 2 are never prime (0, 1, negatives)
    if n < 2:
        return False

    # Only need to check factors up to sqrt(n) for optimality
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            # Found a factor, so n is NOT prime
            return False
    else:
        # Getting here means no factor was found, so n IS prime.
        return True

# Sampling an input number
test_value = int(input("Enter a number to check if it's prime: "))
print("The number inputted is prime (T/F):", is_prime(test_value))