from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        
        ans = sorted(nums, reverse=True)
        ans = sorted(ans, key=counter.get)
        
        return ans
        
