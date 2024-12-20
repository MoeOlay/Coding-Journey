hour_wage = int(input("Please enter your hourly wage: "))
hour_week = int(input("Please enter the number of hours worked per week: "))
weeks = int(input("Please enter the number of weeks worked this year: "))
salary = hour_wage*hour_week*weeks
print("\nYour salary so far this year is $" + str(salary))