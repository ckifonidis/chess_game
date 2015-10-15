from chess.piece import Piece
from chess.position import Position


class Knight(Piece):
    def default_rules(self):
        """
        No specific default rules apply for knight
        """
        return []

    def satisfies_rules(self):
        """
        A Knight can only move in to gammas on any square as long
        as this square is not occupied by piece of the same colour.

        """

        def moves_in_gamma(to_pos: Position, board_dict: dict):
            return self.position.is_in_gamma(to_pos)

        return [moves_in_gamma]
