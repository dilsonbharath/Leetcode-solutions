class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = float('inf')
        for price in prices:
            if price<minprice:
                minprice=price
            
            x = price-minprice
            if x>profit:
                profit=x
        return profit