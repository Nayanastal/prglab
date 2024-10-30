# Set the number of rows for the pyramid
number_of_rows = 5

for i in range(1, number_of_rows + 1):
    # Print leading spaces for formatting
    print(" " * (number_of_rows - i), end="")
    
    for j in range(1, i + 1):
        # Calculate the product and print it
        product = i * j
        print(product, end=" ")
    
    # Move to the next line after each row
    print()
