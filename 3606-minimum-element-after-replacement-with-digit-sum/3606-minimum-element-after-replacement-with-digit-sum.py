class Solution:
    def minElement(self, nums: List[int]) -> int:
        x = []
        for i in nums:
            a = 0
            while i>0:
                k= i//10
                a+=(i-(k*10))
                i=i//10
            x.append(a)
        return min(x)
        
            