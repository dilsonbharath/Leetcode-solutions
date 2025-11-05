class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        di = {n:i for i,n in enumerate(nums1)}
        
        res = [-1]*len(nums1)

        stack = []

        for i in range(len(nums2)-1):

            for j in range(i+1,len(nums2)):

                if nums2[i] in nums1 and nums2[i]<nums2[j]:

                    res[di[nums2[i]]] = nums2[j]
                    break
        
        return res
