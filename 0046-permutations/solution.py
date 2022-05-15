import itertools as it

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(it.permutations(nums , len(nums)) )
        
