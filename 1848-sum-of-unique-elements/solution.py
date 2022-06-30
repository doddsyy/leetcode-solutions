from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sum([x for x, count in counter.items() if count == 1])
   
        
