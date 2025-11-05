class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        res = [-1] * len(nums)

        n = len(nums)
        
        stack = []

        nums = nums * 2

        for i,j in enumerate(nums):
            
            while stack and stack[-1][1] < j:

                idx,val = stack.pop()
                res[idx] = j

            if i<n:

                stack.append([i,j])

        return res