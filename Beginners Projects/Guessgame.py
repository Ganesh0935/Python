# User guesses the number
import random
guess = random.randint(1,100)

print("Welcome to number guessing game!")
print("I've picked the number between 1 to 100. Try to Guess it!")

attempts = 0
while True :
    number = int (input("Enter your guess: "))
    attempts += 1

    if number < guess:
        print("Too low! Try again.")
    elif number > guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've Guessed the number {guess} correctly in {attempts} attempts.")
        break






print("----------@--------")
# computer guess your number
# import random

# user_number = int(input("Enter the number(1-100): "))

# low = 1
# high = 100
# attempts = 0
# while True:
#     guess = random.randint(low,high)
#     attempts +=1
#     if guess < user_number :
#         print("Too Low!")
#         low +=1
#     elif guess > user_number : 
#         print("Too High!")
#         high-=1
#     else:
#         print(f"You got the number {user_number} in {attempts} attempts.")
#         break