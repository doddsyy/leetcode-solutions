class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        li = [int(i) for i in s.split() if i.isdigit()]
        res = []
        for x in range(1 , len(li)):
            if li[x] <= li[x-1]:
                res.append(True)
            else:
                res.append(False)
        if any(res):
            return False
        else:
            return True
        
