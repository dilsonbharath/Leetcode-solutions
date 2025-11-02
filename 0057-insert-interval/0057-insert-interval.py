class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # n = len(intervals)
        # l = 0
        # r = n-1
        # while l<r:
        #     pass
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        merged = []
        for i in intervals:
            if not merged or merged[-1][1]<i[0]:
                merged.append(i)
            else:
                merged[-1][1]=max(i[1],merged[-1][1])
        return merged
        
