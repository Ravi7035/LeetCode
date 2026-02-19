class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} 
        
        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove node from list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert node right after head (Most Recently Used)
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        
        # Move to front (MRU)
        self.remove(node)
        self.insert(node)
        
        return node.value

    def put(self, key, value):
        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])
        
        # Create new node
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        
        # Check capacity
        if len(self.cache) > self.capacity:
            # Remove LRU (node before tail)
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
