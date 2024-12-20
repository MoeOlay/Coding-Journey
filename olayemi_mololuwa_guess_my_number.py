import random
num = random.randint(1,100)
print("I have generated random number between 1 and 100. You will have 10 attempts to guess that number.")
counter = 0
for i in range(10):
    guess = int(input(f'Guess {i+1}: '))
    counter += 1
    if counter == 10:
        print("You have run out of attempts")
        break
    if guess > num:
        print("Your guess is greater than my random number. Try Again.")
    elif guess < num:
        print("Your guess is less than my random number. Try Again.")
    elif guess == num:
        print("You have correctly guessed my random number!")
        break
    if counter == 10:
        print("You have run out of attempts")
        break