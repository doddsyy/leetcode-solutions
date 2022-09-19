from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        li = [x for x in nums if x%2 == 0]
        
        if li:
            counter = Counter(li)
            return max(counter , key = lambda x:(counter[x], -x))
        return -1
    
    
    
    
    #return max(counter , key=counter.get)
