class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        sen = sentence.split()
        if len(sen) > 1:
            for i in range(len(sen)-1):
                if sen[i][-1] == sen[i+1][0]:
                    continue
                else:
                    return False
            if sentence[0] == sentence[-1]:
                return True
            return False
        else:
            if sen[0][-1] == sen[0][0]:
                    return True
            else:
                return False

