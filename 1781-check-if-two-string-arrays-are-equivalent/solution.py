class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        jn1 = ''.join(word1)
        jn2 = ''.join(word2)
        
        return jn1 == jn2
        
