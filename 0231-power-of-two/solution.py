class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for x in range(31):
            if 2**x == n:
                return True
                break
            else:
                continue
