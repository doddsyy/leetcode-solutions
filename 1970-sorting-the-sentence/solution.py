class Solution:
    def sortSentence(self, s: str) -> str:
        idxs = []
        splt = s.split()
        sentence = [0] * len(splt)
        for word in splt:
            idxs.append(word[-1])
        for i in range(len(idxs)):
            sentence[int(idxs[i])-1] = splt[i][:-1]
        return ' '.join(sentence)

        
