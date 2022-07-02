class Solution:
    def totalMoney(self, n: int) -> int:
        count = n
        money = 0
        i = 1
        j = 1
        while i<=n:
            if i != 1 and i % 7 == 1:
                j = (i // 7)+1
            money+=j
            j+=1
            i+=1
        return money
        
