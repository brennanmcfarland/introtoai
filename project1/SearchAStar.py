import SearchAlgorithm as Search


class SearchAStar(Search.SearchAlgorithm):
    """Command pattern class for the A* search algorithm"""

    def __init__(self):
        super().__init__()

    def execute_search(self):
        pass

    def load_data(self):
        pass


class SearchNodeDataAStar(Search.SearchNodeData):
    """Data stored in an A* search node"""

    current_state = None
    gcost = None
    hcost = None

    def __init__(self, current_state, gcost, hcost):
        assert isinstance(current_state, Search.NodeStateData)
        self.current_state = current_state
        self.gcost = gcost
        self.hcost = hcost

    @property
    def fcost(self):
        return self.gcost + self.hcost
