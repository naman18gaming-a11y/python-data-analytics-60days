import random

# guess the num game
secret_num = random.randint(1,100)
print("guess the number between 1 to 100")
while True:
    guess = int(input("enter your guess: "))
    if guess < secret_num:
        print("too low")
    elif guess > secret_num:
        print("too high")
    else:
        print("you guessed it")
        break
         
    