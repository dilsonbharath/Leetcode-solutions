class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        hash = []
        
        for i in arr:

            if i*2 in hash:

                return True

            elif i%2==0 and i//2 in hash:

                return True

            else: 
                
                hash.append(i)

        return False