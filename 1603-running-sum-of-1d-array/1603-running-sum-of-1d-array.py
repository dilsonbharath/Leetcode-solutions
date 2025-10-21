class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        su = 0
        for i in nums:
            su+=i
            res.append(su)
        return res