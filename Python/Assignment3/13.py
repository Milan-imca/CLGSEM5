'''
13 Write a progrom for following. Create a python package “Shapes”. Create modules:
circle.py: This module should have a function area(radius) that calculates and returns the
area of a circle given its radius.
rectangle.py: This module should have a function area(length, width) that calculates and
returns the area of a rectangle given its length and width.
Once the package is created, write a script that imports these modules and calculates:
The area of a circle with radius entered by user 
The area of a rectangle with length and width entered by user
'''

from Shapes import circle, rectangle


radius = float(input("Enter the radius of the circle: "))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

circle_area = circle.area(radius)
rectangle_area = rectangle.area(length, width)

print(f"Area of the circle: {circle_area}")
print(f"Area of the rectangle: {rectangle_area}")
