# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        nums = []
        
        while head is not None:

            nums.append(head.val)
            head = head.next
        
        if not nums:

            return None

        def bst(l,r):

            if l>r:
                return None

            mid = (l+r)//2

            node = TreeNode(nums[mid])

            node.left = bst(l,mid-1)
            node.right = bst(mid+1,r)

            return node

        return bst(0,len(nums)-1)