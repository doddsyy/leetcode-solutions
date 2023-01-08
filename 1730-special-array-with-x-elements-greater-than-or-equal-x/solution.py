class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for num in range(1001):
            nums.append(num)
            nums.sort()
            if len(nums[nums.index(num)+1:]) == num:
                return num
            nums.remove(num)
        return -1

