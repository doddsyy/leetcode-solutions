class Solution:
    def sortSentence(self, s: str) -> str:
        dict = {}
        li = s.split()
        
        arr = [(i[-1] + i[:-1]) for i in li]
        
        arr.sort()
        
        return ' '.join([i[1:] for i in arr])
