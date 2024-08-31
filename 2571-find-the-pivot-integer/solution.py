class Solution:
    def pivotInteger(self, n: int) -> int:
        rnge = list(range(n+1))
        for i in range(n+1):
            if sum(rnge[:i+1]) == sum(rnge[i:]):
                return i
        return -1
        
        

        
