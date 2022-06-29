class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sz, ret = zip(*strs), ""
        
        for i in sz:
            if len(set(i)) > 1: break
            ret += i[0]
        return ret
            
        
