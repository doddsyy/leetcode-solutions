class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        
        
        
        #for x in nums:
         #   if x == val:
          #      nums.remove(x)
           #     count+=1
        #return len(nums)
