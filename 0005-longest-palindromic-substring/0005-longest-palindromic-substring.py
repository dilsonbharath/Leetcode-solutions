class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ans = ''

        for i in range(len(s)):

            for j in range(i,len(s)):

                curr = s[i:j+1]

                if curr == curr[::-1] and len(curr)>len(ans):

                    ans = curr

        return ans










