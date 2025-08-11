class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)-1
        sum = 0
        temp = n
        k = 0
        for i in range(n+1):
            x = ord(columnTitle[temp])-64
            temp-=1
            sum+= pow(26,k)*x
            k+=1
        return sum


        