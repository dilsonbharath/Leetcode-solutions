class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph = {}

        n = len(edges)

        for i,j in edges:

            if i not in graph:

                graph[i] = []

            graph[i].append(j)

            if j not in graph:

                graph[j] = []

            graph[j].append(i)

        for key,value in graph.items():

            if len(value) == n:

                return key

        