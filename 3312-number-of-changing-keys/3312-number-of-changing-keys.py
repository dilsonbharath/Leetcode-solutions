class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        x = 0
        n = len(s)
        for i in range(1,n):
            if s[x].lower()!=s[i].lower():
                count+=1
                x = i
        return count
        