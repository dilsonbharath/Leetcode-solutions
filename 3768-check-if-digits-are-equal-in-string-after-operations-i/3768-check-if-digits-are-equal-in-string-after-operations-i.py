class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            temp = s
            new = ""
            for i in range(len(temp)-1):
                x = (int(temp[i])+int(temp[i+1]))%10
                new += str(x)
            s = new

        return s[0]==s[1]
