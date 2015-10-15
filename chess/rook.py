from chess.piece import Piece
from chess.position import Position


class Rook(Piece):
    def default_rules(self):
        """
        No specific rules apply for rook.
        """
        return []

    def satisfies_rules(self):
        """
        A rook can move in the same line horizontally or vertically as long as there are no pieces in between the
        originating and the destination square.
        """
        def moves_in_line(to_pos: Position, board_dict: dict):
            return self.position.is_in_line(to_pos) \
                   and not [square for square in self.position.squares_in_between(to_pos) if square in board_dict]

        return [moves_in_line]
