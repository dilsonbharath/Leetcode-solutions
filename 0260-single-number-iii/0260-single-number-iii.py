class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        di = {}

        for i in nums:

            if i not in di:
                
                di[i] = 1

            else:
                 
                del di[i]

        return list(di.keys())