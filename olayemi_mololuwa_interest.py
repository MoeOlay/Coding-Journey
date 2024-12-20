principal = float(input("Please enter the loan principal: "))
term = int(input("Please enter the loan term in months: "))
rate = float(input("Please enter the annual interst rate of the loan in the decimal: "))
total_Cost = principal * (1 + (rate/12))**term
interest_Amount = total_Cost - principal
print("\nThe amount of interest in this loan is $" + str(round(interest_Amount,2)))