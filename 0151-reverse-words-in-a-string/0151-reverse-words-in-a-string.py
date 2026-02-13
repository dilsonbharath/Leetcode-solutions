class Solution:
    def reverseWords(self, s: str) -> str:
        
        arr = []
        strs = ""

        for i in range(len(s)):

            if s[i]!= " ":

                strs += s[i]

            if s[i] == " " and len(strs)!=0:

                arr.append(strs)
                strs = ""

        if len(strs) != 0:
            arr.append(strs)

        arr = arr[::-1]
        return " ".join(arr)