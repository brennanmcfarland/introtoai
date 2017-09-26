from abc import ABC, abstractmethod


class SearchAlgorithm(ABC):
    """Abstract base class for all search algorithms; uses the command pattern"""

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def execute_search(self):
        pass


# TODO: make this and maybe other node-related classes inherit from tuple to make them immutable if time
class GraphSearchNode:
    """A node in a search graph"""

    search_data = None
    state_data = None

    def __init__(self, search_data, state_data):
        assert isinstance(search_data, NodeSearchData)
        assert isinstance(state_data, NodeStateData)
        self.state_data = state_data
        self.search_data = search_data


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
    def gcost(self):
        pass
    @abstractmethod
    def h1cost(self):
        pass

    @abstractmethod
    def h2cost(self):
        pass
