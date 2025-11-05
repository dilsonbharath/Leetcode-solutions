class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        di = {n:i for i,n in enumerate(nums1)}
        
        res = [-1]*len(nums1)

        stack = []

        for i in range(len(nums2)):

            curr = nums2[i]

            while stack and stack[-1]<curr:

                val = stack.pop()
                idx = di[val]
                res[idx] = curr

            if curr in nums1:
                stack.append(curr)
            
        return res
