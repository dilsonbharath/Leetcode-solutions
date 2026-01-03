# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        ans = []

        q = []
        q.append(root)

        while q:

            n = len(q)

            tot = 0

            for i in range(n):

                node = q.pop(0)

                tot += node.val

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            ans.append(tot/n)

        return ans
        