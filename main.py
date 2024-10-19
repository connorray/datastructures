from linked_list import LinkedList
from stack import Stack
from queue_impl import LinkedListQueue, DynamicArrayQueue
from binary_tree import BinaryTree
from graph import Graph
from heap import MinHeap, MaxHeap
from priority_queue import PriorityQueue

def main():
    # LinkedList demonstration
    print("LinkedList Demonstration:")
    ll = LinkedList()
    for i in range(1, 6):
        ll.append(i)
    print("Original list:")
    ll.print_list()
    ll.delete(2)
    print("After deleting index 2:")
    ll.print_list()

    # Stack demonstration
    print("\nStack Demonstration:")
    stack = Stack()
    for i in range(1, 6):
        stack.push(i)
        print(f"Pushed {i}, Stack size: {stack.size()}")
    print(f"Top element: {stack.peek()}")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")

    # LinkedListQueue demonstration
    print("\nLinkedListQueue Demonstration:")
    llq = LinkedListQueue()
    for i in range(1, 6):
        llq.enqueue(i)
        print(f"Enqueued {i}, Queue size: {llq.size()}")
    print(f"Front element: {llq.front()}")
    while not llq.is_empty():
        print(f"Dequeued: {llq.dequeue()}")

    # DynamicArrayQueue demonstration
    print("\nDynamicArrayQueue Demonstration:")
    daq = DynamicArrayQueue()
    for i in range(1, 6):
        daq.enqueue(i)
        print(f"Enqueued {i}, Queue size: {daq.size()}")
    print(f"Front element: {daq.front()}")
    while not daq.is_empty():
        print(f"Dequeued: {daq.dequeue()}")

    # BinaryTree demonstration
    print("\nBinaryTree Demonstration:")
    bt = BinaryTree()
    for i in range(1, 8):
        bt.insert(i)
    print("Inorder traversal:")
    bt.inorder_traversal(bt.root)

    # Graph demonstration
    print("\n\nGraph Demonstration:")
    graph = Graph()
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    for v1, v2 in edges:
        graph.add_edge(v1, v2)
    print("Graph structure:")
    graph.print_graph()

    # MinHeap demonstration
    print("\nMinHeap Demonstration:")
    min_heap = MinHeap()
    elements = [4, 10, 3, 5, 1]
    for element in elements:
        min_heap.insert(element)
        print(f"Inserted {element}. Current heap: {min_heap.heap}")
    print("Extracting min elements:")
    while len(min_heap.heap) > 0:
        print(f"Extracted: {min_heap.extract_min()}. Remaining heap: {min_heap.heap}")

    # MaxHeap demonstration
    print("\nMaxHeap Demonstration:")
    max_heap = MaxHeap()
    for element in elements:
        max_heap.insert(element)
        print(f"Inserted {element}. Current heap: {max_heap.heap}")
    print("Extracting max elements:")
    while len(max_heap.heap) > 0:
        print(f"Extracted: {max_heap.extract_max()}. Remaining heap: {max_heap.heap}")

    # PriorityQueue demonstration
    print("\nPriorityQueue Demonstration:")
    pq = PriorityQueue()
    tasks = [("Task 1", 3), ("Task 2", 1), ("Task 3", 2)]
    for task, priority in tasks:
        pq.enqueue(task, priority)
        print(f"Enqueued '{task}' with priority {priority}")
    print("\nDequeuing tasks:")
    while not pq.is_empty():
        print(f"Dequeued: {pq.dequeue()}")

if __name__ == "__main__":
    main()
