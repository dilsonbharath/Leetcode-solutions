class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arr = []
        for i in range(len(boxes)):
            summ = 0
            for j in range(len(boxes)):
                if i!=j and boxes[j]=='1':
                    summ+=abs(i-j)
            arr.append(summ)
        return arr

        
        
         
        