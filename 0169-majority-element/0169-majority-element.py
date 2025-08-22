class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        
        maxel=-1
        ans = -1
        for key,val in counter.items():
            if val>maxel:
                maxel= val
                ans=key
        return ans
        