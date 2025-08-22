class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        for num in nums:
            if num in s:
                s[num]+=1
            else:
                s[num]=1
        n = sorted(s,key=s.get,reverse=True)
        return n[:k]