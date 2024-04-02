import random

# function to play
def play():
    # ask user to enter start and end number
    lower_bound = int(input('lower bound: '))
    upper_bound = int(input('upper bound: '))
    # generate random number using lower and upper bound
    random_number = random.randint(lower_bound, upper_bound)
    guess = ''
    attempt = 0

    while guess != random_number:
        guess = int(input(f'Guess between {lower_bound} and {upper_bound}: '))
        if guess < lower_bound:
            print('Invalid Guess')
        elif guess > upper_bound:
            print('Invalid Guess')
        elif guess < random_number:
            print('Too low')
            attempt += 1
        elif guess > random_number:
            print('Too high')
            attempt += 1
    print(f'You have guessed the random number correctly in {attempt} attempt/attempts')
    play_again()

# function to play again
def play_again():
    # ask user to play again or exit
    response = input('Play again? (y/n): ').lower()
    if response != 'n':
        play()
    print('Thank you for playing')

play()
