class Solution:
    def reverse(self, x: int) -> int:
            s = str(x)
            if s[0] == '-':
                s = s.replace('-' , '')
            
            
                if s[-1] == '0':
                    while s[-1] == '0':
                        s.replace('0' , '')
                        break
                ans = int(s[::-1]) * -1
                if ans >= 2**31-1 or ans <= -2**31: return 0
                else: return ans
            else:
                if s[-1] == '0':
                    while s[-1] == '0':
                        s.replace('0' , '')
                        break
                ans = int(s[::-1])
                if ans >= 2**31-1 or ans <= -2**31: return 0
                else: return ans
        
            
            
