class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        count = 0
        for pref in words:
            if pref == s[:len(pref)]:
                count+=1
                
        return count
        
