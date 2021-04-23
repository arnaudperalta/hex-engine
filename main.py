from hex_engine import sss_engine
from hex_game import hex

board = hex.Board()

print(sss_engine.get_best_move(board, 2, board.turn))
