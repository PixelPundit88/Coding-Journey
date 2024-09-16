import random
is_running = True
death_count = 0
gcoins = 0
name = input('What is your name, traveler?: ').upper()
print(f'Welcome to the adventure game, {name}!')

while is_running:
    print('_________________________________________')
    option = input('You\'re on a crossroad and there is a sign on a rock,\n'
                   'which says "To the RIGHT you go, your death you\'ll meet,\n'
                   'To the LEFT you go, a lake you will find.\n'
                   'If you go STRAIGHT, treasure may await."\n'
                   'Which way do you desire?(Q to quit) ').lower()

    if option == 'left':
        print('_________________________________________')
        print('You found a lake! You rest for a while and continue your journey.')
        meet_1 = input('You met a stranger who wants to play a game with you! \n'
                       '_________________________________________\n'
                       'ROLL the dice and get a number above 3 and greater than stranger\n'
                       'in order to obtain a gold coin,\n'
                       'SKIP the game and you won\'t get anything!\n'
                       'IF you get a number BELOW 3 a stranger seemingly has a knife in his pocket.\n'
                       '_________________________________________\n'
                       'Make your decision: ').lower()
        num_dice = random.randint(1,6)
        num2_dice = random.randint(1, 6)
        if meet_1 == 'skip':
            print('You decided to finish your adventure')
            is_running = False

        elif meet_1 == 'roll':
            print('_________________________________________')
            print(f'You got {num2_dice} on the dice')
            print(f'The stranger got {num_dice} on the dice')
            if num2_dice >= 3 and num2_dice > num_dice:
                print('you won a Gcoin!')
                gcoins += 1
                continue
            elif num2_dice <= 3:
                print('The stranger stabbed you to death!')
                death_count += 1
                break


    elif option == 'right':
        death_count += 1
        print('_________________________________________')
        print('Oooops! Someone tripped over a bush and fell off a cliff!\n'
              'Better luck next time!')
        print(f'You have died {death_count} time(s).')

    elif option == 'straight':
        gcoins += 1
        print('You found a map and a Gcoins!')
        print(f'You now have {gcoins} gold coin(s).')
        follow1 = input('You can FOLLOW the path on the map and possibly get a treasure\n'
                       'or you can go ANOTHER way ').lower()
        #if you FOLLOW you might meet an angry wolf, which will kill you. if NOT nothing happens
        if follow1 == 'follow':
            wolf = random.randint(0,1)
            if wolf == 0:
                print('Suddenly a wolf jumped out and fatally injured you!')
                death_count += 1
                break
            elif wolf == 1:
                print('You found a burried treasure!')
                gcoins += 10
                print(f'You now have {gcoins} gold coin(s).')
                continue
            elif follow1 == 'another':
                print('You found yourself in a prosperous kingdom and decided to calm down with adventures')
                gcoins += 1000
                print('Congrats Traveller, you made it!')
            else:
                print('Choose a valid option')
                continue

    elif option == 'q':
        break

    else:
        print('Choose a valid option! ;0')

print('*_______________________________________*')
print('Thanks for playing!')
print(f'You managed to obtain: {gcoins} Gcoins')
print('Your death count is:', death_count)
print('*_______________________________________*')