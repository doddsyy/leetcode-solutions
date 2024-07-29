class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        for num in edges[1]:
            if num in edges[0]:
                return num
                
        
