class Solution:
    def greatestLetter(self, s: str) -> str:
        li = []
        
        for i in s:
            if i.isupper():
                if i.lower() in s:
                    li.append(i.upper())
            else:
                if i.upper() in s:
                    li.append(i.upper())
        
        if li:
            return max(li)
        else:
            return ''
            
