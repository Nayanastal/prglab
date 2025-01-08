def sum_of_digits(n):
    """Function to calculate the sum of digits of a number"""
    return sum(int(digit) for digit in str(n))

def find_numbers_with_even_digit_sum(start, end):
    """Function to find all numbers whose sum of digits is even in a given range"""
    result = []
    
    # Loop through the range of numbers
    for num in range(start, end + 1):
        if sum_of_digits(num) % 2 == 0:  # Check if sum of digits is even
            result.append(num)
    
    return result

# Example usage:
start_range = 100
end_range = 200

numbers = find_numbers_with_even_digit_sum(start_range, end_range)
print(f"Numbers between {start_range} and {end_range} whose sum of digits is even: {numbers}")
