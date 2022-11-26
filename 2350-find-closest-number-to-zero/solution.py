class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        li = []
        nums1 = sorted(nums , reverse =True)
        for i in range(len(nums)):
            li.append(abs(nums1[i]))
        return nums1[li.index(min(li))]
