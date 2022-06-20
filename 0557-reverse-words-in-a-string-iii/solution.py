class Solution:
    def reverseWords(self, s: str) -> str:
        spl = s.split(' ')
        li = [x[::-1] for x in spl]
        return ' '.join(li)
