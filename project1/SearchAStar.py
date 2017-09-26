import SearchAlgorithm as Search
import queue


class SearchAStar(Search.SearchAlgorithm):
    """Command pattern class for the A* search algorithm"""

    def __init__(self):
        super().__init__()

    def search(self, initial_state_data, manhattan_distance):
        #TODO: move initialization to a separate private method
        assert isinstance(initial_state_data, Search.NodeStateData)
        assert isinstance(manhattan_distance, bool)
        # TODO: see if there's a better way to handle this that doesn't involve method name strings if you have time
        heuristic = "h2cost" if manhattan_distance else "h1cost"
        current_node = self.create_node(initial_state_data, 0, heuristic)
        print(current_node.search_data)
        print(current_node.state_data)

        frontier = queue.PriorityQueue()

    def prioritize_neighbors(self, node):
        assert isinstance(node, SearchNodeAStar)
        neighbors = node.state_data.neighbors #should be a tuple


    def create_node(self, state_data, gcost, heuristic):
        search_data = NodeSearchDataAStar(gcost, getattr(state_data, heuristic))
        search_node = SearchNodeAStar(search_data, state_data)
        return search_node

    def execute_search(self):
        pass

    def load_data(self):
        pass


class SearchNodeAStar(Search.GraphSearchNode):
    """Data stored in an A* search node"""

    def __init__(self, search_data, state_data):
        super(SearchNodeAStar, self).__init__(search_data, state_data)


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
