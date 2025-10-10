class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d={}
        for i in range(len(t)):
            d[t[i]] = i
        x = 0
        for i in range(len(s)):
            a = d.get(s[i])
            x += abs(a-i)
        return x