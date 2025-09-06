class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1=set(nums1)
        s2=set(nums2)
        common=s1&s2
        if common:
            return min(common)
        x = min(s1)
        y = min(s2)
        return min(x*10 +y,y*10+x)
        