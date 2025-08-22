class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxdiff = 0
        minnum = float('inf')
        for num in nums:
            if minnum>num:
                minnum=num
            
            diff = num - minnum
            if diff>maxdiff:
                maxdiff=diff

        if maxdiff>0:
            return maxdiff
        return -1


        