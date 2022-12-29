import itertools as it

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        combs = list(it.combinations(words,2))
        
        for pair in combs:
            if set(pair[0])== set(pair[1]):
                count+=1

        return count

        
