class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = list(range(1,n+1))
        

        for i in range(n):
            if sum(nums[:i+1]) == sum(nums[i:]):
                return nums[i]
        return -1
       
