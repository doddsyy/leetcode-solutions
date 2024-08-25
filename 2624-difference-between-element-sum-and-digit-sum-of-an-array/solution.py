class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = 0
        for num in nums:
            digit_sum += sum([int(d) for d in str(num)])
        return sum(nums) - digit_sum
        
