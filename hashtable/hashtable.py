class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        hash = FNV_offset_basis
        for byte in key.encode():
            hash = hash * FNV_prime  # returns the lower 64-bits of the product
            # print("Hash before:", hash)
            hash = hash ^ byte  # 8-bit operation that modifies only the lower 8-bits of the hash value
            # print("Hash after:", hash)
        return hash  # return as a 64-bit unsigned integer

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)  # find the hash index
        node = self.storage[index]
        if node is None:  # it's free real estate! https://knowyourmeme.com/memes/its-free-real-estate
            self.storage[index] = HashTableEntry(key, value)
        else:
            if node.key != key:  # if we aren't overwriting
                while node.next is not None:  # while we can keep going to the right
                    if node.key != key:  # if it, again, isn't overwriting
                        node = node.next  # keep going
                    else:
                        node.value = value  # assign the value
                if node.key == key:  # we found it, we are overwriting
                    node.value = value
                else:
                    # we are attaching it to the end
                    node.next = HashTableEntry(key, value)
            else:
                node.value = value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        if node is not None:  # while we have items to search through
            while node.next is not None:  # while we are not at the end
                if node.key == key:  # found it!
                    return node.value  # so, return it!
                else:
                    node = node.next  # keep going
            if node.key == key:
                return node.value  # found it (first item)
            else:
                return None
        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
