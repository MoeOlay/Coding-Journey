num_of_values = int(input("Please enter the number of floating-point values: "))
list = []
for i in range(num_of_values):
    fp_values = float(input("Please enter a floating point value: "))
    list.append(fp_values)
greatest = max(list)
print("\nNormalized Floating Point Values:")
for i in list:
    print(f'{i/greatest:.2f}')