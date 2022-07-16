class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        dec = sorted(heights)
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != dec[i]:
                count+=1
                
        return count
