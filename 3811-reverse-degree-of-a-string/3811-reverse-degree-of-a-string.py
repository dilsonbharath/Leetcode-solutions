class Solution:
    def reverseDegree(self, s: str) -> int:
        x = 0
        for i in range(len(s)):
            x = x + ((i+1)*(123-ord(s[i])))
        return x
        