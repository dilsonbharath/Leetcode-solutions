class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        du = {}

        for i in strs:
            j=sorted(i)
            j = "".join(j)
            if j not in du:
                du[j] = [i]
            else:
                du[j].append(i)
        return list(du.values())