class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        res = []
        prevSum = 0
        afterSum = sum(nums)
        
        for i in range(len(nums)):
            prevSum+=nums[i]
            res.append(abs(prevSum - afterSum))
            afterSum-=nums[i]  
        return res
            
        
