class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        di = {}
        
        for i in range(len(heights)):

            di[heights[i]] = names[i]

        heights.sort(reverse=True)

        ans = []

        for i in heights:

            ans.append(di[i])

        return ans