class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        o = ['1']
        z = ['0']

        for i in range(len(nums)-1):

            o.append('1')
            z.append('0')

        if ''.join(o) not in nums:

            return ''.join(o)

        if ''.join(z) not in nums:

            return ''.join(z)

        for i in range(len(nums)):

            o[i] = '0'

            if ''.join(o) not in nums:

                return ''.join(o)

            z[i] = '1'

            if ''.join(z) not in nums:
                
                return ''.join(z)
