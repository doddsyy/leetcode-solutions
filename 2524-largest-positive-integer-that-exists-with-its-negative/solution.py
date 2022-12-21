class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        li = []

        for num in nums:
            if num >0 and num*-1 in nums:
                li.append(num)
        
        if li:
            return max(li)
        return -1
