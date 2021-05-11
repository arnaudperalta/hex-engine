from hex_engine.common import board_evaluation
from hex_game.hex import Board, are_equals
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
        value = sss_star(board, side, depth)
        board.pop()
        if (side == Board.BLUE and value >= best_move_value
            or side == Board.RED and value <= best_move_value):
            best_move_value = value
            best_move = move
    return best_move


def sss_star(board: Board, maximazing_player: bool, depth: int) -> int:
    """
        SSS* algorithm returning the evaluation value
        through the depth.
    """
    queue = [(board, "alive", inf, depth)]
    while queue[0][1] != "over":
        current_tuple = queue.pop()
        if current_tuple[1] == "alive":
            # Si la depth est à 0
            if current_tuple[3] == 0:
                evaluation = board_evaluation(current_tuple[0])
                if board.turn == Board.RED:
                    evaluation *= -1
                queue.append(
                    (
                        current_tuple[0].copy(),
                        "over",
                        min(current_tuple[2], evaluation),
                        0
                    )
                )
            elif current_tuple[0].turn == maximazing_player:
                for x in current_tuple[0].free_cells():
                    child = current_tuple[0].copy()
                    child.push(x)
                    queue.append(
                        (
                            child,
                            "alive",
                            current_tuple[2],
                            current_tuple[3] - 1
                        )
                    )
            else:
                first_child = current_tuple[0].copy()
                first_child.push(first_child.free_cells()[0])
                queue.append((first_child, "alive", current_tuple[2],
                              current_tuple[3] - 1))
        else:
            # Si le noeud est de type Min
            if current_tuple[0].turn != maximazing_player:
                # On récupère le parent
                parent = current_tuple[0].copy()
                parent.pop()
                purge(queue, parent)
                queue.append((parent, "over", current_tuple[2],
                              current_tuple[3]))
            # Si le noeud est de type Max
            else:
                if has_unexamined_brother(current_tuple[0]):
                    brother = current_tuple[0].copy()
                    brother.push(get_next_brother(brother))
                    queue.append((brother, "alive", current_tuple[2],
                                  current_tuple[3]))
                else:
                    parent = current_tuple[0].copy()
                    parent.pop()
                    queue.append((parent, "over", current_tuple[2],
                                  current_tuple[3] + 1))
    return queue[0][2]


def purge(queue, board: Board):
    """
        Delete each child of board from the queue.
    """
    for x in queue:
        parent = x[0].copy()
        parent.pop()
        if are_equals(board, parent):
            queue.remove(x)


def has_unexamined_brother(board: Board) -> bool:
    return board.free_cells()[-1] > board.stack_moves[-1]


def get_next_brother(board: Board) -> int:
    for x in board.free_cells():
        if x != board.stack_moves[-1]:
            return x
    return -1
