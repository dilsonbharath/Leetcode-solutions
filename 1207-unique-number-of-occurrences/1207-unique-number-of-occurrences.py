class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        di = {}

        for i in arr:
            
            if i in di:

                di[i]+=1

            else: di[i]=1

        sett = set()

        for i in di.values():

            if i in sett:

                return False

            else:

                sett.add(i)

        return True