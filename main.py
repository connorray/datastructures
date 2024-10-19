from linked_list import LinkedList
from stack import Stack
from queue_impl import LinkedListQueue, DynamicArrayQueue
from binary_tree import BinaryTree
from graph import Graph
from heap import MinHeap, MaxHeap
from priority_queue import PriorityQueue
from hash_table import HashTable

def main():
    # LinkedList demonstration
    print("LinkedList Demonstration:")
    ll = LinkedList()
    for i in range(1, 6):
        ll.append(i)  # O(1) time, O(1) space
    print("Original list:")
    ll.print_list()  # O(n) time, O(1) space
    ll.delete(2)  # O(n) time, O(1) space
    print("After deleting index 2:")
    ll.print_list()  # O(n) time, O(1) space

    # Stack demonstration
    print("\nStack Demonstration:")
    stack = Stack()
    for i in range(1, 6):
        stack.push(i)  # O(1) time, O(1) space
        print(f"Pushed {i}, Stack size: {stack.size()}")  # size(): O(1) time, O(1) space
    print(f"Top element: {stack.peek()}")  # peek(): O(1) time, O(1) space
    while not stack.is_empty():  # is_empty(): O(1) time, O(1) space
        print(f"Popped: {stack.pop()}")  # pop(): O(1) time, O(1) space

    # LinkedListQueue demonstration
    print("\nLinkedListQueue Demonstration:")
    llq = LinkedListQueue()
    for i in range(1, 6):
        llq.enqueue(i)  # O(1) time, O(1) space
        print(f"Enqueued {i}, Queue size: {llq.size()}")  # size(): O(1) time, O(1) space
    print(f"Front element: {llq.front()}")  # front(): O(1) time, O(1) space
    while not llq.is_empty():  # is_empty(): O(1) time, O(1) space
        print(f"Dequeued: {llq.dequeue()}")  # dequeue(): O(1) time, O(1) space

    # DynamicArrayQueue demonstration
    print("\nDynamicArrayQueue Demonstration:")
    daq = DynamicArrayQueue()
    for i in range(1, 6):
        daq.enqueue(i)  # O(1) amortized time, O(1) space (can be O(n) when resizing)
        print(f"Enqueued {i}, Queue size: {daq.size()}")  # size(): O(1) time, O(1) space
    print(f"Front element: {daq.front()}")  # front(): O(1) time, O(1) space
    while not daq.is_empty():  # is_empty(): O(1) time, O(1) space
        print(f"Dequeued: {daq.dequeue()}")  # dequeue(): O(1) amortized time, O(1) space

    # BinaryTree demonstration
    print("\nBinaryTree Demonstration:")
    bt = BinaryTree()
    for i in range(1, 8):
        bt.insert(i)  # O(log n) average case, O(n) worst case, O(1) space
    print("Inorder traversal:")
    bt.inorder_traversal(bt.root)  # O(n) time, O(h) space (h: height of the tree)

    # Graph demonstration
    print("\n\nGraph Demonstration:")
    graph = Graph()
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    for v1, v2 in edges:
        graph.add_edge(v1, v2)  # O(1) time, O(1) space (assuming adjacency list)
    print("Graph structure:")
    graph.print_graph()  # O(V + E) time, O(1) space (V: vertices, E: edges)

    # MinHeap demonstration
    print("\nMinHeap Demonstration:")
    min_heap = MinHeap()
    elements = [4, 10, 3, 5, 1]
    for element in elements:
        min_heap.insert(element)  # O(log n) time, O(1) space
        print(f"Inserted {element}. Current heap: {min_heap.heap}")
    print("Extracting min elements:")
    while len(min_heap.heap) > 0:
        print(f"Extracted: {min_heap.extract_min()}. Remaining heap: {min_heap.heap}")  # O(log n) time, O(1) space

    # MaxHeap demonstration
    print("\nMaxHeap Demonstration:")
    max_heap = MaxHeap()
    for element in elements:
        max_heap.insert(element)  # O(log n) time, O(1) space
        print(f"Inserted {element}. Current heap: {max_heap.heap}")
    print("Extracting max elements:")
    while len(max_heap.heap) > 0:
        print(f"Extracted: {max_heap.extract_max()}. Remaining heap: {max_heap.heap}")  # O(log n) time, O(1) space

    # PriorityQueue demonstration
    print("\nPriorityQueue Demonstration:")
    pq = PriorityQueue()
    tasks = [("Task 1", 3), ("Task 2", 1), ("Task 3", 2)]
    for task, priority in tasks:
        pq.enqueue(task, priority)  # O(log n) time, O(1) space
        print(f"Enqueued '{task}' with priority {priority}")
    print("\nDequeuing tasks:")
    while not pq.is_empty():  # is_empty(): O(1) time, O(1) space
        print(f"Dequeued: {pq.dequeue()}")  # O(log n) time, O(1) space

    # HashTable demonstration
    print("\nHashTable Demonstration:")
    ht = HashTable()
    
    # Insert key-value pairs
    ht.insert("apple", 5)  # O(1) average time, O(n) worst case, O(1) space
    ht.insert("banana", 7)  # O(1) average time, O(n) worst case, O(1) space
    ht.insert("orange", 3)  # O(1) average time, O(n) worst case, O(1) space
    print("Hash Table after insertions:")
    print(ht)  # O(n) time, O(1) space where n is the number of elements

    # Retrieve values
    print("\nRetrieving values:")
    print("apple:", ht.get("apple"))  # O(1) average time, O(n) worst case, O(1) space
    print("banana:", ht.get("banana"))  # O(1) average time, O(n) worst case, O(1) space

    # Update a value
    ht.insert("apple", 10)  # O(1) average time, O(n) worst case, O(1) space
    print("\nAfter updating 'apple':")
    print("apple:", ht.get("apple"))  # O(1) average time, O(n) worst case, O(1) space

    # Remove a key-value pair
    ht.remove("banana")  # O(1) average time, O(n) worst case, O(1) space
    print("\nAfter removing 'banana':")
    print(ht)  # O(n) time, O(1) space where n is the number of elements

    # Try to get a non-existent key
    try:
        ht.get("grape")  # O(1) average time, O(n) worst case, O(1) space
    except KeyError:
        print("\nTried to get 'grape', but it's not in the hash table.")

if __name__ == "__main__":
    main()
