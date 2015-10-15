from chessboard import Chessboard

if __name__ == "__main__":

    _debug_mode = False
    print("Debug mode: {0}".format("ON" if _debug_mode else "OFF"))

    board_file = "assets/complex_board.txt"
    results_file = "assets/results.txt"
    moves_file = "assets/complex_moves_expected.txt" if _debug_mode else "assets/complex_moves.txt"
    is_legal = "LEGAL"
    is_illegal = "ILLEGAL"

    print("Initializing board from file: {0}".format(board_file))
    print("Results will be printed in {0}".format(results_file))
    print("Chess moves to be evaluated: {0}".format(moves_file))

    board_obj = Chessboard()
    board_obj.initialize_board_from_file(board_file)

    with open(moves_file) as moves:
        res = open(results_file, "w+")
        for from_pos, to_pos, *expected in [_.strip().split() for _ in moves]:
            if board_obj.move(from_pos, to_pos):
                if expected and is_illegal in expected[0]:
                    res.write(("Error in : {0} {1}\n".format(from_pos, to_pos)))
                else:
                    res.write(is_legal + "\n")
            else:
                if expected and expected[0] in is_legal:
                    res.write(("Error in : {0} {1}\n".format(from_pos, to_pos)))
                else:
                    res.write(is_illegal + "\n")
