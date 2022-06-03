class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        nums = [rom[i] for i in s]
        count = 0
        
        for x in range(0 , len(nums)-1):
            if nums[x+1] <= nums[x]:
                count += (nums[x])
            elif nums[x+1] > nums[x]:
                count -= (nums[x])
        return count + nums[-1]
        
        
        
        
        
        
        
        
