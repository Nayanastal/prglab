def generate_numbers(N):
    # Generate a list of numbers from 1 to N
    numbers = list(range(1, N + 1))
    
    # a) Filter out even numbers using list comprehension (Keep only odd numbers)
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    # b) Generate a new list with the cube of odd numbers
    odd_numbers_cubed = [num ** 3 for num in odd_numbers]
    
    return odd_numbers, odd_numbers_cubed

# Example usage:
N = 10  # You can change this value as needed
odd_numbers, odd_numbers_cubed = generate_numbers(N)

print(f"Odd numbers from 1 to {N}: {odd_numbers}")
print(f"Cubes of odd numbers from 1 to {N}: {odd_numbers_cubed}")
