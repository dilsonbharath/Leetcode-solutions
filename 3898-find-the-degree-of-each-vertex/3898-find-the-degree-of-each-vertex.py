class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        
        ans = []
        n = len(matrix)

        for i in range(n):

            x = 0

            for j in range(n):

                if i != j and matrix[i][j] == 1:

                    x += 1

            ans.append(x)

        return ans