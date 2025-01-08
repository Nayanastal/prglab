class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # Method to calculate the area of the rectangle
    def area(self):
        return self.length * self.breadth

    # Method to calculate the perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.length + self.breadth)

    # Method to compare the area of two rectangles
    def compare_area(self, other_rectangle):
        if self.area() > other_rectangle.area():
            return "First rectangle has a larger area."
        elif self.area() < other_rectangle.area():
            return "Second rectangle has a larger area."
        else:
            return "Both rectangles have the same area."

# Example usage:
# Create two rectangle objects
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 6)

# Print the area and perimeter of the first rectangle
print("Rectangle 1 - Length:", rectangle1.length, "Breadth:", rectangle1.breadth)
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())

# Print the area and perimeter of the second rectangle
print("\nRectangle 2 - Length:", rectangle2.length, "Breadth:", rectangle2.breadth)
print("Area:", rectangle2.area())
print("Perimeter:", rectangle2.perimeter())

# Compare the two rectangles by their area
print("\nComparison Result:", rectangle1.compare_area(rectangle2))
