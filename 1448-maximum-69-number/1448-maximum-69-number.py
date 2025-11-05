class Solution:
    def maximum69Number (self, num: int) -> int:
        
        num = str(num)

        i = -1

        for j in range(len(num)):

            if num[j] == '6':

                i = j

                break

        if i == -1:

            return int(num)

        return int(num[:i]+'9'+num[i+1:])