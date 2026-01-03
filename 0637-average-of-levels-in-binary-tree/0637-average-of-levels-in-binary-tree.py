# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        ans = []

        q = deque()
        q.append(root)

        while q:

            n = len(q)

            tot = 0

            for i in range(n):

                node = q.popleft()

                tot += node.val

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            ans.append(tot/n)

        return ans
        