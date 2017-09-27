import SearchAlgorithm as Search
import math


class EightPuzzleState(Search.NodeStateData):
    """Immutable internal representation of the eight puzzle"""

    __tiles = None  # a tuple [0,1,2,3,4,5,6,7,8]
    # cache these values so they needn't be repeatedly calculated
    __blank_tile_index = 0
    __gcost = 0
    __num_spaces = 0
    __rows = 0

    def __init__(self, tiles, gcost):
        assert isinstance(tiles, tuple)
        self.__tiles = tuple.__new__(tuple, tiles)
        self.__blank_tile_index = tiles.index(0)
        self.__num_spaces = len(self.__tiles)
        self.__rows = math.sqrt(self.__num_spaces)
        self.__gcost = gcost

    @property
    def neighbors(self):
        neighbors = []
        # add move left
        if self.__blank_tile_index % self.__rows > 0:
            neighbors.append(EightPuzzleState(
                switch_in_tuple(self.__tiles, self.__blank_tile_index, self.__blank_tile_index - 1), self.gcost + 1))
        # add move right
        if self.__blank_tile_index % self.__rows < self.__rows - 1:
            neighbors.append(EightPuzzleState(
                switch_in_tuple(self.__tiles, self.__blank_tile_index, self.__blank_tile_index + 1), self.gcost + 1))
        # add move up
        if self.__blank_tile_index > self.__rows - 1:
            neighbors.append(EightPuzzleState(
                switch_in_tuple(self.__tiles, self.__blank_tile_index, self.__blank_tile_index - self.__rows),
                self.gcost + 1))
        # add move down
        if self.__blank_tile_index < self.__num_spaces - self.__rows:
            neighbors.append(EightPuzzleState(
                switch_in_tuple(self.__tiles, self.__blank_tile_index, self.__blank_tile_index + self.__rows),
                self.gcost + 1))
        return neighbors

    @property
    def goal_test(self):
        return self.__tiles == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    @property
    def gcost(self):
        return self.__gcost

    @property
    def h1cost(self):
        tiles = self.__tiles
        hcost = 0
        for tile_index in range(len(tiles)):
            if tile_index != tiles[tile_index]:
                hcost += 1
        return hcost

    @property
    def h2cost(self):
        tiles = self.__tiles
        hcost = 0
        for tile_index in range(len(tiles)):
            hcost += abs(tile_index - tiles[tile_index])
        return hcost

    def __eq__(self, other):
        if isinstance(self, other):
            return self.__tiles == other.__tiles
        else:
            return False

    def __hash__(self):
        hash_value = 0
        for i in range(0, self.__num_spaces):
            hash_value += i * self.__num_spaces * self.__tiles[i]
        return hash_value


def switch_in_tuple(tuple_to_permute, i, j):
    """return the given tuple with the elements at indices i and j switched"""
    list_to_permute = list(tuple_to_permute)
    list_to_permute[i], list_to_permute[j] = list_to_permute[j], list_to_permute[i]
    return tuple(list_to_permute)
