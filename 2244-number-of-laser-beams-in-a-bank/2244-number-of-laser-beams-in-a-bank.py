class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        pre = 0
        for i in bank:
            c = 0
            for j in i:
                if int(j) == 1:
                    c+=1
            if c>0:
                ans+= pre*c
                pre = c
        return ans

                