class Solution:
    def findMin(self, nums: List[int]) -> int:  
        l = 0
        r = len(nums)-1
        while l<r:
            if nums[l]==nums[r] or nums[r]>nums[l]:
                r-=1
            else: 
                l+=1
        return nums[l]