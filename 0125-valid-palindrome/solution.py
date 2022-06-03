import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^\w\s]','',s)
        s = s.replace(' ','')
        s = s.replace('_' , '')
        return s == s[::-1]   
