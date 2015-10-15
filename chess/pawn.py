from chess.position import Position
from chess.piece import Piece


class Pawn(Piece):
    def default_rules(self):
        """
        In any case for a pawn move to be considered valid the pawn must move to the next higher or lower
        rank depending on the pawn's colour.
        :return: boolean
        """

        def moves_only_forward(to_pos: Position, board_dict: dict):
            return True if \
                (self.position.is_in_front(to_pos) and self.colour == "w") or (
                    not self.position.is_in_front(to_pos) and self.colour == "b") \
                else False

        return [moves_only_forward]

    def satisfies_rules(self):
        """
        Rules for a move to be considered legal.
        :return: boolean
        """

        def forward_same_file(to_pos: Position, board_dict: dict):
            """
            When a pawn moves to a forward, adjacent square of the same file
            the move is considered valid.
            """
            return self.position.is_adjacent(to_pos) \
                   and self.position.is_same_file(to_pos)

        def forward_same_file_first_turn(to_pos: Position, board_dict: dict):
            """
            When a pawn moves to a forward, adjacent square of the same file
            the move is considered valid.
            """
            return self.position.has_distance(to_pos) == 2 \
                   and self.position.is_same_file(to_pos) \
                   and not [square for square in self.position.squares_in_between(to_pos) if square in board_dict] \
                   and (
                   (self.position.rank == 7 and self.colour == 'b') or (self.position.rank == 2 and self.colour == 'w'))

        def take_piece_diagonally(to_pos: Position, board_dict: dict):
            """
            When a pawn moves to a forward, adjacent square of the same file
            the move is considered valid.
            """
            return self.position.is_adjacent(to_pos) \
                   and self.position.is_diagonal(to_pos) \
                   and str(to_pos) in board_dict.keys() \
                   and (not board_dict[str(to_pos)].colour is self.colour)

        return [forward_same_file, forward_same_file_first_turn, take_piece_diagonally]
