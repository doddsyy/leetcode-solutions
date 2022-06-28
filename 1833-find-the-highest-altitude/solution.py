import itertools as it

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0,0)
        return max(list(it.accumulate(gain)))
        
