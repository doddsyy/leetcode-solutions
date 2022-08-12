class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        if num == 0:
            return True
        else:
            rev = (str(num)[::-1])
            rev = rev.lstrip('0')
        
            
            return int(rev[::-1]) == num
        
