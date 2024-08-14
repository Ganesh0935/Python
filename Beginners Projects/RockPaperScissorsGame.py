import random
# def user_choice():
#     user_input = input("Enter the choice(rock/paper/scissors): ")
#     while user_input not in ['rock','paper','scissors']:
#         print("Enter the valid choice!")
#         user_input = input("Enter the choice(rock/paper/scissors): ")
#     return user_input

# def computer_choice():
#     return random.choice(['rock','paper','scissors'])


def winner(u,c):
    if u == c:
        return "It's a tie!"
    elif (u == 'rock' and c == 'paper') or (u == 'paper' and c=='scissors') or (u == 'scissors' and c =='rock'):
        return "Computer Wins!"
    else:
        return "You wins!"
    

print("Let's play Rock,Paper, Scissors!")
u = input("Enter the choice(rock/paper/scissors): ").lower()
while u not in ['rock','paper','scissors']:
    print("Enter the valid choice!")
    u = input("Enter the choice(rock/paper/scissors): ").lower()
c = random.choice(['rock','paper','scissors'])
print("Your choice:",u)
print("Computer's choice:",c)

print(winner(u,c))

