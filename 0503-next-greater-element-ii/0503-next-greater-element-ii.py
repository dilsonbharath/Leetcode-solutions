class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        res = [-1] * len(nums)
        
        

        for i in range(len(nums)):
            
            x = nums[i]

            for j in range(1,len(nums)):

                y = nums[(i+j)%len(nums)]
                
                if y>x:

                    res[i] = y
                    break

        return res

        

        