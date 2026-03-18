class Solution:
    def minMoves(self, nums: List[int]) -> int:

        s = 0
        max_num = min(nums)

        for i in nums:

            s += abs(max_num - i)

        return s





        