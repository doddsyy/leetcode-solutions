class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        for num in range(2,(n*2)+1,2):
            if num%n == 0:
                return num
        return n*2
        
