from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counter = Counter(arr)
        li = []
        
        for i in counter.values():
            li.append(i)
        
        return len(li) == len(set(li))
