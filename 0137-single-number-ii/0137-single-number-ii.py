class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        di = {}

        for i in nums:
            if i not in di:
                di[i] = 1
            else:
                if di[i] == 2:
                    del di[i]
                else:
                    di[i] += 1

        return list(di.keys())[0]