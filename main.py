import random
import time
from termcolor import colored

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True


# Game instruction
def gameIntro():
    print("     TIC - TAC - TOE Game\n")
    # print("        " + str(1) + " | " + str(2) + " | " + str(3) + " | ")
    # print("        " + "___________")
    # print("        " + str(4) + " | " + str(5) + " | " + str(6) + " | ")
    # print("        " + "___________")
    # print("        " + str(7) + " | " + str(8) + " | " + str(9) + " | ")


    # INSTEAD OF PRINTING WHAT IS ABOVE, DO THIS IN A CODING WAY...

    # First print the number of spaces for the cases [1, 2, 3]. It is done before
    # starting because it's not in the loop
    print("         ", end='')

    # iterate starting form 1 to 9
    for i in range(1, 10):
        print(str(i) + " | ", end='')

        # if i equals these numbers(NB: after they're printed), do the following..
        if i == 3 or i == 6 or i == 9:

            # first skip and line and then put spaces at the end.
            print("\n", end='         ')  # this is for ----

            # we don't want to print ------ after the cases [7, 8, 9], so what we do,
            # we only print this for i less than 9 (NB: we are first check if i was 3, 6 or 9)
            # it's an if inside the first if, so it would just print ---- for 3 and 6
            if i < 9:
                print("___________")
                print(end='         ')   # this is for cases eg [4, 5, 6]


    print("\nYour symbols need to be aligned in order to win the game; eg: 2-5-8 or 3-5-7")
    print("Good luck!")


# print gameboard
def printBoard(board):
    # print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    # print("___________")
    # print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    # print("___________")
    # print(board[6] + " | " + board[7] + " | " + board[8] + " | ")

    # INSTEAD OF PRINTING THAT
    # Comments were already done above

    print("\n" + "         ", end='')
    for i in range(9):
        print(board[i] + " | ", end='')
        if i == 2 or i == 5 or i == 8:
            print("\n", end='         ')
            if i < 8:
                print("___________")
                print(end='         ')


# take player input
def playerInput(board):
    inp = -8
    while inp < 1 or inp > 9:
        try:
            inp = int(input("Enter a number 1-9: "))
            if inp < 1 or inp > 9:
                print(colored("\nNot within the range! Please enter a correct value next time", 'red'))

        except ValueError:
            print(colored("\nIncorrect value! Please enter a correct value next time", 'red'))
            continue

        else:
            if board[inp - 1] == "-":
                board[inp - 1] = currentPlayer
            else:
                print("Oops! that spot is already taken\n")
                inp = 34   # throw an error, in order to restart back


# check for win or tie
def checkRow(board):
    # global --> if value of winner modified, it goes to entire program
    global winner
    # != "-" because three linear dashes means no input, thus no win
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[7]
        return True

def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[8] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[5] != "-":
        winner = board[2]
        return True

# overall win
def checkWin():
    if checkColumn(board) or checkRow(board) or checkDiagonal(board):

        global gameRunning
        gameRunning = False


# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# Computer
def Computer(board):
    while currentPlayer == "O":
        # check if position already taken
        taken = True
        while taken:
            position = random.randint(0, 8)
            if board[position] == "-":
                board[position] = "O"

                # to break out of the loop, just switch players instead of break.
                # helps in TTT_vs_Computer()
                switchPlayer()
                taken = False
            else:
                continue


# check for win or tie again
def checkTie(board):
    if "-" not in board and winner is None:
        print("\nIt is a tie!")

        global gameRunning
        gameRunning = False


def check_end_game():
    if not gameRunning:
        if winner == "X":
            print(colored("\nPlayer 1 win", 'green'))
        else:
            print(colored("\nPlayer 2 win", 'yellow'))
        return True




#Overall function (vs computer or vs person)
def TTT_vs_person():
    if currentPlayer == "X":
        print("\nPlayer 1 turn\n")
    else:
        print(f"\nPlayer 2 turn\n")
    playerInput(board)
    printBoard(board)
    checkWin()
    if check_end_game():
        return ""
    checkTie(board)
    switchPlayer()

def TTT_vs_computer():
    print("\nYour turn")
    playerInput(board)
    printBoard(board)
    checkWin()
    if check_end_game():
        return ""
    checkTie(board)
    switchPlayer()
    time.sleep(1)
    print("\nComputer's turn\n")
    time.sleep(1.7)
    Computer(board)  # This function has switchPlayer(). NO need to call it after again
    printBoard(board)
    checkWin()
    if check_end_game():
        return ""
    checkTie(board)



# Main
gameIntro()
answer = 'y'

opponent = input("\nDo you want a two players mode or play against the Computer?"
                 " Any other button pressed apart from 't', would be considered against the computer.\n"
                 "Press 't' for Two players or 'c' for Computer: ")

if opponent == 't':
    while answer == "y":

        print(colored("\nTwo Players Mode", "yellow"))

        while gameRunning:
            TTT_vs_person()

        answer = input("\nWould you like to continue yes(y) or No(n)? ")
        if answer == "y":

            # reset game
            gameRunning = True
            currentPlayer = "X"
            for i in range(9):
                board[i] = "-"
            continue
        else:
            break

else:
    while answer == "y":

        print(colored("\nYOU vs Computer", "yellow"))

        while gameRunning:
            TTT_vs_computer()

        answer = input("\nWould you like to continue yes(y) or No(n)? ")
        if answer == "y":

            # reset game
            gameRunning = True
            currentPlayer = "X"
            for i in range(9):
                board[i] = "-"
            continue
        else:
            break

print("\nThanks for playing :)")

