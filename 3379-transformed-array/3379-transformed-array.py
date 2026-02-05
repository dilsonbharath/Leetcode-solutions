class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [0 for _ in range(n)]

        for i in range(n):

            if nums[i]==0:
                result[i] = nums[i]

            # elif nums[i]>0:

            #     x = (nums[i] + i)%n
            #     result[i] = nums[x]

            else:

                y = (nums[i]+i)%n
                result[i] = nums[y]

        return result