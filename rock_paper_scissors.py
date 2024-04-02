import random

choices = ['rock', 'paper', 'scissors']

def play():

    score = 0
    rounds = int(input('How many rounds?: '))
    for i in range(rounds):
        computer = random.choice(choices)
        user = input('Your pick: ').lower().strip()
        if user not in choices:
            print('Not in the choices')
        elif user == computer:
            print(f'Computer: {computer}. It is a Tie!')
        elif win(user, computer):
            print(f'Computer: {computer}. You Win!')
            score += 1
        else:
            print(f'Computer: {computer}. You Lose!')
    print(f'You got {score}/{rounds}')

def win(player, opponent):

    if player == 'rock' and opponent == 'scissors' \
    or player == 'paper' and opponent == 'rock' \
    or player == 'scissors' and opponent == 'paper':
        return True
    
play()