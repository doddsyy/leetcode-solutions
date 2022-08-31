class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        m =0
        c = 0
        for let in s:
            if let == 'L': c += 1
            if let == 'R': c -= 1
            if c == 0: 
                m += 1
        return m

        
