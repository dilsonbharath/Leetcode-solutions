class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        x = 0
        sett = set()
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            w = (r-l) +1
            x = max(w,x)
            sett.add(s[r])
        return x

        