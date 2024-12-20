"""
This is a program that allows the user to make calculations based on built of python math operators.
Author: Mololuwa Olayemi
"""
def addition(left, right):
    return left + right

def subtraction(left, right):
    return left - right

def multiplication(left, right):
    return left * right

def division(left, right):
    if right == 0:
        return "Error: Division by zero."
    return left / right

def modulus(left, right):
    return left % right

def power(left, right):
    return left ** right

def floor_division(left, right):
    if right == 0:
        return "Error: Division by zero."
    return left // right

# Dictionary mapping operators to their corresponding functions
operators = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
    '%': modulus,
    '**': power,
    '//': floor_division
}

def convert_to_number(value):
    """Convert string input to an int or float based on its format."""
    if '.' in value:
        return float(value)
    elif value.isnumeric():
        return int(value)
    else:
        raise ValueError(f"Invalid numeric value: {value}")

def calculate(expression):
    """Parse the expression and perform the calculation."""
    # Split expression and check for errors
    parts = expression.split()
    if len(parts) != 3:
        return f"Error: Invalid Expression - ({expression})"
    
    left_str, op, right_str = parts
    
    # Validate operator
    if op not in operators:
        return f"Error: Invalid Operator ({op})"
    
    # Convert strings to numbers and perform calculation
    try:
        left = convert_to_number(left_str)
        right = convert_to_number(right_str)
        result = operators[op](left, right)
        
        # Display formatted result as in the example output
        if isinstance(result, str):  # Handle division by zero error
            return result
        return f"{left} {op} {right} = {result}"
    
    except ValueError:
        return f"Error: Invalid Expression - ({expression})"

def run_calculator():
    print("Please enter an Expression\n")
    
    while True:
        expression = input(">: ").strip()
        
        # Check for stop words
        if expression.lower() in ["quit", "q"]:
            print("Goodbye!")
            break
        
        # Calculate and print the result
        result = calculate(expression)
        print("Result:", result, "\n")

# Run the calculator program
run_calculator()