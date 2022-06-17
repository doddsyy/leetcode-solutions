class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for x in range(31):
            if 3**x == n:
                return True
                break
            else:
                continue
