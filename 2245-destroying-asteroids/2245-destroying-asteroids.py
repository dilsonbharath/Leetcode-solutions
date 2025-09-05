class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        stk = []
        asteroids.sort()
        for a in asteroids:
            stk.append(a)
            while stk and stk[-1]<=mass:
                mass+=stk.pop()
        return not stk
        