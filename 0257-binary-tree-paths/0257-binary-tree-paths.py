# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        ans,arr = [],[]

        def dfs(node):

            if not node:

                return

            if node:

                arr.append(node.val)

            if not node.left and not node.right:

                ans.append(arr[:])
                return

            if node.left:
                
                dfs(node.left)
                arr.pop()

            if node.right:

                dfs(node.right)
                arr.pop()

        dfs(root)

        res = []

        for i in ans:

            res.append("->".join(map(str,i))) 

        return res









        