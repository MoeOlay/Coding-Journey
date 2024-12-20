"""
This program takes the 3 measurements of a given triangle.
It then solves for the perimeter and area of the triangle.
Afterward, it determines whether the triangle is acute, obtuse, or a right triangle.

Author: Mololuwa Olayemi
"""
import math  # Importing the math module for mathematical operations

# Taking inputs for the three sides of the triangle from the user
side_a = int(input("Please enter the length of side A of the triangle (in meters): "))
side_b = int(input("Please enter the length of side B of the triangle (in meters): "))
side_c = int(input("Please enter the length of side C of the triangle (in meters): "))

# Calculating the perimeter of the triangle
perimeter = side_a + side_b + side_c

# Calculating the semi-perimeter, which is needed for the area calculation
s_perimeter = perimeter / 2

# Calculating the area of the triangle using Heron's formula
area = math.sqrt(s_perimeter * (s_perimeter - side_a) * (s_perimeter - side_b) * (s_perimeter - side_c))

# Printing the perimeter and area of the triangle
print(f'The perimeter of the triangle is {perimeter}m\nThe area of the triangle is {area}m^2')

# Determining the type of triangle based on the Pythagorean theorem
# Checking if it is a right triangle
if pow(side_a, 2) + pow(side_b, 2) == pow(side_c, 2):
    print("It is a Right Triangle")
# Checking if it is an acute triangle
elif pow(side_a, 2) + pow(side_b, 2) > pow(side_c, 2):
    print("It is an Acute Triangle")
# Checking if it is an obtuse triangle
elif pow(side_a, 2) + pow(side_b, 2) < pow(side_c, 2):
    print("It is an Obtuse Triangle")