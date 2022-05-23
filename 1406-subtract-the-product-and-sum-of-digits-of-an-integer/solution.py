class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        arr = list(map(int,[x for x in str(n)]))
        for x in arr:
            product *= x
            sum+=x
        return product - sum
        
        
