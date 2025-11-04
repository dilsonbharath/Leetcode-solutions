# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        curr = second = dummy

        for i in range(k):
            curr = curr.next

        first = curr

        while curr:
            curr = curr.next
            second = second.next

        x,y = first.val,second.val
        first.val,second.val = y,x

        return dummy.next
        