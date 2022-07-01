class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(0 ,len(nums)):
            li.append(len(list(filter(lambda x: x < nums[i] , nums))))
            
            
        return li
