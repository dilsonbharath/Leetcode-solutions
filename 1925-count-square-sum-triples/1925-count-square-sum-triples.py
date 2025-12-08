class Solution:
    def countTriples(self, n: int) -> int:

        di = {i*i: i for i in range(1,n+1)}

        count = 0
        
        for i in range(1,n+1):

            for j in range(1,n+1):

                x = i**2 + j**2 

                if x in di and di[x] <=n:

                    count+=1

        return count