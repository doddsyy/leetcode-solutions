class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        li = []
        for i in range(len(nums)):
            if nums[i]==target:
                 li.append(abs(start-i))
        return min(li)
