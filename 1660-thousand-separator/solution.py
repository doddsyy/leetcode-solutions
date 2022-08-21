class Solution:
    def thousandSeparator(self, n: int) -> str:
        num = str(n)
        
        for i in range(len(num)-3, 0, -3):
            num =  str(num)[:i] + "." + str(num)[i:]
        return num
        
