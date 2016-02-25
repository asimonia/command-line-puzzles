import sys

def get_new_board(row, column):
    """Gets a new board data structure"""
    """board[row][column]"""
    board = []
    for x in range(row):
        board.append([])
        for y in range(column):
            board[x].append('*')
    # Put the poison square at the top left coordinate (0,0)
    board[0][0] = 'P'
    return board


def print_board(board, column):
    """Prints the board data structure to the user"""
    
    # print the top portion of the board

    print()
    print("        0 1 2 3 4 5 6 7 8")

    # print each of the rows
    for row in range(len(board)):
        print("%s       %s" % (row, getRow(board, row, column)))

    print()


def getRow(board, row, column):
    """Return a string from the board data structure to a row"""
    boardRow = ''
    for col in range(column):
        boardRow += board[row][col] + ' '
    return boardRow


def show_instructions():
    """Displays the instructions to the user."""
    print()
    print("Here's how a board looks like (This one is 5 by 7)")
    print()
    print("        1 2 3 4 5 6 7 8 9")
    print("1\tP * * * * * *")
    print("2\t* * * * * * *")
    print("3\t* * * * * * *")
    print("4\t* * * * * * *")
    print("5\t* * * * * * *")
    print()
    print("The board is a big cookie - R rows high and C columns")
    print("wide. You input R and C at the start.  In the upper left")
    print("corner of the cookie is a poison square (P).  The one who")
    print("chomps the poison square loses. To take a chomp, type the")
    print("row and column of one of the squares of the cookie.")
    print("All of the squares below and to the right of that square")
    print("(including that square, too) disappear -- Chomp!")
    print("You can't chomp squares that have already been chomped,")
    print("or that are outside the original dimensions of the cookie.")
    print()


def make_move(board, move):
    """All the squares below and to the right of that square,
    including that square, disappear.
    """
    x, y = move

    for row in range(x, len(board)):
        for col in range(y, len(board[0])):
            board[row][col] = ''

    return board


def is_valid_move(x, y, board):
    """Return True if this is a valid move. Otherwise, False."""

    if x > len(board) or y > len(board[0]):
        print("Please choose a move on the board.")
        return False
    elif board[x][y] == 'P':
        print("You don't want to eat the poison cookie!")
        return False
    elif board[x][y] == [] or board[x][y] == '':
        print("That spot is empty.")
        return False

    return True


def enter_player_move(board, player):
    """Let the player enter a move.  Return (x, y) tuple"""
    
    while True:
        print("Player   %d" % (player))
        print("Coordinates of your chomp (row, column)? ")
        
        move = input()
        
        move = move.split()

        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and is_valid_move(int(move[0]), int(move[1]), board):
            return (int(move[0]), int(move[1]))
    
        print()


def new_player(player_turn, PLAYERS):
    """Change the player."""
    if player_turn == PLAYERS:
        player_turn = 1
    else:
        player_turn += 1

    return player_turn


def is_game_over(board):
    """Returns True if the only cell left on the board is the poison square"""
    rows = len(board)
    columns = len(board[0])

    for row in range(rows):
        for col in range(columns):
            if board[row][col] == '*':
                return False

    return True


def main():
    """main subroutine here"""
    print("This is the game of Chomp (Scientific American, Jan 1973")
    print("Do you want the rules? ")
    if input().lower().startswith('y'):
        show_instructions()

    PLAYERS = int(input("How many players? "))
    ROW = int(input("How many rows? "))
    COLUMN = int(input("How many columns? "))


    while True:
        # game setup
        playing = True
        player_turn = 1
        the_board = get_new_board(ROW, COLUMN)
        
        while playing:
            print_board(the_board, COLUMN)
            move = enter_player_move(the_board, player_turn)
            the_board = make_move(the_board, move)
            player_turn = new_player(player_turn, PLAYERS)

            if is_game_over(the_board):
                print("You lose, Player  %d" % (player_turn))
                playing = False
   

if __name__ == '__main__':
    main()