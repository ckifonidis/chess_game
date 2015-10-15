from chess.piece import Piece
from chess.position import Position


class Bishop(Piece):
    def default_rules(self):
        """
        No specific default rules apply for bishop.
        """
        return []

    def satisfies_rules(self):
        """
        A bishop can move in a diagonal line with no pieces in between the originating and the destination square.

        """
        def moves_in_diagonal(to_pos: Position, board_dict: dict):
            return self.position.is_diagonal(to_pos) \
                   and not [square for square in self.position.squares_in_between(to_pos) if square in board_dict]

        return [moves_in_diagonal]
