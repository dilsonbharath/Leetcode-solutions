class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        nums.sort()
        med = nums[len(nums)//2] 
        steps = 0

        for i in nums:

            steps += abs(med - i)       

        return steps