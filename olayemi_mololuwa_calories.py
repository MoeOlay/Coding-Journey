#Prompts the User to input an integer 'age'
age = int(input("Please enter your age: "))

#Prompts the User to input an integer 'weight'
weight = int(input("Please enter your weight in pounds: "))

#Prompts the User to input an integer 'heart rate'
heart_rate = int(input("Please enter your heart rate in beats per minute: "))

#Prompts the User to input an integer 'time'
time = int(input("Please enter the lenght of your workout in minutes: "))

#Calculates the amount of calories using age, weight, heart_rate, and time acccording to the calories expression then prints out calories variable
calories = (((age*.2757)+(weight*.03295)+(heart_rate*1.0781)-75.4991)*time)/8.368
print(f'\nCalories burned: {calories:.2f}')