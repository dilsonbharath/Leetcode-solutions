class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        point = 0 

        start = 0

        if sum(gas)<sum(cost):

            return -1

        for i in range(len(gas)):

            point += gas[i]

            point -= cost[i]

            if point<0:

                point = 0

                start = i + 1

        return start