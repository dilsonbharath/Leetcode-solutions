class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums,ans = [],[]

        def backtrack(j):

            if len(nums) == k:

                ans.append(nums[:])
                return

            for i in range(j,n+1):

                nums.append(i)
                backtrack(i+1)
                nums.pop()

        backtrack(1)
        return ans
                
