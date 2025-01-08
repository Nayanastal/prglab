import math

def is_all_digits_even(num):
    # Check if all digits of the number are even
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True

def find_perfect_squares_with_even_digits(start, end):
    result = []
    
    # Loop through possible square roots to find perfect squares in the range
    for i in range(int(math.sqrt(start)), int(math.sqrt(end)) + 1):
        square = i * i
        if square >= start and square <= end:
            if is_all_digits_even(square):
                result.append(square)
    
    return result

# Example usage:
start_range = 1000
end_range = 9999

perfect_squares = find_perfect_squares_with_even_digits(start_range, end_range)
print("Perfect squares with all even digits:", perfect_squares)
