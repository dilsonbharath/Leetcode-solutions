# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        Node = ListNode(0)
        Node.next = head
        curr = Node
        c = head
        while head:
            if head.val==val:
                curr.next = curr.next.next
            else:
                curr = curr.next
            head = head.next
        return Node.next
        