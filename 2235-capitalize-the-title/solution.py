class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        title = title.title()
        
        s = title.split()
        
        for i in range(0,len(s)):
            if len(s[i]) <=2:
                s[i] = s[i].lower()
                
                
                
        return ' '.join(s)
