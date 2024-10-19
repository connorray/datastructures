from heap import MinHeap

class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def enqueue(self, item, priority):
        self.heap.insert((priority, item))

    def dequeue(self):
        return self.heap.extract_min()[1]

    def is_empty(self):
        return len(self.heap.heap) == 0
