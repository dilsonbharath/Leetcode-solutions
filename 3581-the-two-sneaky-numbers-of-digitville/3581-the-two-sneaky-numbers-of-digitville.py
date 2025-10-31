class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        di = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                if i not in di:
                    di[i]=2
                else:
                    del di[i]
        return list(di.keys())