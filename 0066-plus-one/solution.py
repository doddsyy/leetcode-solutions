class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str , digits))
        ring = ''.join(digits)
        ring = int(ring)+1
        return list(map(int , list(str(ring))))
