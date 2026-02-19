class Solution:
    def reverseByType(self, s: str) -> str:
        
        ch = []
        sy = []

        for i in s:

            if 'a' <= i <= 'z':
                ch.append(i)
            else: sy.append(i)

        ch = ch[::-1]
        sy = sy[::-1]

        i = 0
        j = 0

        ans = ""

        for c in s:

            if 'a' <= c <= 'z':

                ans+=ch[i]
                i+=1

            else:

                ans += sy[j]
                j+=1

        return ans