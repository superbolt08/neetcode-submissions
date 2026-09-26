"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        # Pass 1: create all the clone nodes (val only), map old -> clone
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val) 
            curr = curr.next

        # Pass 2: wire up next and random on the clones
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new.get(curr.next, None) 
            copy.random = old_to_new.get(curr.random, None)
            curr = curr.next

        return old_to_new[head]