class Solution:
    def minOperations(self, s: str) -> int:

        c,d = 0,0
        
        for i in range(len(s)):

            if i%2 == 0:
                
                if s[i] == '0':

                    c+=1

                else:
                    d += 1

            else:

                if s[i] == '1':

                    c+=1

                else:
                    d += 1

        return min(c,d)

                
