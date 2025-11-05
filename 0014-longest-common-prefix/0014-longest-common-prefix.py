class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""

        minn = 201

        for i in strs:

            if len(i)<minn:

                minn = len(i)

        k = 0

        for i in range(minn):

            che = strs[0][k]

            m = 1

            for j in range(1,len(strs)):

                if strs[j][k] == che:

                    m += 1

                else:

                    break

            k += 1

            if m == len(strs):

                res += che

            else:

                break

            

        return res
                       



        





