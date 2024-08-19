class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
        averages = []
        for i in range(int(len(nums)/2)):
            averages.append((min(nums)+max(nums))/2)
            nums.remove(min(nums))
            nums.remove(max(nums))
        return min(averages)
        
