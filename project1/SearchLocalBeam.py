import SearchAlgorithm as Search
from PriorityQueue import PriorityQueue


class SearchLocalBeam(Search.SearchAlgorithm):
    """Command pattern class for the local beam search algorithm"""

    def __init__(self):
        super().__init__()

    def search(self, initial_state_data, k):
        # TODO: move initialization to a separate private method
        assert isinstance(initial_state_data, Search.NodeStateData)
        assert isinstance(k, int)

    def __create_node(self, state_data):
        # TODO: need to come up with a heuristic
        return Search.GraphSearchNode(NodeSearchDataLocalBeam(0), state_data)

    def execute_search(self):
        pass

    def load_data(self):
        pass


class NodeSearchDataLocalBeam(Search.NodeSearchData):
    """Search data pertaining to the given state in the local beam search, contains cost function"""

    hcost = None

    def __init__(self, hcost):
        self.hcost = hcost
