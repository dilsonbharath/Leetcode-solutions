class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 1
        r = 1
        le = [0]*n
        ri = [0]*n
        for i in range(n):
            j = -i-1
            le[i]=l
            ri[j]=r
            l*= nums[i]
            r*= nums[j]
        return [l*r for l,r in zip(le,ri)]
        