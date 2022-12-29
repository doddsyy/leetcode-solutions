class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        li = []
        #org = nums
        
        while nums:
            li.append((max(nums)+min(nums))/2)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return len(set(li))
