import random
import os

if os.name == 'posix':
    clear = lambda: os.system('clear')
else:
    clear = lambda: os.system('cls')

# Un estado en Triqui se puede representar mediante una matriz de 3x3 
# que contiene 'X', 'O' o un espacio vacío. Cada disposición diferente 
# de símbolos en el tablero es un ESTADO UNICO.

# Funcion creadora/limpiadora del tablero.
def nuevo_tablero():
    #  An empty board for X and O values
    brd=[[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
    return brd

# Funcion heuristica para valorar un estado
def heuristica(board):
    # Comprueba filas, columnas y diagonales en caso de una victoria y evalua.
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return 10 if row[0] == 'X' else -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return 10 if board[0][col] == 'X' else -10

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 10 if board[0][0] == 'X' else -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 10 if board[0][2] == 'X' else -10

    return 0

# Funcion del algoritmo Min-Max
def minmax(board, nivel, is_max):
    puntaje = heuristica(board)

    # Casos Base
    if puntaje == 10:
        return puntaje - nivel
    if puntaje == -10:
        return puntaje + nivel
    if is_board_full(board):
        return 0

    if is_max:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minmax(board, nivel + 1, not is_max))
                    board[i][j] = ' '
        return best
    
    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minmax(board, nivel + 1, not is_max))
                    board[i][j] = ' '
        return best
    
# Movimiento de la "IA"
def jugada_IA(board, letter):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = letter
                move_val = minmax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
                    
    board[best_move[0]][best_move[1]] = letter
    
#--------------------------------------------------------
#|<FUNCIONES MODIFICADAS DE LA IMPLEMENTACION DE NUHAGH>|
#--------------------------------------------------------

# Board checking function
def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

# To insert a letter (X or O) in a specific position
def insert_letter(board,letter,pos):
    i = int((pos-1)/3)
    j = ((pos-1) % 3)
    board[i][j] = letter

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

# Comprueba si el jugador humano es ganador
def is_winner(board, letter):
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

    repeat=input("\nDesea jugar de nuevo? (y/n) ")
    while repeat != "n" and repeat != "y":
        repeat=input("Por favor, presione y para si y n para no: ")
    return repeat

# to play the game
def play_game():
    letter = 'O'
    auto_letter = 'X'
    # clean the board
    board=nuevo_tablero()
    draw_board(board)
    # check if there are empty positions on the board
    while is_board_full(board) == False:
        try:
            position=int(input("Seleccione la posicion (1-9) donde quiere marcar: " ))

        except:
            position=int(input("Por favor, solo numeros del 1 al 9: "))

        # check if user selects out of range position
        while (position not in range(1,10)):
            position=int(input("Por favor, elija una posicion valida del 1 al 9: "))

        # check if user selects an occupied position by X or O
        pos_i = int((position-1)/3)
        pos_j = ((position-1) % 3)
        while (board[pos_i][pos_j] != " "):
            position=int(input("Por favor, elija una posicion VACIA del 1 al 9: "))

        # put the letter in the selected position & computer plays then draw the board
        insert_letter(board,letter,position)
        
        # computer move
        jugada_IA(board,auto_letter)
        
        # draw the board
        draw_board(board)

        if is_winner(board, letter):
            print("***************************")
            print("Felicitaciones, has ganado!")
            print("***************************")
            return repeat_game()
        elif is_winner(board, auto_letter):
            print("**************************************")
            print("Que mala suerte, la IA te ha superado!")
            print("**************************************")
            return repeat_game()

    # if " " not in board:
    if is_board_full(board):
        print("*"*69)
        print("Que despliegue de calidad. Sin embargo, esta vez no habra un ganador!")
        print("*"*69)
        return repeat_game()

# Start the game
if __name__ == "__main__":
    clear()
    print("Bienvenido a T-IA-c Toe.")
    repeat="y"
    while(repeat=="y"):
        repeat=play_game()
