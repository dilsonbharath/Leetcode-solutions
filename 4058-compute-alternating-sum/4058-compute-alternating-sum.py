class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        x = 0
        for i in range(len(nums)):
            if i%2==0:
                x+=nums[i]
            else:
                x-=nums[i]
        return x