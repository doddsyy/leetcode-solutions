class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = range(start,(start+n*2), 2)
        return reduce(lambda x,y: x^y, arr)
        
