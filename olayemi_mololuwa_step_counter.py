class NegativeValueError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def steps_to_miles(steps):
    try:
        steps = int(steps)
    except ValueError:
        raise ValueError("Exception: Non-Numeric Value Entered.")
    
    if steps < 0:
        raise NegativeValueError("Exception: Negative Step Count Entered.")
    
    return steps / 2000

# Main program
while True:
    try:
        user_input = input("Enter # of Steps:> ") 
        miles = steps_to_miles(user_input)
        print(f"{miles:.2f} miles") 
    except ValueError as ve:
        print(ve)
    except NegativeValueError as ne:
        print(ne)
