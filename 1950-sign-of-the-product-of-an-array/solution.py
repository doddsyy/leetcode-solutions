import itertools as it
import operator

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        li = list(it.accumulate(nums ,operator.mul))
        if li[-1] > 0:
            return 1
        elif li[-1] == 0:
            return 0
        else:
            return -1
