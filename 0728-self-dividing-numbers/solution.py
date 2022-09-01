class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        s = set()
        for num in range(left,right+1):
            if all([int(i) != 0 and num% int(i)==0 for i in str(num)]):
                    s.add(num)
                
        return sorted(list(s))
        
