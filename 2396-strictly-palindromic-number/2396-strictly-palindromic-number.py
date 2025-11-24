class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def palindromic(n,x):
        
            ans = ""

            while n>0:

                ans += str(n%x)

                n //= x

            return ans == ans[::-1]

        for i in range(2,n-1):

            if not palindromic(n,i):

                return False

        return True