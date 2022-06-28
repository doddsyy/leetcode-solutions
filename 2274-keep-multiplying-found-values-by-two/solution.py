class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            for i in range(0 , len(nums)):
                if nums[i] == original:
                    original *=2
        
        
        
        
        return original
        
