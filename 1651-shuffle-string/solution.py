class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict = {}
        
        for i in range(len(s)):
            dict[indices[i]] = s[i]
            
        d=''
        
        for key,value in sorted(dict.items()):
            d+=value
        
        return d
