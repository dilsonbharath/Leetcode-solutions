class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        di = {}
        for i in nums:
            if i not in di:
                di[i]=1
            else:
                di[i]+=1
        for key, values in di.items():
            if values==1:
                return key