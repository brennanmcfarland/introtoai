from abc import ABC, abstractmethod
import functools


class SearchAlgorithm(ABC):
    """Abstract base class for all search algorithms; uses the command pattern"""

    @abstractmethod
    def search(self, initial_state_data, heuristics_param, max_nodes):
        pass


@functools.total_ordering
class GraphSearchNode:
    """A node in a search graph"""

    search_data = None
    state_data = None

    def __init__(self, search_data, state_data):
        assert isinstance(search_data, NodeSearchData)
        assert isinstance(state_data, NodeStateData)
        self.search_data = search_data
        self.state_data = state_data

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.state_data == other.state_data
        else:
            return False

    def __hash__(self):
        return self.state_data.__hash__()

    def __lt__(self, other):
        return self.state_data.__lt__(other.state_data)


class NodeSearchData(ABC):
    """Abstract base class for search data pertaining to a given state, eg path cost
        Inherited from in the algorithm class"""
    pass


class NodeStateData(ABC, tuple):
    """Abstract base class for state data
        Inherited from in the state representation class
        The abstract methods defined here require the state to be able to generate the needed search data
        It's immutable because it inherits from tuple
    """

    @abstractmethod
    def neighbors(self):
        pass

    @abstractmethod
    def goal_test(self):
        pass

    @abstractmethod
    def last_move(self):
        pass

    @abstractmethod
    def parent(self):
        pass

    @abstractmethod
    def gcost(self):
        pass

    @abstractmethod
    def h1cost(self):
        pass

    @abstractmethod
    def h2cost(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass


def build_solution(goal_node_state_data):
    """given the goal GraphSearchNode, returns a tuple of the moves from start to solution"""
    solution_list = []
    while goal_node_state_data.last_move is not None:
        solution_list.append(goal_node_state_data.last_move)
        goal_node_state_data = goal_node_state_data.parent
    solution_list.reverse()
    return tuple(solution_list)
