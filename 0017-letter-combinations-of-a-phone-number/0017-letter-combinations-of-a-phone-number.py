class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        di = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        ans = []
        s = []

        def fun(i):

            if len(s) == len(digits):

                ans.append(''.join(s[:]))
                return

            num = digits[i]

            for j in di[num]:

                s.append(j)
                fun(i+1)
                s.pop()

        fun(0)
        return ans

