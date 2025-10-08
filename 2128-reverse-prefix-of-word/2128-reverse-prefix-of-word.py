class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x=""
        a=1
        for i in word:
            if i!=ch:
                x+=i
                a+=1
            else:
                x+=i
                break
        if a-1==len(word):
            m = x
        else:
            m=x[::-1]
        return m+word[a:]