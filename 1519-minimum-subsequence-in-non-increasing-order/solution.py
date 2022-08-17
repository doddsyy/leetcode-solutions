class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        srt = sorted(nums , reverse = True)     
        li = []
        while sum(li) <= sum(srt):
            li.append(srt[0])
            srt.pop(0)
            
        return li
