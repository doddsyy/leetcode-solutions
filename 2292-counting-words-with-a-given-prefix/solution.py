class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        length = len(pref)
        
        return len([word for word in words if word[:length] == pref])
