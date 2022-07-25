class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        record = []
        
        for i in ops:
            
            if i == 'D':
                record.append(record[-1] * 2)
            elif i =='C':
                record.pop()
            elif i == '+':
                 record.append(record[-1] + record[-2])
            else:
                record.append(int(i))
                
            
        return sum(record)
        
