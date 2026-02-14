class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]
        
        for r in range(1, query_row + 1):
            new = [0.0] * (r + 1)
            for i in range(len(dp)):
                overflow = max(0.0, dp[i] - 1)
                new[i] += overflow / 2
                new[i+1] += overflow / 2
            dp = new
        
        return min(1.0, dp[query_glass])