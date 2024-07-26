class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        return len([pair for pair in list(combinations(nums, 2)) if sum(pair) < target])
        

        
        
