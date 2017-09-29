import SearchAlgorithm as Search
from PriorityQueue import PriorityQueue


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
        current_node = self.__create_node(initial_state_data, heuristic)
        frontier = PriorityQueue()
        frontier.push(current_node, current_node.search_data.fcost)
        explored = set()

        while True:
            # TODO: remove this
            if frontier.empty():
                return None
            current_node = frontier.pop()
            if current_node.state_data.goal_test:
                print(current_node.state_data)
                return self.__build_solution(current_node.state_data)
            if current_node not in explored:
                explored.add(current_node)
            print("moved ", str(current_node.state_data.last_move), " to " + str(current_node.state_data.parent),
                  str(current_node.search_data.fcost))
            for prioritized_neighbor_node in self.__prioritize_neighbors(current_node, heuristic):
                neighbor_node = prioritized_neighbor_node[1]
                # TODO: explored has multiple values
                if (neighbor_node not in explored) and (not frontier.contains(neighbor_node)):
                    frontier.push(neighbor_node, prioritized_neighbor_node[0])
                elif frontier.contains(neighbor_node) and (
                            frontier.get(neighbor_node).search_data.fcost > neighbor_node.search_data.fcost):
                    frontier.replace(neighbor_node)

    def __build_solution(self, goal_node_state_data):
        """given the goal GraphSearchNode, returns a tuple of the moves from start to solution"""
        solution_list = []
        while goal_node_state_data.last_move is not None:
            solution_list.append(goal_node_state_data.last_move)
            goal_node_state_data = goal_node_state_data.parent
        solution_list.reverse()
        return tuple(solution_list)

    def __prioritize_neighbors(self, node, heuristic):
        """Gets a list of tuples (fcost, node)"""
        assert isinstance(node, Search.GraphSearchNode)
        neighbors = node.state_data.neighbors  # should be a StateData object
        prioritized_neighbors = []
        for neighbor_state_data in neighbors:
            neighbor_node = self.__create_node(neighbor_state_data, heuristic)
            prioritized_neighbors.append((neighbor_node.search_data.fcost, neighbor_node))
        return prioritized_neighbors

    def __create_node(self, state_data, heuristic):
        return Search.GraphSearchNode(NodeSearchDataAStar(state_data.gcost, getattr(state_data, heuristic)), state_data)

    def execute_search(self):
        pass

    def load_data(self):
        pass


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
