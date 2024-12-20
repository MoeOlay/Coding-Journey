password = input("Please Enter Your Pasword: ")
print("Your new strong password is: ", end = '')
for i in password:
    if i == "o" :
        i = "0"
        print(i, end='')
    elif i == "i":
        i = "1"
        print(i, end='')
    elif i == "a":
        i = "@"
        print(i, end='')
    elif i == "e":
        i = "3"
        print(i, end='')
    elif i == "A":
        i = "4"
        print(i, end='')
    elif i == "B":
        i = "8"
        print(i, end='')
    elif i == "s":
        i = "$"
        print(i, end='')
    else:
        print(i, end='')
print("!")
    