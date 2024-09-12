import random

options = ['rock', 'paper', 'scissors']
user_wins = 0
computer_wins = 0
is_running = True

while is_running:
    user_input = input('Type Rock, Paper, Scissors or Q to quit: ').lower()

    if user_input == 'q':
        print('\n')
        print('--------------------------------------')
        print('Thanks for playing!')
        print(f'Your score is: {user_wins}')
        print(f'Your opponent\'s score is: {computer_wins}')
        print('Bye :)')
        print('--------------------------------------')

        break
    if user_input not in options:
        print('--------------------------------------')
        print('This is not a valid option')
        print('--------------------------------------')
        continue

    random_number = random.randint(0, 2)
    # ROCK: 0, PAPER: 1, SCISSORS: 2
    computer_pick = options[random_number]
    print('--------------------------------------')
    print('Computer picked', computer_pick)

    # Determine winner
    if user_input == computer_pick:
        print('--------------------------------------')
        print('It\'s a tie!')
        print('--------------------------------------')
    elif (user_input == 'rock' and computer_pick == 'scissors') or \
         (user_input == 'paper' and computer_pick == 'rock') or \
         (user_input == 'scissors' and computer_pick == 'paper'):
        print('--------------------------------------')
        print('You win!')
        print('--------------------------------------')
        user_wins += 1
    else:
        print('--------------------------------------')
        print('You lose!')
        print('--------------------------------------')
        computer_wins += 1

    if user_wins == 3:
        print('--------------------------------------')
        print('Congratulations, you won the game!')
        print(f'Final score - You: {user_wins}, Computer: {computer_wins}')
        print('--------------------------------------')
        break
    elif computer_wins == 3:
        print('--------------------------------------')
        print('The computer won the game!')
        print(f'Final score - You: {user_wins}, Computer: {computer_wins}')
        print('--------------------------------------')
        break
