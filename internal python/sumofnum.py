# Importing functions from the package
from mymathpackage.factorial import factorial
from mymathpackage.fibonacci import fibonacci
from mymathpackage.sumsubpackage.sum_of_first_10 import sum_of_first_10

# Example usage:
n = 5
print(f"Factorial of {n}: {factorial(n)}")

fib_num = 10
print(f"Fibonacci series up to {fib_num}: {fibonacci(fib_num)}")

print(f"Sum of first 10 numbers: {sum_of_first_10()}")
# Function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Function to generate Fibonacci series up to n numbers
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
# Function to calculate the sum of the first 10 natural numbers
def sum_of_first_10():
    return sum(range(1, 11))
