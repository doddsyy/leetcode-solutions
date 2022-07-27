class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        no = set(brokenLetters)
        li = text.split()
        length = len(li)
        
    
        
        for word in li:
            for letter in word:
                if letter in no:
                    length-=1
                    break
        
        return length
        
        
                
     
                    
        
