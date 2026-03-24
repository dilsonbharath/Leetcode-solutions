class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        ans = []
        stack = []

        for i in range(1,n+1):

            if stack == target:
                return ans

            stack.append(i)
            ans.append("Push")

            if stack and stack[-1] not in target:

                ans.append("Pop")
                stack.pop()

        return ans

