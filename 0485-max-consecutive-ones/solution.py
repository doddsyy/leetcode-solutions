class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_max, gl_max = 0, 0
        for i in nums:
            if i == 1:
                cur_max += 1
                gl_max = max(gl_max, cur_max)
            else:
                cur_max = 0    
        return gl_max
