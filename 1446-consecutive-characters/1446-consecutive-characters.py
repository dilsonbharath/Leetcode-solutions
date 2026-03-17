class Solution:
    def maxPower(self, s: str) -> int:
        
        curr = 0
        stack = []
        stack.append(s[0])
        max_len = 0

        for i in s[1:]:

            if stack[-1] == i:

                curr += 1
                max_len = max(curr,max_len)
 
            else:

                curr = 0
                stack.append(i)

        return max_len+1