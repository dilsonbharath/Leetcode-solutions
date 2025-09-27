class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        let = {}
        for j in magazine:
            if j in let:
                let[j]+=1
            else:
                let[j]=1
        for i in ransomNote:
            if i not in let:
                return False
            if let[i]==1:
                let.pop(i)
            else: let[i]-=1
        return True

        