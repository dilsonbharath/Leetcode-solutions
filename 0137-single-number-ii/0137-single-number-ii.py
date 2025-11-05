class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        di = {}

        for i in nums:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1

        for i,j in di.items():
            if j==1:
                return i

        return -1