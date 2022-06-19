from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        con = Counter(nums)
        sorted = con.most_common()
        x,y = sorted[0]
        return x
        
