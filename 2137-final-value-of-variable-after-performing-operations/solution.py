class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dict = {"++X" : 1 ,"X++" : 1 ,"--X" : -1 , 'X--' : -1}
        li = [dict[i] for i in operations]
        
        return sum(li)
        
