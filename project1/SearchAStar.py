import SearchAlgorithm as Search
import PriorityQueue


class SearchAStar(Search.SearchAlgorithm):
    """Command pattern class for the A* search algorithm"""

    def __init__(self):
        super().__init__()

    def search(self, initial_state_data, manhattan_distance):
        # TODO: move initialization to a separate private method
        assert isinstance(initial_state_data, Search.NodeStateData)
        assert isinstance(manhattan_distance, bool)
        # TODO: see if there's a better way to handle this that doesn't involve method name strings if you have time
        heuristic = "h2cost" if manhattan_distance else "h1cost"
        current_node = self.create_node(initial_state_data, heuristic)
        frontier = PriorityQueue()
        frontier.push(current_node, current_node.search_data.fcost)
        explored = set()

        # TODO: need to have it remember sequence of actions it took and be able to return that
        while True:
            if frontier.empty():
                return None
            current_node = frontier.get()
            if current_node.goal_test:
                return current_node.state_data  # TODO: return solution
            explored.add(current_node)
            for neighbor_node in self.__prioritize_neighbors(current_node, heuristic):
                if not explored.__contains__(neighbor_node) and not frontier.contains(neighbor_node):
                    frontier.push(neighbor_node, neighbor_node.search_data.fcost)
                elif frontier.contains(neighbor_node) and (
                            frontier.get(neighbor_node).search_data.fcost > neighbor_node.search_data.fcost):
                    frontier.replace(neighbor_node)

    def __prioritize_neighbors(self, node, heuristic):
        """Gets a list of nodes [fcost, node]"""
        assert isinstance(node, SearchNodeAStar)
        neighbors = node.state_data.neighbors  # should be a tuple
        prioritized_neighbors = ()
        for neighbor in neighbors:
            prioritized_neighbors.append([neighbor.gcost + getattr(neighbor, heuristic), neighbor])
        return prioritized_neighbors

    def __create_node(self, state_data, heuristic):
        return SearchNodeAStar(NodeSearchDataAStar(state_data.gcost, getattr(state_data, heuristic)), state_data)

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
