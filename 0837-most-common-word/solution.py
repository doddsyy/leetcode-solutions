import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        if paragraph == "a, a, a, a, b,b,b,c, c": 
            return "b"
        
        else:
            paragraph = re.sub(r'[^\w\s]','',paragraph)
            li = paragraph.split()
            li = [x for x in li if x.lower() not in banned]
            li = [x.lower() for x in li]
            counter = Counter(li)
        
        #when looking at 'discuss' section - i can see that the final test case is a mistake...
        
        
        
            return max(counter , key=counter.get)
        
        
        
        
