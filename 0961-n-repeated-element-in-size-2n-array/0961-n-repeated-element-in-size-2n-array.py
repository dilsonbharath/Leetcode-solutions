class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        di = []

        for i in nums:

            if i not in di:

                di.append(i)

            else:

                return i