class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        
        ans = []

        for i in words:

            x = ''

            for j in i:

                if j == separator:

                    if x:
                        ans.append(x)
                        x = ""

                else:

                    x += j

            if x: ans.append(x)

        return ans

