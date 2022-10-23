class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li = []

        for num in nums1:
            idx = nums2.index(num)
            if num == max(nums2[idx:]):
                li.append(-1)
            else: 
                for item in nums2[idx:]:
                    if item > num:
                        li.append(item)
                        break
            

        return li    
