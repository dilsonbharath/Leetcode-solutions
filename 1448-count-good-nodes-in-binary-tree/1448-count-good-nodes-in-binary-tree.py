# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ans = []

        maxx = float('-inf')

        def recursive(node,maxx):

            if node.val>=maxx:

                ans.append(node.val)
                maxx = node.val

            if node.left: recursive(node.left,maxx)
            if node.right: recursive(node.right,maxx)
        
        recursive(root,maxx)
        return len(ans)