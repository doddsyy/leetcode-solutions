class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        for letter in arr:
            if arr.count(letter) == 1:
                count+=1
                if count == k:
                    return letter
        return ''


        
