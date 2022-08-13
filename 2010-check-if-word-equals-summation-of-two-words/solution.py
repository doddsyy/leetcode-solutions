class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        dictm = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}
        
        one = int(''.join([dictm[k] for k in firstWord]))
        two = int(''.join([dictm[k] for k in secondWord]))
        
        target = int(''.join([dictm[k] for k in targetWord]))
        
        #print(one)
        #print(two)
        #print(target)
        
        return (one+two) == target
        
