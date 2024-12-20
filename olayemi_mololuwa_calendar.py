month = input("Please enter the month: ")
day = int(input("Please enter the day: "))
if month == "March" and 0 < day <= 19:
        print(f'{month} {day} is summer in the southern hemisphere.')
elif month == "March" and day <= 31:
        print(f'{month} {day} is autumn in the southern hemisphere.')

elif month == "June" and 0 < day <= 20:
   print(f'{month} {day} is autumn in the southern hemisphere.')
elif month == "June" and day <= 30:
        print(f'{month} {day} is winter in the southern hemisphere.')

elif month == "September" and 0 < day <= 21:
        print(f'{month} {day} is winter in the southern hemisphere.')
elif month == "September" and day <= 30:
        print(f'{month} {day} is spring in the southern hemisphere.')

elif month == "December" and 0 < day <=20:
        print(f'{month} {day} is spring in the southern hemisphere.')
elif month == "December" and day <= 31:
        print(f'{month} {day} is summer in the southern hemisphere.')

elif month == "January" or month == "February":
    print(f'{month} {day} is summer in the southern hemisphere.')

elif month == "April" or month == "May":
    print(f'{month} {day} is autumn in the southern hemisphere.')

elif month == "July" or month == "August":
    print(f'{month} {day} is winter in the southern hemisphere.')

elif month == "October" or month == "November":
    print(f'{month} {day} is spring in the southern hemisphere.')