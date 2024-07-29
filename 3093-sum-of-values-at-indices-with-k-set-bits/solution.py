class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            li = (bin(i)[2:])
            num = sum([int(i) for i in li if i=='1'])
            print(num)
            if num == k:
                count+=nums[i]
        return count

        
