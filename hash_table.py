class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        """
        Simple hash function that uses the built-in hash() and modulo.
        This is for demonstration purposes; in practice, you'd use a more sophisticated hash function.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Update value if key already exists
                return
        self.table[index].append([key, value])

    def get(self, key):
        """Retrieve the value associated with the given key."""
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def remove(self, key):
        """Remove a key-value pair from the hash table."""
        index = self._hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return
        raise KeyError(key)

    def __str__(self):
        """Return a string representation of the hash table."""
        return str(self.table)

# Demonstration of usage
if __name__ == "__main__":
    ht = HashTable()

    # Insert some key-value pairs
    ht.insert("apple", 5)
    ht.insert("banana", 7)
    ht.insert("orange", 3)

    # Print the hash table
    print("Hash Table after insertions:")
    print(ht)

    # Retrieve values
    print("\nRetrieving values:")
    print("apple:", ht.get("apple"))
    print("banana:", ht.get("banana"))

    # Update a value
    ht.insert("apple", 10)
    print("\nAfter updating 'apple':")
    print("apple:", ht.get("apple"))

    # Remove a key-value pair
    ht.remove("banana")
    print("\nAfter removing 'banana':")
    print(ht)

    # Try to get a non-existent key
    try:
        ht.get("grape")
    except KeyError:
        print("\nTried to get 'grape', but it's not in the hash table.")
