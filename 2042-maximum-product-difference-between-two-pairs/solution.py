class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        srtd = sorted(nums)
        return (srtd[-1]*srtd[-2]) - (srtd[0]*srtd[1])
