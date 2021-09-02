board = [" " for x in range(10)]




def insertLetter(letter, pos):
    board[pos] = letter

def spaceFree(pos):
    return board[pos] == " "

def printBoard(board):

    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")

def IsWinner(bo, le):

    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

def PM():
    run = True
    while run:
        move = input("Please select a box to place an 'X' (enter a number from 1-9)")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceFree(move):
                    run = False
                    insertLetter("X",move)
                else:
                    print("This box is already taken!")
            else:
                print("Please insert a number within the range of numbers 1-9 !")
        except:
            print("Please type a number")

def CM(): # AI computer
    possMoves = [x for x,  letter  in enumerate(board) if letter == " " and x != 0] # searches for empty spaces
    move = 0

    for let in ["O","X"]:
        for i in possMoves:
            boardC = board[:] #copy of orginal board that can be changed
            boardC[i] = let
            if IsWinner(boardC, let):
                move = i
                return move

    CO = []
    for i in possMoves:
        if i in[1,3,7,9]:
            CO.append(i)

    if len(CO) > 0:
        move = selectRandom(CO)
        return move

    if 5 in possMoves:
        move = 5
        return move

    EO = []
    for i in possMoves:
        if i in[2,4,6,8]:
            EO.append(i)

    if len(EO) > 0:
        move = selectRandom(EO)

    return move

def selectRandom(list):
    import random
    ln = len(list)
    r = random.randrange(0,ln)
    return list[r]

def isBoardfull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True



def main():
    player_score = 0
    comput_score = 0

    print("TIC TAC TOE GAME!")
    printBoard(board)

    while not (isBoardfull(board)):
        if not (IsWinner(board,"O")):
            PM()
            printBoard(board)
        else:
            print("The Computer has won this game !")
            comput_score = comput_score + 1
            print("You: ",player_score)
            print("Computer: ",comput_score)
            break

        if not (IsWinner(board,"X")):
            move = CM()
            if move == 0:
                print("Tie Game")
            else:
                insertLetter("O", move)
                print("Computer placed an O in box ",move)
                printBoard(board)
        else:
            print("You won this game !")
            player_score = player_score + 1
            print("You : ",player_score)
            print("Computer:",comput_score)
            break

    if isBoardfull(board):
        print("Tied Game!")



while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break