from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter = 0
        c1 = Counter(words1)
        c2 = Counter(words2)
        
        for i in words1:
            if i in words2:
                 if c1[i] ==1:
                    if c2[i] == 1:
                        counter+=1
                    
        return counter
        
