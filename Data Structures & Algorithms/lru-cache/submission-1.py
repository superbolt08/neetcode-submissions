class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}  # key -> Node
        
        # Dummy head and tail nodes simplify pointer operations
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def _remove(self, node: Node) -> None:
        """Remove an existing node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        
        node = self.table[key]
        # Accessing key makes it most recently used -> move to head
        self._remove(node)
        self._add_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            # Update value and move to head
            node = self.table[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # If capacity reached, remove LRU item (node right before tail)
            if len(self.table) == self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.table[lru_node.key]

            # Insert new key-value pair
            new_node = Node(key, value)
            self.table[key] = new_node
            self._add_to_head(new_node)
