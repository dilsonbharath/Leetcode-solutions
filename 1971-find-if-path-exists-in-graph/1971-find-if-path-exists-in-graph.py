from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:

            return True

        graph = {}

        for i,j in edges:

            if i not in graph: graph[i] = []
            if j not in graph: graph[j] = []

            graph[i].append(j)
            graph[j].append(i)


        q = deque()
        q.append(source)
        sett = set()
        sett.add(source)

        while q:

            curr = q.popleft()
            for child in graph[curr]:

                if child == destination:

                    return True

                if child not in sett:

                    sett.add(child)
                    q.append(child)

        return False

                
        