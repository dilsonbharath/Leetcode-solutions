class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num<0:

            return False

        x = num**0.5

        return x == int(x)