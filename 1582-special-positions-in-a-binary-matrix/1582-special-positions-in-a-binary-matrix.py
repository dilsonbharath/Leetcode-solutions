class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        m = len(mat[0])

        ans = 0

        def fun(x,y):

            count = 0

            for i in range(m):

                if mat[x][i] == 1:

                    count += 1

            for j in range(n):

                if mat[j][y] == 1:

                    count += 1
            
            return count == 2


        for i in range(n):

            for j in range(m):

                if mat[i][j] == 1:

                    if fun(i,j):

                        ans += 1

        return ans

            




