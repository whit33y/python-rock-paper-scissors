import string
import os
while True:
    print('Rock, paper scissors')
    game_or_exit = input('n- new game, e- exit \n')
    if game_or_exit == 'n':
        os.system('clear')
        player_one_check = False
        player_two_check = False
        while player_one_check == False:
            os.system('clear')
            player_one = input('r- rock p-paper s-scissors player one \n')
            if player_one in ('r','p','s'):
                player_one_check = True
                os.system('clear')
        while player_two_check == False:
            os.system('clear')
            player_two = input('r- rock p-paper s-scissors player two \n')
            if player_two in ('r','p','s'):
                player_two_check = True
                os.system('clear')
        print('Player one: ',player_one,'\nPlayer two: ',player_two)
        if player_one == player_two:
            print('Draw! \n')
        elif player_one == 'r' and player_two == 'p':
            print('Player two win! \n')
        elif player_one == 'r' and player_two == 's':
            print('Player one win! \n')
        elif player_one == 'p' and player_two == 'r':
            print('Player one win! \n')
        elif player_one == 'p' and player_two == 's':
            print('Player two win! \n')
        elif player_one == 's' and player_two == 'r':
            print('Player two win! \n')
        elif player_one == 's' and player_two == 'p':
            print('Player onen win! \n')
    elif game_or_exit == 'e':
        print('Goodbye!')
        exit()
    else:
        os.system('clear')
        print('Something went wrong \n')
        continue
else:
    print('Something went wrong')
