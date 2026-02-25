class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        x = str(n)
        x = x[::-1]

        return abs(n - int(x))