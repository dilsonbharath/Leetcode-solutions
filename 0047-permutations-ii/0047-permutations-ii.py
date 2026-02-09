class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        arr = []

        count = {}

        for x in nums:

            if x not in count:
                count[x] = 1
            else:
                count[x]+=1

        def rec():
            
            if len(arr) == len(nums):

                ans.append(arr[:])
                return

            

            for x in count:

                if count[x]>0:
                    arr.append(x)
                    count[x]-=1

                    rec()
                    
                    count[x]+=1
                    arr.pop()

        rec()
        return ans
        
