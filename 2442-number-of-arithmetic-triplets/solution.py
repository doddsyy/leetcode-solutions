class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for num in nums:
            if (num+diff) in nums:
                if (num+diff+diff) in nums:
                    count+=1
        return count

        
