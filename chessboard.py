from chess import *
import copy


class Chessboard:
    def __init__(self):
        self.board_dict = {}

    def _add_piece(self, pos, piece):
        self.board_dict[pos] = piece

    @property
    def king_pos(self):
        """
        Property for returning the position of a king based on color.
        Closure holds the position of both kings and returns one as asked.
        :return: Position
        """
        kings = [pos for pos, value in self.board_dict.items() if isinstance(value, King)]

        def king_pos_by_colour(colour):

            return \
                [Position(king_pos[0], king_pos[1]) for king_pos in kings if
                 self.board_dict[king_pos].colour == colour][0]

        return king_pos_by_colour

    @staticmethod
    def _square_occupied(square):
        return True if not '--' in square else False

    def initialize_board_from_file(self, file):
        with open(file) as board:
            for row, rank in zip(board, reversed(Position.ranks)):
                squares = row.strip().split(' ')
                for square, file in zip(squares, Position.files):
                    if Chessboard._square_occupied(square):
                        piece_colour = square[0]
                        piece_type = square[1]
                        pos = Position(file, rank)
                        self._add_piece(str(pos), globals()[Piece.pieces_to_class_dict[piece_type]](piece_colour, pos))

    def move(self, from_pos, to_pos):
        """
        Check if there is a piece on the given square. If there is, ask the piece if it can move to the target square
        otherwise return False.
        :from from_pos: str
        :param to_pos: str
        :return: Boolean
        """
        if from_pos in self.board_dict:
            piece = self.board_dict[from_pos]
            position = Position(to_pos[0], to_pos[1])

        return piece.can_move_to(position, self.board_dict) \
            if (from_pos in self.board_dict) \
               and (self.same_colour_king_not_checked(piece)
                    if not isinstance(piece, King)
                    else self.target_king_square_not_checked(piece, position)) \
            else False

    def square_is_occupied(self, pos):
        return pos in self.board_dict[pos]

    def same_colour_king_not_checked(self, piece):
        """
        If moving a piece results in a board state where the king of the same colour as the piece is checked
        then this move must be considered as illegal.
        :param piece: Piece
        :return: boolean
        """
        temp_dict = copy.deepcopy(self.board_dict)
        temp_dict.pop(str(piece.position))
        for threat in [threat for pos, threat in self.board_dict.items() if not threat.colour is piece.colour]:
            if threat.can_move_to(self.king_pos(piece.colour), temp_dict):
                return False
        return True

    def target_king_square_not_checked(self, king, to_pos):
        """
        If kings tries to move to a checked square this move must be considered illegal.
        :param king:Piece
        :param to_pos: Position
        :return: boolean
        '"""
        for threat in [threat for pos, threat in self.board_dict.items() if not threat.colour is king.colour]:
            if threat.can_move_to(to_pos, self.board_dict):
                return False
        return True
