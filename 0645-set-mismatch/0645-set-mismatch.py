class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        num = ((n*(n+1))//2)-sum(set(nums))
        
        s = set()
        for i in nums:
            if i in s:
                return [i,num]

            s.add(i)
