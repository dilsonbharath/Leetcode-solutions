class Solution:
    def maxDistinct(self, s: str) -> int:

        sett = set()
        
        for i in s:

            if i not in sett:

                sett.add(i)

        return len(sett)
