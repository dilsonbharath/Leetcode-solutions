class Solution:
    def longestPalindrome(self, s: str) -> int:

        di = {}
        
        for i in s:

            if i not in di:

                di[i] = 1

            else:

                di[i]+=1

        ans = 0
        odd = 0

        for i,j in di.items():

            if j%2 == 0:

                ans+=j

            else:
                
                ans += (j-1)
                odd = 1

        if odd:

            return ans+1

        return ans
