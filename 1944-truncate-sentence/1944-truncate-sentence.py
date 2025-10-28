class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        x = s.split()
        x  = x[:k]
        return " ".join(x)