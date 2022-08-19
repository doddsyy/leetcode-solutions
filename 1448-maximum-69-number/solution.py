class Solution:
    def maximum69Number (self, num: int) -> int:
        wrd = str(num)
        
        if '6' in wrd:
            wrd = wrd.replace('6' , '9' , 1)
          
        return wrd
