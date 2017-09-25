import SearchAlgorithm as Search


class EightPuzzleState(Search.NodeStateData):
    """Immutable internal representation of the eight puzzle"""

    tiles = None  # a tuple (0,1,2,3,4,5,6,7,8)
    blank_tile_index = None

    # inheriting from namedtuple makes it immutable
    def __init__(self, tiles):
        assert isinstance(tiles, tuple)
        self.tiles = tuple.__new__(tuple, tiles)
        self.blank_tile_index = tiles.index(0)

    # TODO: get the neighboring nodes, ie figure out what moves are possible and return a tuple of states that would
    # result
    def get_neighbors(self):
        pass

    @property
    def calculate_h1cost(self):
        tiles = self.tiles
        hcost = 0
        for tile_index in range(len(tiles)):
            if tile_index != tiles[tile_index]:
                hcost += 1
        return hcost

    @property
    def calculate_h2cost(self):
        tiles = self.tiles
        hcost = 0
        for tile_index in range(len(tiles)):
            hcost += abs(tile_index - tiles[tile_index])
        assert isinstance(tiles, list)
        return tiles
