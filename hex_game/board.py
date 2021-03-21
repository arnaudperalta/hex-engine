class Move:

	def __init__(self, cell: int):
		self.cell = cell


class Board:

	COLORS = [WHITE, BLACK] = [True, False]

	CELLS = [
		A1, B1, C1, D1, E1, F1, G1, H1, I1, J1, K1,
		A2, B2, C2, D2, E2, F2, G2, H2, I2, J2, K2,
		A3, B3, C3, D3, E3, F3, G3, H3, I3, J3, K3,
		A4, B4, C4, D4, E4, F4, G4, H4, I4, J4, K4,
		A5, B5, C5, D5, E5, F5, G5, H5, I5, J5, K5,
		A6, B6, C6, D6, E6, F6, G6, H6, I6, J6, K6,
		A7, B7, C7, D7, E7, F7, G7, H7, I7, J7, K7,
		A8, B8, C8, D8, E8, F8, G8, H8, I8, J8, K8,
		A9, B9, C9, D9, E9, F9, G9, H9, I9, J9, K9,
		A10,B10,C10,D10,E10,F10,G10,H10,I10,J10,K10,
		A11,B11,C11,D11,E11,F11,G11,H11,I11,J11,K11
	] = range(121)

	def __init__(self):
		self.stack_moves = []
		self.board_state = [None] * 121
		self.turn = self.WHITE

	def __repr__(self):
		print("call SVG representation")

	def __str__(self):
		return self.print_board()

	def is_legal(self, move: Move) -> bool:
		"""
			Return a boolean value, is true if the cell is empty.
		"""
		return self.board_state[move.cell] is None

	def free_cells(self):
		"""
			Return all empty cells on the board.
		"""
		moves = []
		for index, cell in self.board_state:
			if cell is None:
				moves.append(index)
		return moves

	def push(self, move: Move):         
		"""
			Play a move on the board.
		"""             
		if not self.is_legal(move):
			raise Exception("Trying to push an illegal move.")

		self.stack_moves.append(move)
		self.board_state[move.cell] = self.turn
		self.turn = not self.turn

	def pop(self):
		"""
			Rollback the game from one move.
		"""
		move = self.stack_moves.pop()
		self.board_state[move.cell] = None
		self.turn = not self.turn

	def is_game_over(self):
		"""
			Return a boolean value, true if the game is finished.
		"""
		return self.is_white_winner() or self.is_black_winner()

	def is_white_winner(self):
		"""
			Return a boolean value, true if white won the game.
		"""
		print("to be defined")


	def is_black_winner(self):
		"""
			Return a boolean value, true if black won the game.
		"""
		print("to be defined")


	def print_board(self):
		"""
			Print on standard output a board representation of
			the actual state of the game.
		"""
		toPrint = ""
		lineNb = 0
		for i in range(len(self.board_state)):
			if i != 0 and i % 11 == 0:
				toPrint += "\n"
				lineNb += 1
				for j in range(lineNb):
					toPrint += "  "
			if self.board_state[i] == None:
				toPrint += ".  "
			elif self.board_state[i] == self.WHITE:
				toPrint +=  "w  "
			else:
				toPrint += "b  "
		return toPrint
