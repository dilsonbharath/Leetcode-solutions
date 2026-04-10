class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        ans = float('inf')
        n = len(nums)

        flag = True
        
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):

                    if nums[i] == nums[j] == nums[k]:
                        curr = abs(i-j) + abs(j-k) + abs(k-i)
                        flag = False
                    
                        if curr<ans: ans = curr
                        
        if flag: return -1
        return ans