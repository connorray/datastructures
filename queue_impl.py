class LinkedListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, item):
        new_node = LinkedListNode(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.head.val
        self.head = self.head.next
        self._size -= 1
        if self.is_empty():
            self.tail = None
        return item

    def front(self):
        if not self.is_empty():
            return self.head.val
        return None

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size


class DynamicArrayQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
