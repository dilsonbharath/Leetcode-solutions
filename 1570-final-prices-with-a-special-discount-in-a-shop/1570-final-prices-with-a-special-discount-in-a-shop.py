class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        res = prices
        stack = []

        for i,p in enumerate(prices):

            while stack and stack[-1][1]>=p :

                ind,pri = stack.pop()
                res[ind] = pri - p
            
            stack.append([i,p])

        return res