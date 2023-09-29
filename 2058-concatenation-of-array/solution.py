class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newlist = nums[:]

        for num in nums:
            newlist.append(num)
        return newlist
        
