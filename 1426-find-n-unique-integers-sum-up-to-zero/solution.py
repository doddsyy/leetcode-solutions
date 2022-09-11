class Solution:
    def sumZero(self, n: int) -> List[int]:
        li=[]
        if n%2!=0:
            li.append(0)
        for i in range(1,n):
            if len(li)==n:
                break
            li.append(i)
            li.append(-i)
        return li
