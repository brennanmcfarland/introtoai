import heapq


class PriorityQueue:
    """An implementation of the priority queue, since the standard lib's implementation is built for scheduling.
    Uses heapq."""

    def __init__(self, heap_list=[]):
        self.heap = list(heap_list)

    def __len__(self):
        return len(self.heap)

    def push(self, item, cost):
        heapq.heappush(self.heap, (cost, item))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def peek(self):
        return self.heap[0][1]

    def contains(self, queried_item):
        return queried_item in (item[1] for item in self.heap)

    def get(self, queried_item):
        for item in self.heap:
            if item[1] == queried_item:
                return item[1]

    def replace(self, queried_item):
        for item in self.heap:
            if item[1] == queried_item:
                queried_item = item

    def empty(self):
        return len(self.heap) == 0

    def clear(self):
        self.heap = list([])

    def truncate(self, n):
        """Return a new priority queue with only the n best values from this one"""
        heap_list = list(self.heap).copy()
        heap_list = heap_list[:n]
        heapq.heapify(heap_list)
        return PriorityQueue(heap_list)
