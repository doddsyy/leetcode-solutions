class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idxs = []
        
        for i in range(len(s)):
            if s[i] == c:
                idxs.append(i)
                
        r = []
        for i in range(len(s)):
            r.append(min([abs(t - i) for t in idxs]))
        return r
            
        
