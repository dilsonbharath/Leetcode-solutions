class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i in range(len(nums)):
            for j in range(i+1):
                if i!=j and target==nums[i]+nums[j]:
                    lst.append(i)
                    lst.append(j)
                    break

        lst.sort()
        return lst