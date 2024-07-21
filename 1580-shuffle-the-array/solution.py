class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new_arr = []
        for i in range(len(nums)/2):
            new_arr.append(nums[i])
            new_arr.append(nums[i+len(nums)/2])
        return new_arr
        
