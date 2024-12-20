speed_limit = int(input("Please enter the speed limit for the road: "))
speed = int(input("Please enter the vehicle's recorded speed: "))
if speed-speed_limit > 40:
    print("The speeding fine is $300.")
elif speed-speed_limit > 20:
    print("The speeding fine is $150.")
elif speed-speed_limit > 5:
    print("The speeding fine is $75.")
elif speed_limit-speed > 9:
    print("The speeding fine is $50.")
else:
    print("There is no fine.")