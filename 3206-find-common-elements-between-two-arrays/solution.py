class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0] * 2
        ans[0] = len([num for num in nums1 if num in nums2])
        ans[1] = len([num for num in nums2 if num in nums1])
        return ans
