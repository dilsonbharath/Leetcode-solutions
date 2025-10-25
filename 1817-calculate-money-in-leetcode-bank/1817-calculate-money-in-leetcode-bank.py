class Solution:
    def totalMoney(self, n: int) -> int:
        rem = n%7
        no = n//7

        ans =  28*(no) + (no*(no-1)//2)*7 + ((rem*(rem+1))//2) + (no*rem)
        return ans