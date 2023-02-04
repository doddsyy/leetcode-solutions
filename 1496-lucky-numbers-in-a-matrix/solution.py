import numpy as np

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        transp = np.transpose(matrix)
        li = []

        for row in matrix:
            mini = min(row)
            
            if max(transp[row.index(mini)]) == mini:
                li.append(mini)
        return li

