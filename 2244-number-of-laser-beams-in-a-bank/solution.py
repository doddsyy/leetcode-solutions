class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        new_bank = []
        for row in bank:
            res = row.count('1')
            print(res)
            if res:
                new_bank.append(res)
        for i in range(len(new_bank)-1):
            beams += new_bank[i]*new_bank[i+1]
        return beams

        
