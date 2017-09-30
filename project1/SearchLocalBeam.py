import SearchAlgorithm as Search
from PriorityQueue import PriorityQueue


class SearchLocalBeam(Search.SearchAlgorithm):
    """Command pattern class for the local beam search algorithm"""

    def __init__(self):
        super().__init__()

    def search(self, initial_state_data, k, max_nodes=0):
        assert isinstance(initial_state_data, Search.NodeStateData)
        assert isinstance(k, int)
        current_node = self.__create_node(initial_state_data)
        explored = PriorityQueue()  # the nodes we've already looked at
        frontier = PriorityQueue()  # the nodes we're looking at now
        frontier_successors = PriorityQueue()  # successors of the nodes we're looking at now
        frontier.push(current_node, current_node.search_data.hcost)  # add the first node to the frontier
        node_count = 0

        while True:
            if frontier.empty():  # failure
                return None
            while not frontier.empty():  # for every node in the frontier, expand it and pick the k best successors
                #  print("moved ", str(current_node.state_data.last_move), " to " + str(current_node.state_data.parent),
                #  str(current_node.search_data.hcost))
                # get the next frontier node and mark it as explored
                current_node = frontier.pop()
                explored.push(current_node, current_node.search_data.hcost)
                if current_node.state_data.goal_test:  # success
                    return Search.build_solution(current_node.state_data)
                # expand unexplored neighbors
                for prioritized_neighbor_node in self.__prioritize_neighbors(current_node):
                    neighbor_node = prioritized_neighbor_node[1]
                    if not explored.contains(neighbor_node):
                        frontier_successors.push(neighbor_node, prioritized_neighbor_node[0])
                        node_count += 1
                        if 0 < max_nodes <= node_count:  # failure
                            return None
            # get the k best moves and put them in explored, clearing frontier
            frontier = frontier_successors.truncate(k)
            frontier_successors.clear()

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
        return Search.GraphSearchNode(NodeSearchDataLocalBeam(state_data.h2cost), state_data)


class NodeSearchDataLocalBeam(Search.NodeSearchData):
    """Search data pertaining to the given state in the local beam search, contains cost function"""

    hcost = None

    def __init__(self, hcost):
        self.hcost = hcost
