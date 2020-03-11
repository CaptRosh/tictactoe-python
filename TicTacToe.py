import random
win=0
entries = [' ']*10
availablePositions=[0,1,2,3,4,5,6,7,8,9]
players = [0,'X','O']

def board():
    print('            |            |            \n'
          '            |            |            \n'
          '    '+entries[1]+'       |     '+entries[2]+'      |    '+entries[3]+'      \n'
          '            |            |            \n'
          '------------------------------------\n'
          '            |            |            \n'
          '    '+entries[4]+'       |     '+entries[5]+'      |    '+entries[6]+'      \n'
          '            |            |            \n'
          '            |            |            \n'
          '------------------------------------\n'
          '            |            |            \n'
          '    '+entries[7]+'       |     '+entries[8]+'      |    '+entries[9]+'      \n'
          '            |            |            \n'
          '            |            |            \n'
          )

def checkwin(mark):
    return ((entries[7] == mark and entries[8] == mark and entries[9] == mark) or  # across the top
            (entries[4] == mark and entries[5] == mark and entries[6] == mark) or  # across the middle
            (entries[1] == mark and entries[2] == mark and entries[3] == mark) or  # across the bottom
            (entries[7] == mark and entries[4] == mark and entries[1] == mark) or  # down the middle
            (entries[8] == mark and entries[5] == mark and entries[2] == mark) or  # down the middle
            (entries[9] == mark and entries[6] == mark and entries[3] == mark) or  # down the right side
            (entries[7] == mark and entries[5] == mark and entries[3] == mark) or  # diagonal
            (entries[9] == mark and entries[5] == mark and entries[1] == mark))    # diagonal

def boardFull():
    return 9 == win

def poscheck(playername,mark):
        pos = int(input("Player" + playername + "'s" +" turn:"))
        if pos not in [1,2,3,4,5,6,7,8,9] or pos not in availablePositions:
            print("Sorry, please go again.")
        else:
            availablePositions.pop(pos)
            availablePositions.insert(pos,'occupied')
            entries.pop(pos)
            entries.insert(pos, mark)

def replay():
    return input("Do you want to play again?").lower().startswith('y')

def randomPlayer():
    return random.choice((-1,1))

while True:
    print("Welcome to TicTacToe, let's start.")
    toggle = randomPlayer()
    player = players[toggle]
    if player == 'X':
        out=1
    elif player == 'O':
        out=2

    print("This round, Player "+ str(out)+ " will go first")

    gameOn=True
    input("Press enter to start")
    board()
    while gameOn:
        if toggle == 1:
            poscheck('1',player)
        else:
            poscheck('2',player)
        board()
        win+=1

        if checkwin(player):
            board()
            print("Congrats! Player {} has won".format(player))
            gameOn=False
        else:
            if boardFull():
                board()
                print('Game is a draw')
                break
            else:
                toggle *= -1
                player=players[toggle]

    entries=[' ']*10
    availablePositions=[num for num in range(0,10)]
    win = 0
    if not replay():
        exit()
