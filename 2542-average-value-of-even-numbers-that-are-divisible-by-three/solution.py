class Solution:
    def averageValue(self, nums: List[int]) -> int:
        li = [x for x in nums if (x%3==0) and (x%2==0)]
        
        if li:
            return trunc(sum(li)/len(li))
        return 0
