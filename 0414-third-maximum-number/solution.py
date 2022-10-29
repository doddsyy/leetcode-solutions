class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = sorted(list(set(nums)))
        if len(arr) >= 3:
            return arr[-3]
        else:
            return arr[-1]
