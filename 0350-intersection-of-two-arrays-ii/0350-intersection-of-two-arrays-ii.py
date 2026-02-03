class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dict1 = {}
        dict2 = {}

        for i in nums1: 
            if i not in dict1:
                dict1[i] = 1

            else:
                dict1[i]+=1

        for i in nums2: 
            if i not in dict2:
                dict2[i] = 1

            else:
                dict2[i]+=1

        ans = []
        for i in dict1:

            if i in dict2:

                x = min(dict1[i],dict2[i])

                for _ in range(x):

                    ans.append(i)

        return ans

