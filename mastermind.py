import random as rnd

def get_code(CODE_PEGS, colors):
	"""Computer randomly generates the colors for the code"""
	code = []
	for slot in range(CODE_PEGS):
		code.append(rnd.choice(colors))
	return code


def get_move(code, colors, player_move):
	"""Evaluate player's move against the computer"""
	pegs = []
	copy_code = code.copy()
	copy_player_move = player_move.copy()
	
	# Check to see if player move color matches computer's move.
	# Order matters.  If true, add a B peg.
	for i in range(len(code)):
		if code[i] == player_move[i]:
			copy_code.remove(code[i])
			copy_player_move.remove(player_move[i])
			pegs.append('B')

	# Check to see if player has correct colors.
	# Order does not matter.  If true, add a W peg.
	for letter in copy_code:
		if letter in copy_player_move:
			copy_player_move.remove(letter)
			pegs.append('W')

	return pegs


def show_instructions():
	print("Master Mind is a code-breaking game for two players.\n")
	print("One player becomes the codemaker, the computer, while the other becomes the codebreaker.")
	print("The codemaker chooses a pattern of N code pegs.  Duplicates are allowed, so a player could")
	print("even choose N code pegs of the same color.  The chosen pattern is unseen by the codebreaker.\n")
	print("The codebreaker tries to guess the pattern, in both order and color, within ten turns.")
	print("Each guess is made by placing a row of code pegs on the decoding board.  Once placed, the codemaker")
	print("provides feedback by placing from zero to N key pegs in the small holes of the row with the guess.")
	print("A black key peg: correct color placed correctly")
	print("A white key peg: correct color placed incorrectly\n")


def valid_move(player_move, colors, CODE_PEGS):
	"""Check to see if the move is valid"""
	if len(player_move) != CODE_PEGS:
		return False

	for letter in player_move:
		if letter not in colors:
			return False

	return True


def main():
	"""Main subroutine goes here"""
	print("The game of Mastermind\n")
	print("Color codes:")
	print("R=Red		O=Orange	Y=Yellow")
	print("G=Green		B=Blue		P=Purple")
	print()
	print("Do you want instructions? ")

	if input().lower().startswith('y'):
		show_instructions()

	CODE_PEGS = int(input("How many color code pegs would you like for your game? \n"))

	while True:
		# game setup
		turns = 1
		MAX_TURNS = 10
		colors = ['R', 'G', 'O', 'B', 'Y', 'P']
		pegs = []
		code = get_code(CODE_PEGS, colors)
		move_history = []

		while turns <= MAX_TURNS:

			player_move = []

			while not valid_move(player_move, colors, CODE_PEGS):
				print("Turn # %s : " % (turns)) 
				player_move = list(input("What is your move? \n").upper())

			result = get_move(code, colors, player_move)
			
			move_history.append(player_move)
			for move in range(len(move_history)):
				print("#" + str(move + 1) + ": " + str(move_history[move]))
			
			turns += 1
			print("%s   black pegs" % result.count('B'))
			print("%s   white pegs" % result.count('W'))

		print("Looks like you made too many moves!")
		print("The secret code was: %s" % (code))
		break


if __name__ == '__main__':
	main()