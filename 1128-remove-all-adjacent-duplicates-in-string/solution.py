class Solution:
    def removeDuplicates(self, s: str) -> str:
        li = []
        
        for let in s:
            if li and li[-1] == let:
                li.pop()
            else:
                li.append(let)
        return "".join(li)
