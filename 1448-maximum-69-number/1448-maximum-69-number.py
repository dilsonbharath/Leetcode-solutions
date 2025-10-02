class Solution:
    def maximum69Number (self, num: int) -> int:
        x = []
        while num>0:
            a = (num//10)*10
            x.append(num-a)
            num = num//10
        n = len(x)
        i=0
        x.reverse()
        while i<n:
            if x[i]==6:
                x[i]=9
                i=n
            i+=1
        c = 0
        for i in x:
            c = (c*10)+i
        return c


        