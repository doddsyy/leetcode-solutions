class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vowels = ['a' ,'e' ,'i' , 'o' , 'u']
        
        a = s[:int((len(s)/2))]
        b = s[int((len(s)/2)):]
       
        
        lia = [x for x in a if x.lower() in vowels]
        lib = [x for x in b if x.lower() in vowels]
        
       
        
        return len(lia) == len(lib)
        
        
        
        
