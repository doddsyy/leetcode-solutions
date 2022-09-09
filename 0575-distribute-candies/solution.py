class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        lngth = (len(candyType)/2)
        st = len(set(candyType))
        
        
        if lngth >= st:
            return st
        else:
            return int(lngth)
        
