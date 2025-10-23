class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {'}',')',']'}
        di = {'}':'{',')':'(',']':'['}
        for i in s:
            if i in d and stk and stk[-1]==di[i]:
                stk.pop()
            else:
                stk.append(i)
        return len(stk)==0