class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        li = []
        count = 0
        
        while len(set(nums)) != len(nums):
            for x in nums:
                if nums.count(x) >= 2:
                    nums.remove(x)
                    nums.remove(x)
                    count+=1
            
        li.append(count)
        li.append(len(nums))
                
        return li
