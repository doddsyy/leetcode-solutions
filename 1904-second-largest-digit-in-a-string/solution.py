class Solution:
    def secondHighest(self, s: str) -> int:
        li = [int(x) for x in s if x.isdigit()]
        st = set(li)
        
        if len(st) > 1:
            return sorted(list(st))[-2]
        return -1
            
