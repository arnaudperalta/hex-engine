from hex_game import hex
from hex_engine import common, minimax_engine

# Création d'un plateau de hex
board = hex.Board()

# On joue plusieurs coups
board.push(hex.Board.A1)
board.push(hex.Board.K11)
board.push(hex.Board.J11)
board.push(hex.Board.I11)
board.push(hex.Board.K10)

print(board)
common.board_evaluation(board)
while not board.is_game_over():
    # On peux augmenter la profondeur selon l'efficacité du kernel.
    board.push(minimax_engine.get_best_move(board, 2, board.turn))
    print(board)
