'''1. Create a function calculate_area (length, width=5) that returns the area of a rectangle. If the width is not provided, it should default to 5.'''

def calculate_area(length,width=5):
  return length * width

print(f"Area of Rectangle with width: {calculate_area(10,10)}")
print(f"Area of Rectangle with default width value : {calculate_area(10,5)}")

