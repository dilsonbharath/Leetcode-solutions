class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = len(word1)
        y = len(word2)
        a = min(x,y)
        s = ""
        for i in range(a):
            s = s+word1[i]+word2[i]
        if a==x:
            s+=word2[a:]
        else:
            s+=word1[a:]
        return s