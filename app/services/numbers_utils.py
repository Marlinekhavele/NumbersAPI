def is_prime_numbers(n):
    if n <= 1:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_numbers(n):
    # Perfect numbers are positive
    if n <= 0:
        return False
    
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

def is_armstrong_number(n):
    # Handle negative numbers
    n = abs(n)
    digits = [int(d) for d in str(n)]
    return sum(d**len(digits) for d in digits) == n

def digit_sum(n):
    # Use absolute value for digit sum
    return sum(int(digit) for digit in str(abs(n)))

def classify_number(number):
    # Absolute value for consistent processing
    number = abs(number)
    
    properties = []
    
    if number % 2 == 0:
        properties = ["armstrong", "even"] if is_armstrong_number(number) else ["even"]
    else:
        properties = ["armstrong", "odd"] if is_armstrong_number(number) else ["odd"]
    
    return {
        "is_prime": is_prime_numbers(number),
        "is_perfect": is_perfect_numbers(number),
        "properties": properties,
        "digit_sum": digit_sum(number)
    }