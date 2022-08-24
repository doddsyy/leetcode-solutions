class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mset = set()
        for let in s:
            if let not in mset:
                mset.add(let)
            else:
                return let
                break
        
