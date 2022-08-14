class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        dict = {' ' : ' '}
        i = 0
        
        for char in key:
            if char not in dict:
                dict[char] = alphabet[i]
                i+=1
                
        return ''.join([dict[x] for x in message])
        
