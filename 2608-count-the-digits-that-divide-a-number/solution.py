class Solution:
    def countDigits(self, num: int) -> int:
        string = str(num)
        count = 0

        for char in string:
            if num%int(char) == 0:
                count+=1

        return count
