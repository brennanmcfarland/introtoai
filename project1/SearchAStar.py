import SearchAlgorithm as Search


class SearchAStar(Search.SearchAlgorithm):
    """Command pattern class for the A* search algorithm"""

    def __init__(self):
        super().__init__()

    def execute_search(self):
        pass

    def load_data(self):
        pass


class SearchNodeAStar(Search.GraphSearchNode):
    """Data stored in an A* search node"""

    def __init__(self, search_data, state_data):
        super().__init__(search_data, state_data)


class NodeSearchDataAStar(Search.NodeSearchData):
    """Search data pertaining to the given state in the A* search, contains cost functions"""

    gcost = None
    hcost = None

    def __init__(self, gcost, hcost):
        self.gcost = gcost
        self.hcost = hcost

    @property
    def fcost(self):
        return self.gcost + self.hcost
