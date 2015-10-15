from chess.position import Position
from chess.piece import Piece


class King(Piece):
    def default_rules(self):
        """
        No specific default rules apply for bishop.
        """
        return []

    def satisfies_rules(self):
        """
        A king can move to all adjacent squares.

        """
        def moves_to_adjacent_squares(to_pos: Position, board_dict: dict):
            return (self.position.is_adjacent(to_pos))

        return [moves_to_adjacent_squares]
