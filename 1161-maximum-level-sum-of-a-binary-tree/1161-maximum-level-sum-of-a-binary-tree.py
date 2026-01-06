# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:

            return 0

        maxx = []

        q = deque()
        seen = set()

        q.append(root)

        while q :

            n = len(q)
            curr = 0

            for i in range(n):

                node = q.popleft()
                curr += node.val

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            maxx.append(curr)

        

        return maxx.index(max(maxx))+1



            






        