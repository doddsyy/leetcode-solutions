class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1:
            return False
        return sum([n%x == 0 for x in range(1 ,n+1)]) == 3
