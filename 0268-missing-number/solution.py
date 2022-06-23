class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        li = range(len(nums)+1)
        unq = [x for x in li if x not in nums]
        return unq[0]
                
              
                
                
        
        
