class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for let in t:
            if let not in s or s.count(let) != t.count(let):
                return let
            
        
