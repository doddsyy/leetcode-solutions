class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([word for word in nums if len(str(word))%2 == 0])
        
