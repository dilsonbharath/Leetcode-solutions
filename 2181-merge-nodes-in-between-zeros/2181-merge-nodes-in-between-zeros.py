# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy
        curr = 0

        while head:

            if head.val == 0 and curr>0:

                tail.next = ListNode(curr)
                tail = tail.next
                curr = 0

            curr += head.val

            head = head.next

        return dummy.next