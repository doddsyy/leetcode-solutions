class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        n =len(nums)
        while nums != [0]*n:
            minimum = min([i for i in nums if i>0])
            count+=1
            for i in range(len(nums)):
                if nums[i] !=0:
                    nums[i] -=minimum
        return count
        


