class Solution:
    def bitwiseComplement(self, n: int) -> int:

        if n == 0: return 1

        num = ''
        
        while n>0:

            if n%2 == 0:

                num += '1'
            
            else:

                num += '0'

            n = n//2

        num = num[::-1]
        
        res = 0

        for i in num:

            res = res*2 + int(i)

        return res

        