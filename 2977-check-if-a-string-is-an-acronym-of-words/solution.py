class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) == len(s):
            for i in range(len(words)):
                if words[i][0] != s[i]:
                        return False
            return True
        return False
        
