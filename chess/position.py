class Position:
    ranks = [str(x) for x in range(1, 9)]
    files = [chr(x) for x in range(97, 105)]

    def __init__(self, file, rank):
        self.rank = int(rank)
        self.file = ord(file)

    def is_adjacent(self, other):
        return abs(self.rank - other.rank) == 1

    def is_in_front(self, other):
        return other.rank - self.rank > 0

    def is_same_rank(self, other):
        return self.rank == other.rank

    def is_same_file(self, other):
        return self.file == other.file

    def is_in_line(self, other):
        return self.is_same_file(other) | self.is_same_rank(other)

    def is_in_gamma(self, other):
        return self.has_distance(other) == 3 and (not self.is_in_line(other))

    def has_distance(self, other):
        return abs(self.file - other.file) + abs(self.rank - other.rank)

    def is_diagonal(self, other):
        return abs(self.rank - self.file) == abs(other.rank - other.file) or \
               (self.rank + self.file == other.rank + other.file)

    def squares_in_between(self, other):

        file_from, rank_from = Position.pos_list_get_indices(self)
        file_until, rank_until = Position.pos_list_get_indices(other)
        rank_step = 1 if rank_from < rank_until else -1
        file_step = 1 if file_from < file_until else -1
        rank_from = rank_from + 1 if rank_step == 1 else rank_from - 1
        file_from = file_from + 1 if file_step == 1 else file_from - 1

        if self.is_diagonal(other):
            return [file + rank for (rank, file)
                    in zip(Position.ranks[rank_from:rank_until:rank_step],
                           Position.files[file_from:file_until:file_step])]
        elif self.is_same_file(other):
            return [file + rank for rank, file
                    in zip(Position.ranks[rank_from:rank_until:rank_step],
                           [chr(self.file) for _ in range(abs(rank_until - rank_from))])]
        elif self.is_same_rank(other):
            return [file + rank for file, rank
                    in zip(Position.files[file_from:file_until:file_step],
                           [str(self.rank) for _ in range(abs(file_until - file_from))])]
        return False

    @staticmethod
    def pos_list_get_indices(pos):
        return Position.files.index(chr(pos.file)), Position.ranks.index(str(pos.rank))

    # TODO: Clean up squares_in_between function a bit.
    """
    @staticmethod
    def pos_list_adjust_step():

    @staticmethod
    def pos_list_adjust_starting_index(starting_index, step):
    """

    def __str__(self):
        return "{1}{0}".format(str(self.rank), chr(self.file))

