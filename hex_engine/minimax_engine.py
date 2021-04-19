from hex_engine.common import board_evaluation
from hex_game.hex import Board
from math import inf

def get_best_move(board: Board, depth: int, side: bool) -> int:
	"""
		Return the estimated best move along the depth
	"""
	best_move_value = -inf
	if side == Board.RED:
		best_move_value = inf
	
	for move in board.free_cells():
		board.push(move)
		value = minimax_ab(board, -inf, inf, not side, depth - 1)
		board.pop()
		if (side == Board.BLUE and value >= best_move_value
			or side == Board.RED and value <= best_move_value):
			best_move_value = value
			best_move = move

	return best_move


def minimax_ab(board: Board, alpha: int, beta: int, maximazing_player: bool, depth: int) -> int:
	"""
		Alpha-beta pruning algorithm returning the evaluation value 
		through the depth.
	"""
	if depth == 0:
		return board_evaluation(board)

	if maximazing_player == Board.BLUE:
		best_move = -inf
		for move in board.free_cells():
			board.push(move)
			best_move = max(best_move, minimax_ab(board, alpha, beta, Board.RED, depth - 1))
			board.pop()
			alpha = max(alpha, best_move)
			if beta <= alpha:
				return best_move
		return best_move
	else:
		best_move = inf
		for move in board.free_cells():
			board.push(move)
			best_move = min(best_move, minimax_ab(board, alpha, beta, Board.BLUE, depth - 1))
			board.pop()
			beta = min(beta, best_move)
			if beta <= alpha:
				return best_move
		return best_move
