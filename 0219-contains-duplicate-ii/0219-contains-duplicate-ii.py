class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        di = {}

        for i in range(len(nums)):

            if nums[i] in di and i - di[nums[i]] <= k:
                return True

            di[nums[i]] = i

        return False