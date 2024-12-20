#imports 'math' and 'random' modules
import math
import random

#sets pi from math module to variable 'pi'
pi =  math.pi

#Prompts user for a integer 'radius'
radius = int(input("Please enter the radius of the sphere: "))

#calculates volume using 'pi' and 'radius' variables with the volume expression and assign value to 'volume' variable then prints out volume variable with string
volume = (4/3)*pi*pow(radius,3)
print(f'The volume of a sphere with a radius of {radius} is {volume:.2f}')

#Generates random integer from 1-10 using 'randint' function from 'random' module adn assigns to 'r_int' variable
r_int = random.randint(1,10)

#prints out 'r _int' variable and does 'factorial' function from 'math' module on 'r_int' variable
print(f'\nThe factorial of {r_int} is {math.factorial(r_int)}')
