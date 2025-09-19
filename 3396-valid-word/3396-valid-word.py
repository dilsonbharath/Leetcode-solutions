class Solution:
    def isValid(self, word: str) -> bool:
        vowel = 'aeiou'
        vowel += vowel.upper()
        cons = 'bcdfghjklmnpqrstvwxyz'
        cons += cons.upper()
        num = '0123456789'+vowel+cons
        hasvow = False
        hascons = False
        n = len(word)
        if n<3:
            return False
        for i in word:
            if i not in num:
                return False
            if i in vowel:
                hasvow = True
            if i in cons:
                hascons = True
        return hasvow and hascons
        
        