from chess.piece import Piece
from chess.position import Position


class Queen(Piece):
    def default_rules(self):
        """
        No specific default rules apply for queen.
        """
        return []

    def satisfies_rules(self):
        """
        A queen can move in diagonal or in the same line, vertically or horizontally when no pieces
        are in between the destination and the target sqauare.
        """
        def moves_in_line(to_pos: Position, board_dict: dict):
            return (self.position.is_in_line(to_pos) or self.position.is_diagonal(to_pos)) \
                   and not [square for square in self.position.squares_in_between(to_pos) if square in board_dict]

        return [moves_in_line]
