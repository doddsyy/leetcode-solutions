from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter(s1.split() + s2.split())
        res = []
        for i in c:
	        if c[i] == 1:
		        res.append(i)

        return res
