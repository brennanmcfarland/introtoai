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
        current_node = self.__create_node(initial_state_data)
        # TODO: it's setting explored and frontier to the same reference, why????
        explored = PriorityQueue()
        frontier = PriorityQueue()
        explored.push(current_node, current_node.search_data.hcost)

        while True:
            if explored.empty():
                return None
            if current_node.state_data.goal_test:
                return Search.build_solution(current_node.state_data)
            while not explored.empty():
                print("moved ", str(current_node.state_data.last_move), " to " + str(current_node.state_data.parent),
                      str(current_node.search_data.hcost))
                current_node = explored.pop()
                # TODO: need to implement my own heuristic instead of just reusing h2cost
                for prioritized_neighbor_node in self.__prioritize_neighbors(current_node):
                    neighbor_node = prioritized_neighbor_node[1]
                    frontier.push(neighbor_node, prioritized_neighbor_node[0])
            # get the k best moves and put them in explored, clearing frontier
            explored = frontier.truncate(k)
            frontier.clear()

    def __prioritize_neighbors(self, node):
        """Gets a list of tuples (fcost, node)"""
        assert isinstance(node, Search.GraphSearchNode)
        neighbors = node.state_data.neighbors
        prioritized_neighbors = []
        for neighbor_state_data in neighbors:
            neighbor_node = self.__create_node(neighbor_state_data)
            prioritized_neighbors.append((neighbor_node.search_data.hcost, neighbor_node))
        return prioritized_neighbors

    def __create_node(self, state_data):
        # TODO: need to come up with a heuristic, not just use h2
        return Search.GraphSearchNode(NodeSearchDataLocalBeam(state_data.h2cost), state_data)

    def execute_search(self):
        pass

    def load_data(self):
        pass


class NodeSearchDataLocalBeam(Search.NodeSearchData):
    """Search data pertaining to the given state in the local beam search, contains cost function"""

    hcost = None

    def __init__(self, hcost):
        self.hcost = hcost
