from abc import ABC, abstractmethod


class SearchAlgorithm(ABC):
    """Abstract base class for all search algorithms; uses the command pattern"""

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def execute_search(self):
        pass


class GraphSearchNode:
    """A node in a search graph"""

    search_data = None
    state_data = None

    def __init__(self, search_data, state_data):
        assert isinstance(search_data, NodeSearchData)
        assert isinstance(state_data, NodeStateData)
        self.state_data = state_data
        self.search_data = search_data

class NodeStateData(ABC):
    """Abstract base class for state data
        The abstract methods defined here require the state to be able to generate the needed search data
    """

    @abstractmethod
    def get_neighbors(self):
        pass

    @abstractmethod
    def calculate_h1cost(self):
        pass

    @abstractmethod
    def calculate_h2cost(self):
        pass


class NodeSearchData(ABC):
    """Abstract base class for search data pertaining to a given state, eg path cost"""
    pass
