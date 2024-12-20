class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.num + other.num)
        raise TypeError("Operand must be an instance of Number")

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.num - other.num)
        raise TypeError("Operand must be an instance of Number")

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.num * other.num)
        raise TypeError("Operand must be an instance of Number")

    def __truediv__(self, other):
        if isinstance(other, Number):
            if other.num != 0:
                return Number(self.num // other.num)
            raise ValueError("Cannot divide by zero")
        raise TypeError("Operand must be an instance of Number")

num1 = Number(25)
num2 = Number(5)

num3 = num1 + num2
num4 = num1 - num2
num5 = num1 * num2
num6 = num1 / num2

num7 = (num3 + num4 * num2) / num5

print(f'{num1} + {num2} = {num3}')
print(f'{num1} - {num2} = {num4}')
print(f'{num1} * {num2} = {num5}')
print(f'{num1} / {num2} = {num6}')
print(f'( {num3} + {num4} * {num2} ) / {num5} = {num7}')
