from hex_engine.common import board_evaluation
from hex_game.hex import Board
from math import inf


def get_best_move(board: Board, depth: int, side: bool) -> int:
    """
        Return the estimated best move along the depth
    """
    if board.is_game_over():
        return -1
    best_move_value = -inf
    if side == Board.RED:
        best_move_value = inf

    for move in board.free_cells():
        board.push(move)
        value = negamax_ab(board, -inf, inf, not side, depth - 1)
        board.pop()
        if (side == Board.BLUE and value >= best_move_value
                or side == Board.RED and value <= best_move_value):
            best_move_value = value
            best_move = move

    return best_move


def negamax_ab(board: Board, alpha: int, beta: int, maximazing_player: bool,
               depth: int) -> int:
    """
        Negamax alpha-beta pruning algorithm returning the evaluation value
        through the depth.
    """
    if depth == 0:
        return board_evaluation(board) * (1 if maximazing_player else -1)

    best_move = -inf
    for move in board.free_cells():
        board.push(move)
        best_move = max(best_move, -negamax_ab(board, -beta, -alpha,
                                               not maximazing_player,
                                               depth - 1))
        board.pop()
        alpha = max(alpha, best_move)
        if beta <= alpha:
            break

    if maximazing_player == Board.RED:
        return best_move * - 1
    return best_move
