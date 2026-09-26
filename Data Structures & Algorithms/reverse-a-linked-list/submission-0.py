# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        dummy = ListNode(0)
        curr = dummy
        while stack:
            curr.next = ListNode(stack.pop())       # create a new node with the popped value
            curr = curr.next

        return dummy.next

