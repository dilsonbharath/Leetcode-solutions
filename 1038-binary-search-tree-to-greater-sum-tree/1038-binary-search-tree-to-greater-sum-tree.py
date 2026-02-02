# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.curr = 0

        def bfs(node):

            if not node: return

            if node.right: bfs(node.right)

            self.curr += node.val

            node.val = self.curr

            if node.left: bfs(node.left)

        bfs(root)

        return root






        