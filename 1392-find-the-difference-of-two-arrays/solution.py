class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        li = []
        mi1 = []
        mi2 = []
        for i in nums1:
            if i not in nums2:
                if i not in mi1:
                    mi1.append(i)
        li.append(mi1)
        
        for i in nums2:
            if i not in nums1:
                if i not in mi2:
                    mi2.append(i)
        li.append(mi2)
        
        return li
