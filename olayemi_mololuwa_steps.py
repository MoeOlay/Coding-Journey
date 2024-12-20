def feet_to_steps(args=0):
    steps = args/2.5
    print(f'{int(steps)} steps')
distance = float(input("Please enter the distance travelled in feet: "))
feet_to_steps(distance)