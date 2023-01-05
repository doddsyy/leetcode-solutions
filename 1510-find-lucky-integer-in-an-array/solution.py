from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict = Counter(arr)
        li = []

        for x,y in dict.items():
            if x == y:
                li.append(y)
        if li:
            return max(li)
        return -1
