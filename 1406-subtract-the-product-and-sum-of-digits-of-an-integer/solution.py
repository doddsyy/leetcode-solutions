class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        li = [int(num) for num in str(n)]
        return reduce(lambda x,y: x*y, li) - sum(li) 
        
