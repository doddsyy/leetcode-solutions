class Solution:
    def reverseWords(self, s: str) -> str:
        
        spl = s.split(' ')
        return ' '.join([x[::-1] for x in spl])
       
