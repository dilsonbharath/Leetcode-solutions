class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        ans = []
        
        for i in range(left,right+1):

            x = str(i)
            count = 0

            for j in x:

                y = int(j)
                if y != 0 and i%y == 0:

                    count += 1

            if count == len(x):

                ans.append(i)

        return ans

