class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=0
        n=len(nums)
        arr = []
        while i<n:
            x = nums[i]
            if i<n-1 and nums[i]==nums[i+1]-1:
                x = nums[i]
                y = x
                while i<n-1 and nums[i]+1==nums[i+1]:
                    i+=1
                    y+=1
                i+=1
                arr.append(str(x)+"->"+str(y))
            else:
                arr.append(str(nums[i]))
                i+=1
                
        return arr

        