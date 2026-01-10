#design hashmap
class ListNode:
    """
    A node for our linked list (the chain inside each bucket).
    It stores the key-value pair and a pointer to the next node.
    """
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize the data structure.
        We create a list of 10,000 buckets.
        We put a dummy node (0,0) in every bucket to make handling the 
        linked list easier (we never have to deal with an empty bucket/None).
        """
        self.size = 10**4
        self.set = [ListNode(0, 0) for _ in range(self.size)] 

    def put(self, key: int, value: int) -> None:
        """
        Inserts a (key, value) pair into the HashMap.
        If the key already exists, update the corresponding value.
        """
        # 1. Find the correct bucket index using modulo
        index = key % self.size
        
        # 2. Get the dummy head of the linked list at that index
        cur = self.set[index]
        
        # 3. Walk through the linked list to check if key exists
        while cur.next:
            if cur.next.key == key:
                # Key found! Update the value
                cur.next.val = value
                return
            cur = cur.next
        
        # 4. If we reach here, the key was not found. 
        # Create a new node and add it to the end of the chain.
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, 
        or -1 if this map contains no mapping for the key.
        """
        index = key % self.size
        cur = self.set[index]
        
        # Traverse the list looking for the key
        while cur.next:
            if cur.next.key == key:
                # Key found! Return its value
                return cur.next.val
            cur = cur.next
        
        # If the loop finishes without finding the key, return -1
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map 
        contains a mapping for the key.
        """
        index = key % self.size
        cur = self.set[index]
        
        # Traverse looking for the node to delete
        while cur.next:
            if cur.next.key == key:
                # Key found! Skip over this node to remove it
                # (Connect current node to the node AFTER the next one)
                cur.next = cur.next.next
                return
            cur = cur.next
