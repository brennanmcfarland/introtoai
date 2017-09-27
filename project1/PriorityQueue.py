import heapq


# TODO: if time, combine with hash table functionality for quicker retrieval of an element in the set
class PriorityQueue:
    """An implementation of the priority queue, since the standard lib's implementation is built for scheduling"""

    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def push(self, item, cost):
        heapq.heappush(self.heap, (cost, item))

    def pop(self):
        return heapq.heappop(self.heap)

    def contains(self, queried_item):
        return queried_item in (item[1] for item in self.heap)

    # TODO: make these more efficient, again, with a hash table as mentioned above
    def get(self, queried_item):
        for item in self.heap:
            if item == queried_item:
                return item

    def replace(self, queried_item):
        for item in self.heap:
            if item == queried_item:
                queried_item = item

    def empty(self):
        return len(self.heap) == 0

    def clear(self):
        while not (self.empty()):
            self.pop()
