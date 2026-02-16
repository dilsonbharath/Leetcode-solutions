class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        di = {}

        i = 97

        ans = ""
        
        for c in key:

            if c != ' ' and ord(c) not in di:

                di[ord(c)] = i
                i += 1

        for k in range(len(message)):

            if message[k]!=" ":

                x = ord(message[k])
                ans += chr(di[x])

            else:

                ans += message[k]

        return ans