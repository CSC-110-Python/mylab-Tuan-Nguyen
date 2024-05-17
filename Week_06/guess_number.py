print("Welcome to Guess Number!")
right_number = 13
guess = 0
count = 0
done = False
while not done:
    guess = int(input("Guess a number from 1 to 20: "))
    count += 1
    if guess <= 0 or guess > 20:
        print("Invalid guess")
    elif guess != right_number:
        if guess > right_number:
            print("Too high")
        else:
            print("Too low")
    elif guess == right_number:
        print("Correct!")
        done = True


