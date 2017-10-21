import copy

import SearchAlgorithm as Search
import math

left, right, up, down = "left", "right", "up", "down"


class EightPuzzleState(Search.NodeStateData):
    """Immutable internal representation of the eight puzzle.  The state itself is stored with the row/column positions
     flattened as a tuple with 0 for the blank space. Equality, hashing, etc, is all based on this tuple."""

    __tiles = None  # a tuple (0,1,2,3,4,5,6,7,8)
    __last_move = None
    __parent = None
    # cache these values so they needn't be repeatedly calculated
    __blank_tile_index = 0
    __gcost = 0
    __num_spaces = 0
    __rows = 0

    # new vs init may be causing these issues
    def __new__(cls, state, gcost=0, last_move=None, parent=None):
        assert isinstance(state, tuple)
        new_puzzle = Search.NodeStateData.__new__(cls)
        new_puzzle.__tiles = tuple.__new__(tuple, state)
        new_puzzle.__blank_tile_index = state.index(0)
        new_puzzle.__num_spaces = len(state)
        new_puzzle.__rows = int(math.sqrt(new_puzzle.__num_spaces))
        new_puzzle.__gcost = gcost
        new_puzzle.__last_move = last_move
        new_puzzle.__parent = parent
        return new_puzzle

    def get_tiles(self):
        return copy.copy(self.__tiles)

    @property
    def neighbors(self):
        """Gets all states immediately reachable rom this state that was not the last state (hence __last_move)"""
        state_neighbors = []
        # add move left
        left_result = self.left
        if left_result is not self and self.__last_move != right:
            state_neighbors.append(left_result)
        # add move right
        right_result = self.right
        if right_result is not self and self.__last_move != left:
            state_neighbors.append(right_result)
        # add move up
        up_result = self.up
        if up_result is not self and self.__last_move != down:
            state_neighbors.append(up_result)
        # add move down
        down_result = self.down
        if down_result is not self and self.__last_move != up:
            state_neighbors.append(down_result)
        return tuple(state_neighbors)

    @property
    def up(self):
        """Get the state reached from moving up, this state if not possible"""
        if self.__blank_tile_index > self.__rows - 1:
            return EightPuzzleState(
                switch_in_tuple(self.__tiles, self.__blank_tile_index, self.__blank_tile_index - self.__rows),
                self.gcost + 1, up, self)
        else:
            return self

    @property
    def down(self):
        """Get the state reached from moving down, this state if not possible"""

        if self.__blank_tile_index < self.__num_spaces - self.__rows:
            return EightPuzzleState(
                switch_in_tuple(self.__tiles, self.__blank_tile_index, self.__blank_tile_index + self.__rows),
                self.gcost + 1, down, self)
        else:
            return self

    @property
    def left(self):
        """Get the state reached from moving left, this state if not possible"""

        if self.__blank_tile_index % self.__rows > 0:
            return EightPuzzleState(
                switch_in_tuple(self.__tiles, self.__blank_tile_index, self.__blank_tile_index - 1),
                self.gcost + 1, left, self)
        else:
            return self

    @property
    def right(self):
        """Get the state reached from moving right, this state if not possible"""

        if self.__blank_tile_index % self.__rows < self.__rows - 1:
            return EightPuzzleState(
                switch_in_tuple(self.__tiles, self.__blank_tile_index, self.__blank_tile_index + 1),
                self.gcost + 1, right, self)
        else:
            return self

    @property
    def goal_test(self):
        return self.__tiles == (0, 1, 2, 3, 4, 5, 6, 7, 8)

    @property
    def last_move(self):
        return self.__last_move

    @property
    def parent(self):
        return self.__parent

    @property
    def gcost(self):
        return self.__gcost

    @property
    def h1cost(self):
        """Number of out-of-place tiles"""
        tiles = self.__tiles
        hcost = 0
        for tile_index in range(len(tiles)):
            if tile_index != tiles[tile_index]:
                hcost += 1
        return hcost

    @property
    def h2cost(self):
        """Sum of each tile's distance from its goal state"""
        tiles = self.__tiles
        hcost = 0
        for tile_index in range(len(tiles)):
            hcost += abs(tile_index - tiles[tile_index])
        return hcost

    def index(self, element):
        return self.__tiles.index(element)

    def __eq__(self, other):
        if isinstance(self, other):
            return self.__tiles == other.__tiles
        else:
            return False

    def __hash__(self):
        hash_value = 0
        for i in range(0, self.__num_spaces):
            hash_value += (i + 1) * self.__num_spaces * self.__tiles[i]
        return hash_value

    def __lt__(self, other):
        return self.__tiles < other.__tiles

    def __str__(self):
        return str(self.__tiles)


def switch_in_tuple(tuple_to_permute, i, j):
    """return the given tuple with the elements at indices i and j switched"""
    list_to_permute = list(tuple_to_permute)
    list_to_permute[i], list_to_permute[j] = list_to_permute[j], list_to_permute[i]
    return tuple(list_to_permute)
