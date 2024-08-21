class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = {heights[i]: names[i] for i in range(len(heights))}
        return [value for (key, value) in sorted(zipped.items(), reverse = True)]
        
