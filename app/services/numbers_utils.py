from functools import lru_cache

def is_prime_number(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_number(n):
    """
    Check if a number is a perfect number.
    """
    if n <= 0:
        return False
    
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

def is_armstrong_number(n):
    """
    Check if a number is an Armstrong number.
    """
     # Convert number to list of digits
    digits = [int(d) for d in str(n)]
    # Check if sum of digits raised to power of digit count equals number
    return sum(d**len(digits) for d in digits) == n

def digit_sum(n):
    """
    Calculate the sum of digits.
    """
    return sum(int(digit) for digit in str(n))

@lru_cache(maxsize=1000)
def classify_number(number):
    """
    Classify number with various mathematical properties.
    """
    properties = []
    # check even or odd
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Armstrong number check
    if is_armstrong_number(number):
        properties.append("armstrong")
    
    return {
        "is_prime": is_prime_number(number),
        "is_perfect": is_perfect_number(number),
        "properties": properties,
        "digit_sum": digit_sum(number)
    }
