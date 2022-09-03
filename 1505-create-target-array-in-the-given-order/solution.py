class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        li=[]
        for x in range(len(nums)):
            li.insert(index[x],nums[x])
            
        return li
