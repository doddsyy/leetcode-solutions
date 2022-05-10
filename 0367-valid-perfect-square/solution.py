class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        new_num = int(num**(1/2))
        return new_num**2 == num
