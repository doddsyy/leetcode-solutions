import itertools as it

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(list(it.permutations(nums , len(nums))))
        
