phone_number = int(input("Please enter your phone number: "))
area_code= phone_number//10000000
rest_of_number = str(phone_number%10000000)
print(f'Phone Number: ({area_code}) {rest_of_number[:3]}-{rest_of_number[3:]}')
