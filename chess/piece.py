import abc

from chess.position import Position


class Piece:
    __metaclass__ = abc.ABCMeta

    pieces_to_class_dict = {"R": "Rook",
                            "N": "Knight",
                            "B": "Bishop",
                            "Q": "Queen",
                            "K": "King",
                            "P": "Pawn"}

    def __init__(self, colour, pos):
        self.colour = colour
        self.position = pos

    def __str__(self):
        return "colour: {0}, type: {1}".format(self.colour, type(self))

    @abc.abstractmethod
    def satisfies_rules(self):
        """
        One of these rules must be satisfied in order for the move to be considered legal.
        All piece types must define at least one such rule.
        :return: boolean
        """
        return

    @abc.abstractmethod
    def default_rules(self):
        """
        These rules are mandatory to be satisfied by a piece type. If any of these rules fails,
        then the move is considered illegal.
        :return: boolean
        """
        return

    def default_piece_rules(self):
        """
        Rule 1: If the target square of a piece movement is occupied by piece of same colour
        consider the move illegal. This stands for all pieces.
        :return: boolean
        """

        def not_occupied_by_same_colour(to_pos: Position, board_dict: dict):
            return True if \
                (not str(to_pos) in board_dict) or (str(to_pos) in board_dict and
                                                    board_dict[str(to_pos)].colour is not self.colour) \
                else False

        return [not_occupied_by_same_colour]

    def can_move_to(self, to_pos, board_dict):
        """
        Check that default piece rules are satisfied, regardless of piece type.
        Check that default rules for the give piece type are satisfied.
        Check that at least one of the rules that need to be satisfied for a specific
        piece type is satisfied, otherwise the move is considered illegal.
        :param to_pos: Position
        :param board_dict: Position
        :return: boolean
        """

        for default_piece_rule in self.default_piece_rules():
            if not default_piece_rule(to_pos, board_dict):
                return False

        if not self.default_rules() is None:
            for default_rule in self.default_rules():
                if not default_rule(to_pos, board_dict):
                    return False

        for rule in self.satisfies_rules():
            if rule(to_pos, board_dict):
                return True

        return False
