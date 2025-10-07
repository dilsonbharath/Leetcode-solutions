class Solution:
    def maxFreqSum(self, s: str) -> int:
        dv={}
        d={}
        vo = ('a','e','i','o','u')
        for i in s:
            if i in vo:
                if i in dv:
                    dv[i]+=1
                else:
                    dv[i]=1
            else:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
        max_vow=0
        max_cons=0
        for i in dv.values():
            if max_vow<i:
                max_vow=i
        for i in d.values():
            if max_cons<i:
                max_cons=i


        return max_vow+max_cons