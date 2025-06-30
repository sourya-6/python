def sum_to_single_digit(n):
    while n >= 10:
        total = 0
        while n:
            total += n % 10
            n //= 10
        n = total
    return n

def get_registration_cost(num):
    if num < 0 or num > 9999:
        return "Invalid number"

    digits = [
        (num // 1000) % 10,
        (num // 100) % 10,
        (num // 10) % 10,
        num % 10
    ]

    # All 4 digits are the same
    if digits.count(digits[0]) == 4:
        return 100000

    # Sequential check (limited)
    if num in [1234, 2345, 3456, 4567, 5678, 6789]:
        return 110000

    # Last 3 digits same
    if digits[1] == digits[2] == digits[3]:
        return 95000

    # Last 2 digits same
    if digits[2] == digits[3]:
        return 85000

    # Ascending digits
    if digits[0] < digits[1] < digits[2] < digits[3]:
        return 65000

    # Digit sum reduces to 9
    if sum_to_single_digit(sum(digits)) == 9:
        return 55000

    # Single-digit (0001 to 0009)
    if 1 <= num <= 9:
        return 75000

    # Default
    return 5000

# Example usage
num = int(input("Enter a 4-digit number: "))
cost = get_registration_cost(num)
print(f"Registration cost for {num:04d} is Rs {cost}")
