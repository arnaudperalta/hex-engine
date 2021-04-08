from typing import List
from hex_game import hex
from math import inf

def board_evaluation(board: hex.Board):
	""""
		Return the substraction between blue and red score.
		If the heuristic evaluation return a positive value, blue player has
		an advantage on the board, else red has an advantage.
	"""
	return get_score(board, board.BLUE) - get_score(board, board.RED)


def get_score(board: hex.Board, color: bool) -> int:
	"""
		The score of a side on the board is calculated by the minimum amount of hex
		needed to finish the game with the dijkstra algorithm.
		The less is the score, the best it is.
		First and last rows/lines are linked with a cost of 0, the path is calculated
		with the opposites corner of the board.
	"""
	# Initialisation
	visited = []
	values = []
	for _ in range(len(hex.Board.CELLS)):
		values.append(inf)
	values[hex.Board.A1] = 0

	# Tant qu'il existe un sommet non visité
	while len(visited) != len(hex.Board.CELLS):
		# On choisit un sommet pas encore visité minimal
		curr = find_lowest(visited, values)
		visited.append(curr)
		# Pour chaque voisin de current hors de visited et différent de la couleur opposée
		for h in hex.neighbors(curr):
			# print (curr, hex.neighbors(curr))
			if h not in visited:
				weight = transition_value(
					curr,
					board.hex_color(curr),
					h,
					board.hex_color(h),
					color
				)
				if values[h] > (values[curr] + weight) and weight != inf:
					values[h] = values[curr] + weight
	print(values)
	return values[hex.Board.K11]


def find_lowest(visited, values):
	"""
		Secondary function for get_score, returns the minimal element
		in values who's not in visited.
	"""
	mini = inf
	sommet = -1
	for i in range(len(values)):
		if i not in visited and values[i] <= mini:
			mini = values[i]
			sommet = i

	return sommet
	

def transition_value(hex1: int, color1: bool, hex2: int, color2: bool, side: bool) -> int:
	"""
		Return the value of a transition between two neighbours hex and their colors.

		Return inf if the transition is not possible.
	"""

	if color1 == color2 and color1 != None:
		return 0

	# Si hex1 et hex2 sont dans la premiere colonne.
	if (hex1 % hex.Board.LINE_LEN == 0 
			and hex2 % hex.Board.LINE_LEN == 0
			and side == hex.Board.BLUE):
		return 0

	# Si hex1 et hex2 sont dans la derniere colonne.
	if (hex1 % hex.Board.LINE_LEN == hex.Board.LINE_LEN - 1
			and hex2 % hex.Board.LINE_LEN == hex.Board.LINE_LEN - 1
			and side == hex.Board.BLUE):
		return 0

	# Si hex1 et hex2 sont dans la premiere ligne.
	if (hex1  <= hex.Board.K1
			and hex2  <= hex.Board.K1
			and side == hex.Board.RED):
		return 0

	# Si hex1 et hex2 sont dans la derniere ligne.
	if (hex1 >= hex.Board.A11
			and hex2 >= hex.Board.A11
			and side == hex.Board.RED):
		return 0

	if color1 == (not side) or color2 == (not side):
		return 1000

	return 1
