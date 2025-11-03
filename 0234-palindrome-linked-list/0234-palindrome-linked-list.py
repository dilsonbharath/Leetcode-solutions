# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        dummy = ListNode(0,head)
        curr = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            curr = curr.next
        
        dummy = dummy.next
        second = None
        while slow:
            temp = slow.next
            slow.next = second
            second = slow
            slow = temp
        
        while second:
            if second.val != head.val:
                return False
            second = second.next
            head = head.next
        return True
