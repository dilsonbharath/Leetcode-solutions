class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        di1 = ['a','c','e','g']

        return coordinates[0] in di1 and int(coordinates[1])%2==0 or coordinates[0] not in di1 and int(coordinates[1])%2!=0