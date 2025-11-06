class Solution:
    def convert(self, s: str, numRows: int) -> str:

        res = [[] for _ in range(numRows)]

        if numRows == 1:

            return s

        i = 0 

        d = 0

        for l in s:

            res[i].append(l)

            if i == 0:

                d = 1

            elif i == numRows - 1:

                d = -1

            i += d

        return ''.join(''.join(row) for row in res)
            
