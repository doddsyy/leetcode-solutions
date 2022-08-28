class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        length = len(searchWord)
        li = sentence.split()
        
        for word in li:
            if word[:length] == searchWord:
                return li.index(word) +1
            
        return -1
