class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a = []
        n=len(nums)
        for i in range(n):
            lo , hi = i+1 , n-1
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            while lo<hi:
                summ = nums[i]+nums[lo]+nums[hi]
                if summ==0:
                    a.append([nums[i],nums[lo],nums[hi]])
                    lo+=1
                    hi-=1
                    while lo<hi and nums[lo]==nums[lo-1]:
                        lo+=1
                    while lo<hi and nums[hi]==nums[hi+1]:
                        hi-=1
                elif summ > 0:
                    hi-=1
                else:
                    lo+=1
        return a

        