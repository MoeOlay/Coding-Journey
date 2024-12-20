#Prompts the user for an integer 'cents'
cents = int(input("Please enter a number of cents: "))

#Calculate maximum amount of quarters possible in 'cents' variable amount then subtracts that value in cents from 'cent' variable
quarters = cents//25
cents = cents-25*quarters

#Calculate maximum amount of dimes possible in the remaining 'cents' variable amount then subtracts that value in cents from 'cent' variable
dimes = cents//10
cents = cents-10*dimes

#Calculate maximum amount of nickels possible in the remaining 'cents' variable amount then subtracts that value in cents from 'cent' variable
nickels = cents//5
cents = cents-5*nickels

#Calculate maximum amount of pennies possible in the remaining 'cents' variable amount which should be the remainder of cents
pennies = cents//1
print(f'Coins: {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies')