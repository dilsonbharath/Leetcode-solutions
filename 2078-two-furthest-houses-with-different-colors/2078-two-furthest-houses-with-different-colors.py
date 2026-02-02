class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        maxx = 0

        for i in range(len(colors)-1):

            for j in range(i+1,len(colors)):

                if colors[i]!=colors[j]:

                    if maxx < j-i:

                        maxx = j-i

        return maxx



