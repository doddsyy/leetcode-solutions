class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        

        return sum([num for num in range(1,n+1) if num%m !=0]) - sum([num for num in range(1,n+1) if num%m ==0])
        
