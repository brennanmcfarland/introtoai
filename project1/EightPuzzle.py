import SearchAlgorithm as Search


class EightPuzzleState(Search.NodeStateData):
    """Internal representation of the eight puzzle"""

    tiles = None  # a tuple (0,1,2,3,4,5,6,7,8)

    def __init__(self):
        super().__init__()

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
