class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        letters = ['a','b','c']

        ans = []
        arr = []

        def recursive():

            if len(arr) == n:

                ans.append("".join(arr))
                return

            for i in letters:

                if not arr or arr[-1] != i:

                    arr.append(i)
                    recursive()
                    arr.pop()

        recursive()

        if len(ans) < k: return ""

        return ans[k-1]

        
        