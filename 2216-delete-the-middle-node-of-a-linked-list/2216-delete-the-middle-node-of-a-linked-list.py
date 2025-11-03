# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        fast = head
        while fast and fast.next:
            head = head.next
            curr = curr.next
            fast = fast.next.next
        curr.next = curr.next.next
        return dummy.next