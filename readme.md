# Data Structures Implementation

This repository contains implementations of fundamental data structures in Python. Each data structure is designed for efficient operations and demonstrates key concepts used in computer science and software engineering.

## Linked List

The `LinkedList` class in `linked_list.py` implements a singly linked list. It uses a `ListNode` class to represent individual nodes in the list. The linked list supports the following operations:

- `append(val)`: Adds a new node with the given value to the end of the list. Time complexity: O(n), where n is the number of nodes.
- `delete(index)`: Removes the node at the specified index. Time complexity: O(n) in the worst case.
- `print_list()`: Displays the contents of the list.

The implementation demonstrates the use of a dummy head node and traversal techniques common in linked list operations.

## Stack

The `Stack` class in `stack.py` implements a last-in-first-out (LIFO) data structure. It uses a Python list as the underlying storage mechanism. The stack supports these operations:

- `push(item)`: Adds an item to the top of the stack. Time complexity: O(1) amortized.
- `pop()`: Removes and returns the top item from the stack. Time complexity: O(1).
- `peek()`: Returns the top item without removing it. Time complexity: O(1).
- `is_empty()`: Checks if the stack is empty. Time complexity: O(1).
- `size()`: Returns the number of items in the stack. Time complexity: O(1).

This implementation showcases the use of Python's built-in list methods for efficient stack operations.

## Queue

The `queue_impl.py` file contains two queue implementations:

### LinkedListQueue

This implementation uses a linked list structure for the queue. It maintains both head and tail pointers for efficient enqueue and dequeue operations. The `LinkedListQueue` class supports:

- `enqueue(item)`: Adds an item to the back of the queue. Time complexity: O(1).
- `dequeue()`: Removes and returns the front item from the queue. Time complexity: O(1).
- `front()`: Returns the front item without removing it. Time complexity: O(1).
- `is_empty()`: Checks if the queue is empty. Time complexity: O(1).
- `size()`: Returns the number of items in the queue. Time complexity: O(1).

### DynamicArrayQueue

This implementation uses a Python list as the underlying storage. The `DynamicArrayQueue` class supports the same operations as `LinkedListQueue`, but with different time complexities:

- `enqueue(item)`: Time complexity: O(1) amortized.
- `dequeue()`: Time complexity: O(n), where n is the number of items in the queue.

The dynamic array implementation demonstrates the trade-offs between different backing data structures for queues.

## Binary Tree

The `BinaryTree` class in `binary_tree.py` implements a basic binary tree structure. It uses a `TreeNode` class to represent individual nodes. The binary tree supports:

- `insert(val)`: Inserts a new node with the given value into the tree using level-order traversal. Time complexity: O(n) in the worst case, where n is the number of nodes.
- `inorder_traversal(node)`: Performs an inorder traversal of the tree, printing node values.

This implementation demonstrates tree traversal techniques and the use of a queue for level-order insertion.

## Graph

The `Graph` class in `graph.py` implements an undirected graph using an adjacency list representation. The graph supports:

- `add_vertex(vertex)`: Adds a new vertex to the graph. Time complexity: O(1).
- `add_edge(vertex1, vertex2)`: Adds an undirected edge between two vertices. Time complexity: O(1).
- `print_graph()`: Displays the graph structure.

This implementation showcases the use of a dictionary for efficient vertex and edge management in graphs.

## Heap

The `heap.py` file contains implementations for both MinHeap and MaxHeap:

### MinHeap

The `MinHeap` class implements a binary heap where the parent is always smaller than its children. It supports:

- `insert(key)`: Inserts a new key into the heap. Time complexity: O(log n).
- `extract_min()`: Removes and returns the minimum element. Time complexity: O(log n).

### MaxHeap

The `MaxHeap` class is similar to `MinHeap` but maintains the property that the parent is always larger than its children. It supports:

- `insert(key)`: Inserts a new key into the heap. Time complexity: O(log n).
- `extract_max()`: Removes and returns the maximum element. Time complexity: O(log n).

Both heap implementations demonstrate the use of array-based representation of trees and the heapify process.

## Priority Queue

The `PriorityQueue` class in `priority_queue.py` implements a priority queue using a `MinHeap`. It supports:

- `enqueue(item, priority)`: Adds an item with a given priority to the queue. Time complexity: O(log n).
- `dequeue()`: Removes and returns the item with the highest priority (lowest priority value). Time complexity: O(log n).
- `is_empty()`: Checks if the priority queue is empty. Time complexity: O(1).

This implementation showcases the use of a heap for efficient priority queue operations.

## Hash Table

The `HashTable` class in `hash_table.py` implements a basic hash table (also known as a hash map) using separate chaining for collision resolution. The hash table supports the following operations:

- `insert(key, value)`: Adds a key-value pair to the hash table or updates the value if the key already exists. Time complexity: O(1) average case, O(n) worst case where n is the number of items in the bucket.
- `get(key)`: Retrieves the value associated with the given key. Time complexity: O(1) average case, O(n) worst case.
- `remove(key)`: Removes a key-value pair from the hash table. Time complexity: O(1) average case, O(n) worst case.

The implementation uses a simple hash function based on Python's built-in `hash()` function and the modulo operator. It demonstrates:

- The use of separate chaining to handle collisions.
- Dynamic resizing is not implemented, showcasing a basic fixed-size hash table.
- Key concepts such as hash functions, collision resolution, and basic hash table operations.

This hash table implementation provides a foundation for understanding hash-based data structures and can be extended to include more advanced features like dynamic resizing and alternative collision resolution strategies.

These data structure implementations provide a solid foundation for understanding core computer science concepts and can be used as building blocks for more complex algorithms and applications.
