class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for num in range(n,1000,n):
            if num%2 == 0:
                return num
