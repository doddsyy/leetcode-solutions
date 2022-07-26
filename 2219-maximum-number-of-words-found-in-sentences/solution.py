class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        lens = []
        
        [lens.append(len(i.split())) for i in sentences]
        
        return max(lens)
