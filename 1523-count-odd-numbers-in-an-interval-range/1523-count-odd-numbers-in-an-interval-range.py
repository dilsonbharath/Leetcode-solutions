class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        tot = high - low + 1

        if tot%2==0 or low%2==0:

            return tot//2

        return tot//2 + 1