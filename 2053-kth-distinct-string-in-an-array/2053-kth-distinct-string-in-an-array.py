class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        di = {}

        sett = set()

        for i in arr:

            if i not in sett:

                di[i] = 1
                sett.add(i)

            else:

                if i in di:
                    
                    del di[i]

            
        i = 1

        for key in di:

            if i == k:

                return key

            i +=1
        
        return ""

            




