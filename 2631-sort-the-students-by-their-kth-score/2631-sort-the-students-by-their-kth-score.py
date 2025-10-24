class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(score)):
            for i in range(1,len(score)):
                if score[i-1][k]<score[i][k]:
                    score[i-1],score[i]=score[i],score[i-1] 
        return score
