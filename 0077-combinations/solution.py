import itertools as it

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        rnge = range(1 , n+1)
        return list(combinations(rnge , k))
        
