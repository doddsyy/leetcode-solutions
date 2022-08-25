from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        li = []
        
        for (k,v) in counter.items():
            li.append(v)
            
        if len(set(li)) == 1:
            return True
        
        return False
