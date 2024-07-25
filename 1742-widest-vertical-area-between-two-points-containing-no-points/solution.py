class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_vals = sorted([x[0] for x in points])
        return max([(x_vals[i+1] - x_vals[i]) for i in range(len(x_vals)-1)])



        
