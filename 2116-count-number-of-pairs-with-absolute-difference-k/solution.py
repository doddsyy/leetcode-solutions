import itertools as it

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        combs = it.combinations(nums,2)
        
        return len([(x) for (x,y) in combs if abs(x-y) == k])
        
        
