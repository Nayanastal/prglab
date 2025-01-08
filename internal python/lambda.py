# Lambda function to find area of square
area_of_square = lambda side: side * side

# Lambda function to find area of rectangle
area_of_rectangle = lambda length, width: length * width

# Lambda function to find area of triangle
area_of_triangle = lambda base, height: 0.5 * base * height

# Example usage:
side = 4
length = 5
width = 3
base = 6
height = 8

print(f"Area of square with side {side}: {area_of_square(side)}")
print(f"Area of rectangle with length {length} and width {width}: {area_of_rectangle(length, width)}")
print(f"Area of triangle with base {base} and height {height}: {area_of_triangle(base, height)}")
