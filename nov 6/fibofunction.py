def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci series is:")
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b 

n = int(input("Enter the number: "))

fibonacci_series(n)
