class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0 for _ in range(len(temperatures))]
        stack = []

        for i,t in enumerate(temperatures):

            while stack and stack[-1][1]<temperatures[i]:
                
                ans = (i - stack[-1][0])
                res[stack[-1][0]] = ans
                stack.pop()

            stack.append([i,t])

        return res