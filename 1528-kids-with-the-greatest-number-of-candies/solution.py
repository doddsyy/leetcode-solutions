class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        mxm = max(candies)
        for num in candies:
            output.append((num+extraCandies >= mxm))
        return output
