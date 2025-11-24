class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        res = []

        x  = ""

        for i in nums:

            x += str(i)

            if (int(x,2))%5==0:

                res.append(True)

            else:

                res.append(False)

        return res
