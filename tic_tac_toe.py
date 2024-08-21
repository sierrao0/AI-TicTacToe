import random
import os
clear = lambda: os.system('clear')

# Letter choice function
def select_letter():
    let=""
    auto_let=""
    # ask user to select a letter (X or O)
    while(let != "x" and let != "o"):
        let=input("Select X or O: ").replace(" ","").strip().lower()
        if let == "x":
            auto_let="o"
        else:
            auto_let="x"
    return let, auto_let

# Un estado en Triqui se puede representar mediante una matriz de 3x3 
# que contiene 'X', 'O' o un espacio vacío. Cada disposición diferente 
# de símbolos en el tablero es un estado único.

# Board cleaning/creating function
def clean_board():
    #  an empty board for X and O values
    brd=[[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
    return brd

# Board checking function
def is_board_full(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != ' ':
                count += 1
    return count

# To insert a letter (X or O) in a specific position
def insert_letter(board,letter,pos):
    i = int(pos/3)
    j = (pos % 3) - 1
    board[i][j-1]=letter

# To take computer moves
def computer_move(board,letter):
    computer_letter=letter
    possible_moves=[]
    available_corners=[]
    available_edges=[]
    available_center=[]
    position=-1

    # All possible moves
    for i in range(1,len(board)):
        if board[i] ==" ":
            possible_moves.append(i)

    # If the position can make X or O wins!
    # The computer will choose it to win or ruin a winning of the user
    for let in ["x","o"]:
        for i in possible_moves:
            board_copy=board[:]
            board_copy[i] = let
            if is_winner(board_copy,let):
                position=i


    # If computer cannot win or ruin a winning, then it will choose a random position starting
    # With the corners, the center then the edges
    if position == -1:
        for i in range(len(board)):
            # An empty index on the board
            if board[i]==" ":
                if i in [1,3,7,9]:
                    available_corners.append(i)
                if i == 5:
                    available_center.append(i)
                if i in [2,4,6,8]:
                    available_edges.append(i)
        # Check corners first
        if len(available_corners)>0:
            # select a random position in the corners
            position=random.choice(available_corners)
        # then check the availability of the center
        elif len(available_center)>0:
            # select the center as the position
            position=available_center[0]
        # lastly, check the availability of the edges
        elif len(available_edges)>0:
            # select a random position in the edges
            position=random.choice(available_edges)
    # fill the position with the letter
    board[position]=computer_letter

# to draw the board
def draw_board(board):
    # draw first row
    print("\n")
    print(" "+board[0][0]+" | "+board[0][1]+" | "+board[0][2]+" ")
    print("-"*11)
    # draw second row
    print(" "+board[1][0]+" | "+board[1][1]+" | "+board[1][2]+" ")
    print("-"*11)
    # draw third row
    print(" "+board[2][0]+" | "+board[2][1]+" | "+board[2][2]+" ")
    print("\n")
    return board

# to check if a specific "player" is the winner
def is_winner(board,letter):
    r# Check rows, columns, and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] == letter:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] == letter:
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == letter:
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] == letter:
        return True

    return False

# to repeat the game
def repeat_game():

    repeat=input("Play again? Press y for yes and n for no: ")
    while repeat != "n" and repeat != "y":
        repeat=input("PLEASE, press y for yes and n for no: ")
    return repeat

# to play the game
def play_game():

    letter, auto_letter= select_letter()
    # clean the board
    board=clean_board()
    board=draw_board(board)
    # check if there are empty positions on the board
    while is_board_full(board) == False:
        try:
            position=int(input("Select a position (1-9) to place an "+letter+" : " ))

        except:
            position=int(input("PLEASE enter position using only NUMBERS from 1-9: "))

        # check if user selects out of range position
        while (position not in range(1,10)):
            position=int(input("Please, choose another position to place an "+letter+" from 1 to 9 :"))

        # check if user selects an occupied position by X or O
        pos_i = int(position / 3)
        pos_j = (position % 3) - 1
        while (board[pos_i][pos_j] != " "):
            position=int(input("Please, choose an EMPTY position to place an "+letter+" from 1 to 9: "))

        # put the letter in the selected position & computer plays then draw the board
        insert_letter(board,letter,position)
        # computer move
        computer_move(board,auto_letter)
        # draw the board
        board=draw_board(board)

        if is_winner(board,letter):
            print("Congratulations! You Won.")
            return repeat_game()
        elif is_winner(board,auto_letter):
            print("Hard Luck! Computer won")
            return repeat_game()

    # if " " not in board:
    if is_board_full(board):
        print("Tie Game :)")
        return repeat_game()

# Start the game
if __name__ == "__main__":
    clear()
    print("Welcome to T-IA-c Toe. \n")
    repeat="y"
    while(repeat=="y"):
        repeat=play_game()
